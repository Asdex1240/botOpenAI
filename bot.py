import os
import openai
openai.api_key = os.getenv("TOKEN")

#Hacer pregunta
question = input("¿Que quieres preguntar? ")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=question,
  max_tokens=128,
  temperature=0.5
)

#Imprimir el resultado en la consola
print(response.choices[0].text)