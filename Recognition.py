#speech Recognition
import speech_recognition as sr

Audio_file = ('sample.wav')
r = sr.Recognizer()#intialize the recognizer

with sr.AudioFile(Audio_file) as source:
    audio = r.record(source)#read the audio file
try:
    print("Audio File Contain: "+r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition Could Not Understand Audio: ")
except sr.RequestError:
    print('Could Not Get The Result From Google Speech Recognition')