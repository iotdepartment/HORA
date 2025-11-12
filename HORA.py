import time
from datetime import datetime

def mostrar_hora_cada_10_segundos():
    try:
        while True:
            hora_actual = datetime.now().strftime("%H:%M:%S")
            print("Hora actual:", hora_actual)
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nPrograma detenido por el usuario.")

if __name__ == "__main__":
    mostrar_hora_cada_10_segundos()
