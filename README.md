# 🤖 Jarvis - AI Powered Voice Assistant

Jarvis is a Python-based AI voice assistant inspired by Jarvis - AI Assistant.  
It can listen to voice commands, open websites, play music, fetch news, and answer questions using Google's Gemini AI.

The project uses Speech Recognition for listening, Pyttsx3 for voice output, and Google Gemini API for AI responses.

---

# Features

## Voice Recognition
- Listens to user commands through microphone
- Uses Google's Speech Recognition API
- Wake word activation system

Example:- 
User: Hello
Jarvis: Ya

---

## Webiste Control
Jarvis can open any website you added in utility
file.
Example:-
Open YouTube --> Automatically opens: (YouTube Link)

---

## Music Player
Play songs using voice commands which are added in the \MusicUtility.py\ file.

Example:- 
Play song --> Automatically plays: (song)

## Gemini Integration
Jarvis uses Google's Gemini AI to answer general questions.

Example:
What is Artificial Intelligence?
Response:
Artificial Intelligence is a branch of computer science...

Powered by: Google Gemini API
Model: gemini-2.5-flash

## Technologies Used (Python Libraries)
- Python - Main Porgramming Language
- SpeechRecognition - Voice Input
- Pyttsx3 - Text to Speech
- Google GenAI - AL responses
- Requests - API calls
- Webbrowser - Website opening
NewsAPI -  News fetching

## Project Structure

```
MEGA_PROJECT_JARVIS
│
├── JARVIS_VOICE_ASSISTANT.py
│
├── MusicLibrary.py
│
├── Utility.py
│
├── README.md
│
└── .venv
```

## Libraries Installation
1. SpeechRecognition - Used for converting voice into text.

Install:
```
pip install SpeechRecognition
```
Usage:
```
import speech_recognition as sr
```
Features:
- Mircophone input
- Speech-to-text conversion
- Google speech recognition support

2. Pyttsx3 - Used for text-to-speech

Install:
```
pip install pyttsx3
```
Usage:
```
import pyttsx3
```
Features:
- Offline voice output
- Uses system voices
- No internet required

3. PyAudio - Used for microphone access.

Install:
```
pip install pyaudio
```
Usage:
```
sr.Microphone()
```
Features:
- Captures microphone audio
- Connects hardware with Python

4. Google GenAI - Used for Gemini AI integration.

Install:
```
pip install google-genai
```
Import:
```
from google import genai
```
Used for:
- AI conversations
- Question answering
- Natural language processing

5. Requests - Used for API communication.

Install:
```
pip install requests
```
Usage:
```
import requests
```
Used for:
- News API calls
- HTTP requests

6. 🔑 API Setup
- Gemini API Key
  1. Open Google AI Studio
  2. Create API key
  3. Add key in:
    ```
    client = genai.Client(
        api_key="YOUR_API_KEY"
    )
    ```

## ⚙️ Installation Guide
- Clone Repository
```
git clone YOUR_REPOSITORY_LINK
```
- Go inside folder:
```
cd "MEGA PROJECT - JARVIS"
```
- Create Virtual Environment
(Python 3.12 recommended.)

Create:
```
python -m venv .venv
```
Activate(Windows):
```
.venv\Scripts\activate
```

- Install Dependencies
```
pip install SpeechRecognition pyttsx3 requests google-genai pyaudio
```

## Running Project

Start:
```
python "JARVIS_VOICE_ASSISTANT.py"
```
Output:
```
Initializing jarvis...

Recognizing...

Listening...
```

## Example Commands
1. Open Websites
```
Hello
Open Google
```
2. AI Questions
```
Hello
What is machine learning?
```

## 🐛 Troubleshooting
- Microphone not working

Install:
```
pip install pyaudio
```
Check microphone permissions.

- Pyttsx3 no voice

Test:
```
import pyttsx3
engine = pyttsx3.init()
engine.say("Hello")
engine.runAndWait()
```

- Gemini not responding
Check:
   1. API key
   2. Internet connection
   3. Package installation

## 🔮 Future Improvements
Planned features:

- Face recognition
- Weather updates
- Email sending
- WhatsApp automation
- Smart home control
- GUI interface
- Custom wake word
- Memory system

## 👨‍💻 Author
Naitik Singh - 
Python Developer | AI Enthusiast

## ⭐ Support
If you like this project:
Give it a ⭐ on GitHub!
