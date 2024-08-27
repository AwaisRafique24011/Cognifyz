def generate_fibonacci(n_terms):
    # Initialize the first two terms of the Fibonacci sequence
    fib_sequence = [0, 1]

    # Generate Fibonacci sequence up to n_terms
    while len(fib_sequence) < n_terms:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence[:n_terms]

while True:
    n_terms = int(input("Enter the number of terms: "))
    if n_terms <= 0:
        print("Please enter a positive integer.")
    else:
        fibonacci_sequence = generate_fibonacci(n_terms)
        print(f"Fibonacci sequence up to {n_terms} terms:")
        print(fibonacci_sequence)
        
    check = input("Check another one ... Y/N  =  ")
    if check == str.lower("n"):
       break
    
