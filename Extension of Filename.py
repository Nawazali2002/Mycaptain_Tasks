def get_file_extension(filename):
    parts = filename.split('.')
    if len(parts) > 1:
        return parts[-1]
    else:
        return "No extension found"

def main():
    filename = input("Input the Filename: ")
    extension = get_file_extension(filename)
    print("The extension of the file is:", extension)

if __name__ == "__main__":
    main()
