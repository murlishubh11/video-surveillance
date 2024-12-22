# Video Surveillance Web App
This project is a simple Flask-based web application that allows you to stream video and monitor video feeds through a web interface. It works on macOS, Windows, and Linux, provided the necessary dependencies are installed.

## Prerequisites
Make sure you have the following installed on your system:

Python 3.7+ (recommended version 3.11)
pip (Python package manager)
Virtual Environment (for isolated Python environment)
Install Dependencies


## Clone the Repository

First, clone the repository to your local system:

git clone https://github.com/your-username/video_surveillance.git
cd video_surveillance
Set Up Virtual Environment

## Create a virtual environment for the project:

python3 -m venv myenv
Activate the virtual environment:

### On macOS/Linux:

source myenv/bin/activate
### On Windows: 

myenv\Scripts\activate

### Install Required Packages

### Install the dependencies:
pip install -r requirements.txt
If requirements.txt does not exist, install the dependencies manually:

pip install flask opencv-python-headless numpy

### After installing dependencies, you can start the Flask application:


python app.py

This will start the server on http://127.0.0.1:5000. 
You should see the following output in the terminal:


Running on http://127.0.0.1:5000/ 
Access the Web Interface



## License
This project is open-source and available under the MIT License.

