# 🤖 Jarvis - Voice-Activated Virtual Assistant

A Python-based virtual assistant that responds to voice commands, integrates with OpenAI's GPT model, and performs various tasks like web browsing, music playback, and news updates.

## 🌟 Features

- **Voice Activation**: Responds to "Jarvis" as a wake word
- **Natural Language Processing**: Powered by OpenAI's GPT-3.5 Turbo model
- **Text-to-Speech**: Clear voice responses using gTTS (Google Text-to-Speech)
- **Web Navigation**: Quick access to popular websites
- **Music Playback**: Play songs from a customizable library
- **News Updates**: Real-time news headlines using NewsAPI
- **Ambient Noise Adjustment**: Automatically adjusts for background noise
- **Error Handling**: Robust error management for voice recognition

## 🛠️ Technologies Used

- Python 3.13
- OpenAI API
- SpeechRecognition
- pyttsx3
- pygame
- gTTS (Google Text-to-Speech)
- NewsAPI
- Requests

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/jarvis.git
   cd jarvis
   ```

2. Install required packages:
   ```bash
   pip install openai speech_recognition pyttsx3 pygame gtts requests
   ```

3. Set up API keys:
   - Get an OpenAI API key from [OpenAI Platform](https://platform.openai.com)
   - Get a NewsAPI key from [NewsAPI](https://newsapi.org)
   - Update the API keys in `main.py` and `client.py`

## 📂 Project Structure

- `main.py`: Core assistant functionality and voice recognition
- `client.py`: OpenAI API integration setup
- `musiclibrary.py`: Music library configuration

## 🎯 Usage

1. Run the assistant:
   ```bash
   python main.py
   ```

2. Wait for "Initializing Jarvis..." prompt
3. Say "Jarvis" to activate
4. Speak your command when prompted

### Available Commands

- "Open [website]" - Opens popular websites (Google, YouTube, Stack Overflow, etc.)
- "Play [song]" - Plays music from the configured library
- "News" - Reads latest news headlines
- Any other command will be processed by GPT-3.5 for a natural response

## 🎵 Music Library

Add songs to `musiclibrary.py`:
```python
music = {
    "song_name": "youtube_url",
    # Add more songs here
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔑 Notes

- Remember to keep your API keys secure and never commit them directly to GitHub
- Consider using environment variables for API keys in production
- The assistant requires a working microphone and internet connection

## 🎯 Future Improvements

- [ ] Add more voice commands
- [ ] Implement local file operations
- [ ] Add calendar integration
- [ ] Improve error handling
- [ ] Add system control features
- [ ] Implement multi-language support

## 📞 Contact

Gaurav vashistha - gaurav.vashistha09@gmail.com
Project Link: [https://github.com/yourusername/jarvis](https://github.com/yourusername/jarvis)

---
*Made with ❤️ by Gaurav Vashistha*