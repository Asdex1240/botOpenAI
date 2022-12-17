from modules.questions import openaiQ
from modules.voz import convertirVoz
from modules.reconocimiento import voice
import os
import openai

openai.api_key = os.getenv("TOKEN")

op = 'Si'

def main():
    convertirVoz(openaiQ())
    os.remove('./media/pregunta.wav')
    os.remove('./media/respuesta.mp3')

while op == 'Si' or op == 'si' or op == 'Sí' or op == 'sí':
    main()
    convertirVoz('¿Desea realizar otra pregunta?, Responde Si o No')
    op = voice()

convertirVoz('Que tengas un lindo día')