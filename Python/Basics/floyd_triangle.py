def print_floyd_triangle(rows):
    num = 1
    for i in range(1, rows + 1):
        print(' '.join(str(num + j) for j in range(i)))
        num += i


def main():
    try:
        rows = int(input("Enter number of rows: "))
        if rows <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a positive integer.")
        return

    print_floyd_triangle(rows)


if __name__ == "__main__":
    main()
