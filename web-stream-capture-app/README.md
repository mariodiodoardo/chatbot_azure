# Video and Photo Capture Web Application

This project is a simple web application that allows users to capture photos and videos using their smartphone or computer's camera using HTML5 MediaDevices API.
The captured media is uploaded to a Flask server, which handles the saving of the files.

## Features

- Capture photos and videos from a device's camera.
- Upload photos and videos as Base64 strings to a Flask API.
- Save the captured photos and videos on the server.
- Display a timer (elapsed time) while recording videos.
- Responsive design for optimal user experience across devices.

## Project Structure

The project is divided into two main folders:

- `captureStreamBackend`: Contains the Python code for the rest API
- `captureStreamFrontend`: Contains the HTML structure of the web app, including css and JavaScript code for photo and video capture.

## Requirements

### Frontend
- A modern web browser with camera support.
- Internet connection to run the server.

### Backend
- Python 3.8+
- Flask
- Flask-CORS

## Installation and Setup

### Backend (Flask API)

1. Clone the repository:
    ```bash
    git clone https://github.com/maurizioidini/web-stream-capture-app.git
    ```
2. Run backend:
    ```bash
    python captureStreamBackend/app.py
    ```
3. Open in your browser
    ```
    captureStreamFrontend/index.html
    ```