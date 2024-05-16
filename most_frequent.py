def most_frequent(input_string):
    # Convert the input string to lowercase to count frequency in a case-insensitive manner
    input_string = input_string.lower()

    # Create a dictionary to store the frequency of each letter
    frequency_dict = {}
    for letter in input_string:
        if letter.isalpha():  # Only consider alphabetic characters
            if letter in frequency_dict:
                frequency_dict[letter] += 1
            else:
                frequency_dict[letter] = 1

    # Sort the dictionary by frequency in descending order
    sorted_frequency = sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True)

    # Print the letters and their frequencies
    for letter, frequency in sorted_frequency:
        print(f"{letter} = {frequency:02}")

def main():
    input_string = input("Please enter a string: ")
    most_frequent(input_string)

if __name__ == "__main__":
    main()
