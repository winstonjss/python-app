import time

# Función que imprime "Hola Mundo" cada 5 segundos
def print_hello_world():
    while True:
        print("Hola Mundo")
        time.sleep(5)  # Pausa de 5 segundos

# Llamada a la función
if __name__ == "__main__":
    print_hello_world()