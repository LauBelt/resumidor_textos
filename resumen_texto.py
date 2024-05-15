from openai import OpenAI

class Resumentexto:
    model_openai = "gpt-3.5-turbo"

    def __init__(self, api_key):
        self.api_key = api_key

    def resumen(self, texto, idioma="es"):
        client = OpenAI(api_key=self.api_key)
        
        if idioma == "es":
            prompt = f"Resume el siguiente texto en español:\n{texto}"
        elif idioma == "en":
            prompt = f"Summarize the following text in English:\n{texto}"
        else:
            prompt = f"Resume el siguiente texto en español:\n{texto}"

        response = client.chat.completions.create(
            model=self.model_openai,
            messages=[
                {"role": "system", "content": "Eres un asistente que puede leer un texto y resumirlo en el idioma especificado. Su resumen tendrá 10 oraciones o menos."},
                {"role": "user", "content": prompt},
            ],
        )
        respuesta = response.choices[0].message.content
        client.close()
        return respuesta
