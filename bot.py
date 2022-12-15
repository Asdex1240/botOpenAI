from modules.questions import openaiQ
from modules.voz import convertirVoz
import os
import openai

openai.api_key = os.getenv("TOKEN")

op = 'Si'

def main():
    respuesta = openaiQ()
    convertirVoz(respuesta)
    print(respuesta)
    os.remove('./media/respuesta.mp3')

while op == 'Si':
    main()
    op = input('¿Desea realizar otra pregunta? (Si/No): ')
