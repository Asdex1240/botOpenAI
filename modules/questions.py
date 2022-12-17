import openai
from modules.reconocimiento import voice
from modules.voz import convertirVoz
def openaiQ():
    
    convertirVoz("¿Qué quieres preguntar?")

    return openai.Completion.create(
        model="text-davinci-003",
        prompt=voice(),
        max_tokens=128,
        temperature=1
    ).choices[0].text
