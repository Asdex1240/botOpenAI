import keyboard
import sounddevice as sd
import soundfile as s

channels = 1
rate = 44100
duration = 5

def voice():
    print('Escuchando')
    
    myrecording = sd.rec(int(duration * rate), samplerate=rate, channels=channels)  
    sd.wait()
    s.write("../media/pregunta.wav", myrecording, rate)
    print('Grabación finalizada')

voice()
