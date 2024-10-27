# Makehaton 2024 Swiss Challenge

## Overview

In this project, we tackle the Challenge 3: Drone Aircraft Inspection, where Swiss Airlines is exploring the use of drones for efficient aircraft inspections. The aim is to create a solution that balances speed, accuracy, and safety while minimizing potential hazards during the inspection process.

### Challenge Context

Drones can rapidly inspect aircraft from multiple angles, but ensuring safety around airport facilities, personnel, and the aircraft itself is crucial. The full inspection process involves capturing images, analyzing them for damage, and generating comprehensive reports. While the entire pipeline includes multiple stages—from image capture to decision-making—we focus specifically on developing an intelligent Q&A chatbot that enhances the inspection process.

## Core Solution

The core of our solution is an **AI-powered chatbot** that utilizes **OpenAI on Azure**. This chatbot leverages a **Retrieval-Augmented Generation (RAG)** approach, allowing it to:

- **Access Reports and Data**: The chatbot can retrieve and process inspection reports generated from the analysis of images. It accesses relevant data stored in a database, enabling it to provide accurate and informed responses.
- **Respond to User Queries**: Users can interact with the chatbot to ask questions regarding the condition of the aircraft, insights from the inspection reports, and recommendations based on the data analyzed.
- **Enhance User Experience**: By providing timely and relevant information, the chatbot significantly improves communication regarding aircraft inspections and helps users make informed decisions.

### Implementation Steps

1. **Chatbot Development**: We built a Flask REST API that serves as the backbone of the chatbot, handling user requests and interacting with the OpenAI API to generate responses.

2. **RAG Integration**: The RAG model allows the chatbot to access a database of inspection reports and relevant data, enhancing its ability to provide contextually appropriate answers.

3. **User Interface**: A user-friendly web frontend was developed, enabling users to input their questions and receive answers from the chatbot seamlessly.

4. **Database Connection**: The system connects to a database that stores inspection reports and associated data, ensuring that the chatbot has access to the latest information.

### Features

- **Intelligent Chat Interface**: Users can easily ask questions related to aircraft inspections and receive accurate responses.
- **Real-Time Data Access**: The chatbot retrieves data from the database in real-time, ensuring responses are based on the most up-to-date information.
- **User-Friendly Design**: The interface is designed to be accessible and easy to navigate, making it convenient for users to interact with the chatbot.

## Project Structure

The project is organized into two main folders:

- `chatbotBackend`: Contains the Python code for the Flask REST API that communicates with OpenAI's Azure service and connects to the database.
- `chatbotFrontend`: Contains the HTML structure of the web application, including CSS and JavaScript for the chatbot interface.

## Requirements

### Frontend
- A modern web browser.
- Internet connection to access the server and OpenAI's Azure API.

### Backend
- Python 3.8+
- Flask
- Flask-CORS
- A database (e.g., SQLite, PostgreSQL) to store inspection reports.

## Installation and Setup

### Backend (Flask API)

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/makehaton_2024_swiss_challenge.git
    ```
2. Navigate to the backend directory:
    ```bash
    cd makehaton_2024_swiss_challenge/chatbotBackend
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Flask server:
    ```bash
    python app.py
    ```
5. Open the frontend application in your browser:
    ```plaintext
    chatbotFrontend/index.html
    ```

## Team

### #makeitfly

Join us in our mission to leverage AI for enhancing aircraft inspection processes and improving communication about aircraft safety!
