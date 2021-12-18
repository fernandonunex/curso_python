def run():

    square_numbers = [i**2 for i in range(0, 101) if i % 3 != 0]

    # Long method to make this list of squares
    # for i in range(101):
    #     square = i**2
    #     if square%3 != 0:
    #         square_numbers.append(square)

    for i in square_numbers:
        print(f"El cuadrado es: {i}")


if __name__ == '__main__':
    run()
