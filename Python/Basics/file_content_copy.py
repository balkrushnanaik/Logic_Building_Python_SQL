def copy_file(source_path, destination_path):
    with open(source_path, 'rb') as source_file, open(destination_path, 'wb') as dest_file:
        dest_file.write(source_file.read())


def main():
    source = input("Enter source filename: ").strip()
    destination = input("Enter destination filename: ").strip()

    try:
        copy_file(source, destination)
        print(f"Contents copied from {source} to {destination}.")
    except FileNotFoundError:
        print(f"Source file not found: {source}")
    except IOError as error:
        print(f"Error copying file: {error}")


if __name__ == "__main__":
    main()
