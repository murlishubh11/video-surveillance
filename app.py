from flask import Flask, Response, render_template, request, redirect, url_for, session, flash
import cv2
import numpy as np
import atexit
import hashlib

# Set up Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# In-memory storage for users (username, password_hash)
users = {}

# Initialize video capture (0 for the default camera or a file path for video)
video_capture = cv2.VideoCapture(0)

# Check if the camera is successfully opened
if not video_capture.isOpened():
    raise RuntimeError("Could not open video device")

# Initialize VideoWriter to save video to a file (e.g., output.mp4)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 format
width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define output file (local storage)
out = None  # Initialize as None; will create once motion is detected

# Background subtraction for motion detection
background_subtractor = cv2.createBackgroundSubtractorMOG2()

# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'username' in session:
        return redirect(url_for('index'))  # If already logged in, redirect to home page
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_hash = hashlib.sha256(password.encode()).hexdigest()  # Hash the password
        users[username] = password_hash
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))  # If already logged in, redirect to home page
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_hash = hashlib.sha256(password.encode()).hexdigest()  # Hash the password

        if username in users and users[username] == password_hash:
            session['username'] = username  # Store username in session
            flash('Login successful!', 'success')
            return redirect(url_for('index'))  # Ensure the user is redirected after successful login
        else:
            flash('Invalid username or password. Please try again.', 'danger')
    return render_template('login.html')

# Logout Route
@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove username from session
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

# Home Page (Only accessible if logged in)
@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

# Video Feed (Only accessible if logged in)
@app.route('/video_feed')
def video_feed():
    if 'username' not in session:
        return redirect(url_for('login'))
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Function to generate video frames
def generate_frames():
    global out  # Declare 'out' as a global variable
    
    while True:
        # Read the next frame from the video capture
        success, frame = video_capture.read()
        if not success:
            print("Failed to capture frame")
            break
        
        print("Captured a frame")

        # Apply motion detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        motion_mask = background_subtractor.apply(gray_frame)

        # Optional: Highlight motion in the frame
        contours, _ = cv2.findContours(motion_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        motion_detected = False  # Flag to check if any motion is detected

        for contour in contours:
            if cv2.contourArea(contour) > 500:  # Ignore small movements
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                motion_detected = True  # Motion detected

        # If motion is detected, initialize or update the video writer
        if motion_detected:
            if out is None:  # Initialize VideoWriter only when motion is detected
                out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (width, height))
            out.write(frame)  # Save the frame with motion to the video file

        # Encode frame for live streaming to the browser
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

# Release video capture and video writer on exit
def release_resources():
    video_capture.release()
    if out is not None:
        out.release()  # Release the video writer
    cv2.destroyAllWindows()

atexit.register(release_resources)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
