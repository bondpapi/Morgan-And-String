def morganAndString(a: str, b: str) -> str:
    i, j = 0, 0  # Pointers to track positins in 'a' and 'b'
    len_a, len_b = len(a), len(b)
    result = []  # Stores the lexicographically minimal string

    # Append a sentinel character 'z' to both strings to handle end cases
    a += "z"
    b += "z"

    # Contune until both pointers reach the end of the strings
    while i < len_a or j < len_b:
        # Compare the remaining parts of 'a' and 'b' lexicographically
        if a[i:] <= b[j:]:
            # Append the character from 'a' to the result
            result.append(a[i])
            i += 1
        else:
            # Append the character from 'b' to the result
            result.append(b[j])
            j += 1

    return "".join(result)


def main():
    # Read the number of test cases
    t = int(input("Enter the number of test cases: ").strip())

    results = []
    for _ in range(t):
        # Read the two strings for each test case
        a = input("Enter the first string: ").strip()
        b = input("Enter the second string: ").strip()

        # Compute the lexicographically minimal string
        result = morganAndString(a, b)

        # Store result for the test case
        results.append(result)

    # Print all the results
    print("\nResults:")
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
