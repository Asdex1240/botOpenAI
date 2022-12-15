from gtts import gTTS
from modules.reproducir import reproducir
def convertirVoz(respuesta):
    tts = gTTS(respuesta, lang="es")
    ruta = "./media/respuesta.mp3"
    tts.save(ruta)
    reproducir(ruta)