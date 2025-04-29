import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from groq import Groq
from gtts import gTTS
import pygame
import os

recognizer=sr.Recognizer()
engine=pyttsx3.init()

newVoiceRate = 190
engine.setProperty('rate',newVoiceRate)

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
     tts=gTTS(text)
     tts.save("audio.mp3")
     # Initialize pygame mixer
     pygame.mixer.init()

     # Load your MP3 file
     pygame.mixer.music.load("audio.mp3")  # Replace with your actual file path

     # Play the MP3
     pygame.mixer.music.play()

     # Keep the program running while the music plays
     while pygame.mixer.music.get_busy():
          pygame.time.Clock().tick(10)

     pygame.mixer.music.unload()

def askAi(command):
          client = Groq(
     api_key="YOUR_GROQ_API_KEY",
     )
          chat_completion = client.chat.completions.create(
     messages=[
          {
               "role": "user",
               "content": command,
          }
     ],
     model="llama-3.3-70b-versatile",
     )
          return chat_completion.choices[0].message.content

def processComand(command):
     if "open youtube" in command.lower():
          webbrowser.open("https://www.youtube.com")
     elif "open google" in command.lower():
          webbrowser.open("https://www.google.com") 
     elif "open facebook" in command.lower():
          webbrowser.open("https://www.facebook.com")    
     elif "open linkedin" in command.lower():
          webbrowser.open("https://www.linkedin.com")  
     elif command.lower().startswith("play"): 
          song=command.lower().split(" ")[1] 
          link=musicLibrary.music[song]
          webbrowser.open(link)
     elif "search on google" in command.lower():
          term=command.lower().split(" ")[3]
          webbrowser.open(f"https://www.google.com/search?q={term}")
     elif command.lower().startswith("news"):
         q=command.lower().split(" ")[2]
         print(command)
         r= requests.get(f"https://newsapi.org/v2/everything?q={q}&apiKey=YOUR_API_KEY")

         data = r.json()
         if data.get("status") == "ok":
          articles = data.get("articles", [])
          for idx, article in enumerate(articles):
               speak(f"{idx+1}. {article['title']}")
          else:
               print("Error:", data.get("message"))
     else:
          output=askAi(command)
          speak(output)
                    

        
if __name__=="__main__":
    speak("Initializin Jarvis....")
    #Listen for the wake word "Jarvis"
    while True:
       
            try:
                with sr.Microphone() as source:
                    print("Listening ...")
                    audio = recognizer.listen(source,timeout=5,phrase_time_limit=1)
                word = recognizer.recognize_google(audio).lower()
                if "jarvis" in word:
                    speak("Yeah")
                    
                    #listen for the command after the wake word
                    with sr.Microphone() as source:
                        print("Recognizing...")
                        audio=recognizer.listen(source)
                        command = recognizer.recognize_google(audio).lower()
                        processComand(command)
                       
            
            except Exception as e:
                print(f"Could not request results; {e}")
  
