from datagen import data


def main():
    print("Hello World")
    dataSet = data.gen_data(2, 10, 20, 2, 4)
    print(dataSet)


if __name__ == '__main__':
    main()
