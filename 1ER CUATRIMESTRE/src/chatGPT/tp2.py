"""
Interfaz para consultar a ChatGPT via API de OpenAI.
- Soporta historial de comandos con readline.
- Manejo de errores en tres niveles (input, API, sistema).
"""
import os
from openai import OpenAI, APIError, APIConnectionError, RateLimitError

try:
    import readline  # Historial con flecha arriba

    LAST_INPUT = ""

    while True:
        try:
            consulta = input(
                "Escribí tu consulta para chatGPT (Enter para salir): "
            ).strip()
            if not consulta:
                print("Saliendo del programa.")
                break

            readline.add_history(consulta)
            LAST_INPUT = consulta

            print(f"You: {consulta}")

            try:
                client = OpenAI(api_key=os.getenv("sk-proj-k_bThKGN3SAoLkmAXXrjpVIFxg1DcXZcTWFhcf\
                    hhM40rs3NhjzgcKdadx0rofSwkOgk0zhpc2hT3BlbkFJ2MTg1iS\
                        3K7rCMv5hqQoPlfvHSuIZ0kuz-6a2iXscy1Ck\
                            VOuvuLS80lcsBtwJ_NBuE6-1eOSSoA"))
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": consulta}]
                )
                print("chatGPT:", response.choices[0].message.content.strip())

            except (APIError, APIConnectionError, RateLimitError) as api_error:
                print(f"❌ Error de API: {api_error}")

        except (EOFError, KeyboardInterrupt) as input_error:
            print(f"❌ Interrupción: {input_error}")

except ImportError:
    print("❌ Faltan dependencias. Instala pyreadline3 en Windows:")
    print("    pip install pyreadline3")
