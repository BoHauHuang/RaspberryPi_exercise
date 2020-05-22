import speech_recognition as sr
import os
from gtts import gTTS

#obtain audio from the microphone
r=sr.Recognizer() 

#myvoice = sr.AudioFile('hello.mp3')
myvoice = sr.AudioFile('proc.wav')
with myvoice as source:
    print("Use audio file as input!")
    audio = r.record(source)

# recognize speech using Google Speech Recognition 
try:
    print("Google Speech Recognition thinks you said:")
    cmd = r.recognize_google(audio)
    print(cmd)
    if cmd == "process":
        os.system('ps')
        output = os.popen('ps').read()
        tts = gTTS(text=output, lang='en')
        tts.save('output.mp3')
        os.system('omxplayer -o local -p output.mp3 > /dev/null 2>&1')
    

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("No response from Google Speech Recognition service: {0}".format(e))
