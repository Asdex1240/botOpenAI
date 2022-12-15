import openai

def openaiQ():
    question = input("¿Que quieres preguntar? ")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        max_tokens=128,
        temperature=0.5
    )
    respuesta = response.choices[0].text
    return respuesta