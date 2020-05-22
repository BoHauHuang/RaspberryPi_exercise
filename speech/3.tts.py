from gtts import gTTS
import os

tts = gTTS(text='ls', lang='en')
tts.save('hello.wav')

os.system('omxplayer -o local -p hello.wav > /dev/null 2>&1')
