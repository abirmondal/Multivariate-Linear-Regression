from datagen import data


def main():
    print("Hello World")
    test = data.gen_data(2, 10, 20, 2, 4)
    print("The final data generated is: ")
    print(test)


if __name__ == '__main__':
    main()
