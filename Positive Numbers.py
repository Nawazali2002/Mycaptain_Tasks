def print_positive_numbers(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    return positive_numbers

def main():
    list1 = [12, -7, 5, 64, -14]
    list2 = [12, 14, -95, 3]
    
    print("Input: list1 =", list1)
    print("Output:", ", ".join(map(str, print_positive_numbers(list1))))
    
    print("Input: list2 =", list2)
    print("Output:", print_positive_numbers(list2))

if __name__ == "__main__":
    main()
