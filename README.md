#Video Surveillance Web App
This project is a simple Flask-based web application that allows you to stream video and monitor video feeds through a web interface. It works on macOS, Windows, and Linux, provided the necessary dependencies are installed.

##Prerequisites
Make sure you have the following installed on your system:

Python 3.7+ (recommended version 3.11)
pip (Python package manager)
Virtual Environment (for isolated Python environment)
Install Dependencies
Clone the Repository

First, clone the repository to your local system:

bash
Copy code
git clone https://github.com/your-username/video_surveillance.git
cd video_surveillance
Set Up Virtual Environment

Create a virtual environment for the project:

bash
Copy code
python3 -m venv myenv
Activate the virtual environment:

On macOS/Linux:

bash
Copy code
source myenv/bin/activate
On Windows:

bash
Copy code
myenv\Scripts\activate
Install Required Packages

Install the dependencies:

bash
Copy code
pip install -r requirements.txt
If requirements.txt does not exist, install the dependencies manually:

bash
Copy code
pip install flask opencv-python-headless numpy
Make Sure You Have a Webcam or Virtual Camera

This application requires a webcam or a virtual camera device to stream video. On macOS, you can use software like CamTwist to create a virtual camera. On Windows, make sure your webcam is connected and working.

Running the Application
For macOS, Linux, and Windows
Start the Flask Application

After installing dependencies, you can start the Flask application:

bash
Copy code
python app.py
This will start the server on http://127.0.0.1:5000. You should see the following output in the terminal:

bash
Copy code
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
Access the Web Interface

Open a web browser and go to http://127.0.0.1:5000/. You will be able to interact with the video surveillance web interface.


##License
This project is open-source and available under the MIT License.

