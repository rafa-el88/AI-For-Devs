# This code snippet demonstrates how to use the OpenAI API to generate a response from a GPT-4.1 model.
# It includes importing the OpenAI library.
from openai import OpenAI

#initializing the client. this is Key imported by command, is utilized to authenticate the client.
# The key is stored in an environment variable for security reasons.
client = OpenAI()

# Making a request model to generate a response
# role=system is used to set the context for the assistant(Instruction System Rule)
# role=user is used to provide the user's input.
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  store=True,
  max_tokens=200,
  temperature=0.2,
  messages=
  [
     {
        "role": "system",
        "content": "Você é um programador Sênior. Retorne apenas código com qualidade."
     },
     {
        "role": "user", 
        "content": "Escreva um código em Python que imprima os números de 1 a 10."
      }
  ]
)

print(completion.choices[0].message.content);
