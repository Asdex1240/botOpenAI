import keyboard
import sounddevice as sd
import soundfile as s
import speech_recognition as sr

recognizer = sr.Recognizer()
channels = 1
rate = 44100
duration = 5

def voice():
    print('Escuchando')
    
    myrecording = sd.rec(int(duration * rate), samplerate=rate, channels=channels)  
    sd.wait()
    ruta = "./media/pregunta.wav"
    s.write(ruta, myrecording, rate)
    audio_file = sr.AudioFile(ruta)
    with audio_file as source:
        audio = recognizer.record(source)
    result = recognizer.recognize_google(audio, language="es-ES")
    return result

