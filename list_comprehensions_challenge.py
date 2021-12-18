def run():
    factors = [i for i in range(0,100000) if ((i % 4 == 0) and (i % 6 == 0) and (i % 9 == 0))]

    print("The factors are:")
    print(factors)

if __name__ == '__main__':
    run()
