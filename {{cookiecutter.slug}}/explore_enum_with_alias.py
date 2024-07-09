from enum import Enum


class Color(Enum):
    BLUE = 1
    AZUL = 1
    RED = 2
    GREEN = 3


def main():
    print(list(Color))
    print(Color.__members__)

    # Accessing members
    print(Color.BLUE)
    print(Color.AZUL)
    print(Color.GREEN)


if __name__ == "__main__":
    main()
