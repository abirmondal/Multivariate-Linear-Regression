from datagen import data
import pandas


def main():
    print("Hello World")
    data.gen_data(2, 10, 20, 5, 8, 100)
    pr = pandas.read_csv("data.csv")
    print(pr)


if __name__ == '__main__':
    main()
