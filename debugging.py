def divisors(num):
    divisors = [i for i in range(1,num +1) if num % i == 0]
    return divisors


def run():
    try:
        num = int(input("Ingresa un numero: "))
        if num < 0 or isinstance(num, float):
            raise ValueError
        print(divisors(num))
        print("Termino mi programa ")
    except ValueError:
        print("Debes ingresar un número entero positivo")

if __name__ == "__main__":
    run()