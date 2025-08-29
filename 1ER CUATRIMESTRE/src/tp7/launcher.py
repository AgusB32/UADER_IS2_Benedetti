import sys
from json_reader_factory import JSONReaderFactory

VERSION = "versión 1.1"

def print_usage():
    print("\nUSO:")
    print("  python launcher.py [clave] [modo]")
    print("\nOpciones:")
    print("  -v       → Muestra la versión del programa")
    print("\nArgumentos:")
    print("  clave    → (opcional) Clave a buscar en el JSON. Por defecto: token1")
    print("  modo     → (opcional) 'singleton' (por defecto) o 'legacy'\n")

def main():
    filepath = "sitedata.json"
    allowed_modes = ["singleton", "legacy"]
    argc = len(sys.argv)

    # Versión
    if argc == 2 and sys.argv[1] == "-v":
        print(VERSION)
        return

    # Controlar exceso de argumentos
    if argc > 3:
        print("[ERROR CONTROLADO]: Demasiados argumentos.")
        print_usage()
        return

    # Recuperar argumentos con valores por defecto
    key = sys.argv[1] if argc >= 2 else "token1"
    mode = sys.argv[2] if argc == 3 else "singleton"

    # Validar modo
    if mode not in allowed_modes:
        print(f"[ERROR CONTROLADO]: Modo inválido '{mode}'. Debe ser 'singleton' o 'legacy'.")
        print_usage()
        return

    # Obtener e imprimir resultado
    reader = JSONReaderFactory.get_reader(filepath, mode)
    result = reader.get_value(key)
    print(result)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[ERROR CONTROLADO]: Fallo inesperado: {e}")
