# gTTS Example

This repository contains a simple example of using **gTTS (Google Text-to-Speech)** in Python to convert text to speech. The example demonstrates how to create an audio file from text and play it on different operating systems.

## Features
- Convert text to speech using Google's Text-to-Speech API.
- Save the generated speech to an audio file (`.mp3`).
- Play the audio file on Windows, macOS, and Linux.

## Prerequisites
- Python 3.x

## Installation
To use this project, you need to install the `gtts` library. You can install it using `pip`:
```bash
pip install gtts
```

## Usage
1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/gtts-example.git
    cd gtts-example
    ```
2. Run the Python script to generate and play the audio:
    ```bash
    python tts_example.py
    ```
3. The script will create an output.mp3 file and play it automatically.

## Code Example
Here is a basic example of using gTTS to convert text to speech:
```python
from gtts import gTTS
import os

# Text to convert to speech
text = "안녕하세요! TTS를 사용해서 음성을 생성해보세요."

# Create a gTTS object
tts = gTTS(text=text, lang='ko')

# Save the converted audio to a file
tts.save("output.mp3")

# Play the converted file
# os.system("start output.mp3")  # Windows
os.system("afplay output.mp3")  # macOS
# os.system("mpg321 output.mp3")  # Linux
```

## Supported Languages
gTTS supports multiple languages. To specify a different language, change the lang parameter in the script. Some examples include:

- English: lang='en'
- Korean: lang='ko'
- Japanese: lang='ja'
- Spanish: lang='es'

For a full list of supported languages, see the gTTS documentation.

## Troubleshooting
If you encounter issues with playing the audio file, make sure you have an appropriate media player installed (e.g., mpg321 for Linux).
For macOS users, afplay is usually pre-installed, while Windows users can use the default start command.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing
Feel free to submit issues or pull requests if you would like to improve this example or add more features.

## Acknowledgements
gTTS (Google Text-to-Speech) - Python library for Google TTS API.
