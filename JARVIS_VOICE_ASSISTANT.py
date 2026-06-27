import speech_recognition as sr
import webbrowser
import pyttsx3 
import MusicLibrary # Custom made module of music
import utility # custom made module of utility
import requests
from google import genai
import threading

client = genai.Client(
    api_key="YOUR_API_KEY" # <-- ENTER YOUR API_KEY HERE
)

recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine_lock = threading.Lock()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
newsapi = "YOUR_NEWS_API_KEY" # <-- ENTER YOUR NEWS API_KEY HERE

def speak_old(text):
    print("Jarvis: ", text)

    with engine_lock:
        engine.stop()
        engine.say(text)
        engine.runAndWait()

# AI INTEGRATION
def askAI(question):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
                      You are Jarvis, a voice assistant.
                      Answer shortly and clearly.

                      User:
                      {question}"""
        )

        return response.text

    except Exception as e:
        print(e)
        return "AI is not working right now."

def processCommand(c):
    if "open utility_01" in c.lower():
        webbrowser.open("utility_01")
    if "open utility_02" in c.lower():
        webbrowser.open("utility_02")
    if "open utility_03" in c.lower():
        webbrowser.open("utility_03")
    if "open utility_04" in c.lower():
        webbrowser.open("utility_04")
    
    if "open" in c.lower():
        utitlities = c.lower.split(" ")[1]
        link1 = utility.web[utitlities]
        webbrowser.open(link1)
    elif "play" in c.lower():
        song = c.lower().split(" ")[1]
        link2 = MusicLibrary.music[song]
        webbrowser.open(link2)
    elif "news" in c.lower():
        r = requests.get(f"Link:{newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])

            for article in articles:
                speak_old(article['title'])
    else:
        # Let openAI handle the request from the user
        answer = askAI(c)
        speak_old(answer)

if __name__ == "__main__":
    speak_old("Initializing Jarvis....")
    while True:
        # obtain audio from the microphone
        r = recognizer

        print("recognizing...")
        # recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=5)
            word = r.recognize_google(audio) # Google integrated for better voice recognization

            #Listen for the wake word "Jarvis"
            if word.lower() == "jarvis":
                speak_old("Ya") 

                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            print("Error. {0}".format(e))
