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

```MEGA PROJECT - JARVIS

│
├── MEGA PROJECT 01 - JARVIS.py
│
├── MusicLibrary.py
│
├── Utility.py
│
├── README.md
│
└── .venv```