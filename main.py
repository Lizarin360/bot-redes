import openai as ai
import json


try: 
    def main():
        # Reemplaza "tu-api-key-aquí" con la clave API real proporcionada por OpenAI.
        ai.api_key = "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"

        # La llamada a la API de GPT-3.
        respuesta = ai.ChatCompletion.create(
            model ="gpt-3.5-turbo",
            messages = [
                {"role": "system", "content": "eres un matematico muy experimentado"},
                {"role": "user", "content": "cual es el valor de pi"}
            ],
        )

        # Extrae e imprime el texto generado.
        generated_text = respuesta['choices'][0]['message']['content']
        print(generated_text)


    main()

except Exception as ex:
    print("Error: ",ex)

# revisar el video https://www.youtube.com/watch?v=ICTYsfKNrAI