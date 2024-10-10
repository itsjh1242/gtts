import os

from gtts import gTTS

# Text to convert to speech
text = "간장 공장 공장장은 강 공장장이고, 된장 공장 공장장은 장 공장장이다."

# Create a gTTS object
tts = gTTS(text=text, lang="ko")

# Save the converted audio to a file
tts.save("output.mp3")

# Play the converted file
# os.system("start output.mp3")  # Windows
os.system("afplay output.mp3")  # macOS
# os.system("mpg321 output.mp3")  # Linux
