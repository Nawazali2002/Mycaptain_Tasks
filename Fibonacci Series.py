def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def main():
    num_terms = int(input("How many terms of the Fibonacci sequence would you like to generate? "))
    fib_sequence = fibonacci(num_terms)
    print("The first", num_terms, "terms of the Fibonacci sequence are:", fib_sequence)

if __name__ == "__main__":
    main()
