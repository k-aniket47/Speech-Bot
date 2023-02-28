import speech_recognition as sr
import openai
import os
import pyttsx3
from dotenv import load_dotenv

load_dotenv()
Discord_token = os.getenv("Discord_token")
OPEN_AI_API = os.getenv("OPEN_AI_API")

engine = pyttsx3.init()

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    print("You said: ", text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
response = openai.Completion.create(
    engine="davinci",
    prompt=f"Q: {text}\nA:",
    temperature=0.5,
    max_tokens=100,
    n=1,
    stop=None,
    timeout=10,
)

answer = response.choices[0].text.strip()
print("OpenAI says: ", answer)

engine.say(answer)
engine.runAndWait()
