from gtts import gTTS
import os

tts = gTTS(text='process', lang='en')
tts.save('proc.wav')

os.system('omxplayer -o local -p proc.wav > /dev/null 2>&1')
