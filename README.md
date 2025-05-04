# 🤖 Jarvis Assistant (Python Voice AI)

**Jarvis** is a Python-based voice assistant that listens to voice commands through the microphone and performs various actions like opening websites, fetching news, answering general questions using the **GROQ API**, and more.

---

## 🎯 Features

- 🎙️ Takes voice input through microphone  
- 🌐 Opens websites like:
  - Google  
  - Facebook  
  - LinkedIn  
- 📰 Tells latest news (via News API)  
- 🔎 Searches topics on Google  
- 💡 Answers general questions using GROQ API (powered by LLMs)  
- 🗣️ Responds with synthesized voice (text-to-speech)  

---

## 🧠 Technologies Used

- Python  
- `speech_recognition`  
- `pyttsx3` (text-to-speech)  
- `webbrowser`  
- `requests` (API calls)  
- GROQ API (for intelligent answers)  
- News API (for latest headlines)  

---

## 📦 Installation

1. **Clone the Repository**
```bash
git clone https://github.com/ShubhamG07/Jarvis
```

2. **Access the main folder**
```bash
cd jarvis-assistant
```

3. **Install Required Packages**
```bash
pip install -r requirements.txt
```

4. **Set Up API Keys**

- Get your GROQ API key and News API key
- Edit it in placeholder in application

5. **Run the Assistant**
```bash
python jarvis.py
```

## 🗣️ Example Commands

  -  "Open Google"

  -  "Search Python programming"

  -  "Show me latest news"

   - "What is the capital of France?"

## Notes

  -  Internet connection is required for API-based features.

  -  Make sure your microphone is working properly.

  -  Text-to-speech engine may vary across OS (e.g., sapi5 for Windows).
