import openai
from modules.reconocimiento import voice
from modules.voz import convertirVoz
def openaiQ():
    convertirVoz("¿Qué quieres preguntar?")
    question =  voice()

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        max_tokens=128,
        temperature=1
    )
    respuesta = response.choices[0].text
    print(respuesta)
    return respuesta