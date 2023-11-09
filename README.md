# Relaxation Guide
The Relaxation Guide is a Python application built using the tkinter library, which provides a graphical user interface (GUI) for guiding users through relaxation exercises and engaging in a conversation with a virtual assistant powered by OpenAI's GPT-3.5 Turbo. Updates to UI/UX coming soon.

## Features
The Relaxation Guide offers the following features:
**- Feelings-Based Relaxation Exercises**: Users can select their current emotional state (e.g., Stressed, Anxious, Sad) and access relaxation exercises tailored to their feelings.
**- Interactive Chat with Virtual Assistant**: Users can have a conversation with a virtual assistant powered by OpenAI's GPT-3.5 Turbo to discuss their thoughts and feelings.
**- Customizable Styling**: The application allows for customization of colors and fonts to enhance the user experience.

## Getting Started
To run the Relaxation Guide locally, follow these steps:
1. Clone this GitHub repository to your local machine.
2. Ensure you have Python installed. You can download Python from the [official Python website](https://www.python.org/downloads/)
3. Install the required Python packages by running the following command in your terminal:
   ```
   pip install tkinter openai
4. Obtain an OpenAI API key: You'll need an API key from OpenAI to use the chat functionality. Replace 'INSERT_API_KEY' in the send_message method with your actual API key.
5. Run the application:
   ```
   python3 relaxation-guide-v1.py
7. The application's main window will appear, and you can start exploring the relaxation exercises and having conversations with the virtual assistant

## Usage
**- Select Feelings**: Click on the buttons that represent different emotional states (e.g., Stressed, Anxious) to access relaxation exercises specific to that feeling.
**- Conversation**: Click the "Have a Conversation" button to initiate a chat with the virtual assistant. Type your messages and press "Send" or press the "Return" key to send your message. The assistant will respond with helpful information.
**- Exercise Descriptions**: Click on any exercise button to view a description of the selected exercise in a pop-up dialog.
**- Customization**: You can customize the color scheme and fonts of the application by modifying the corresponding attributes in the code.

## Dependencies
- Python 3.x
- tkinter (for GUI)
- openai (for chat funcionality)

## License 
This project is licensed under the MIT License.
