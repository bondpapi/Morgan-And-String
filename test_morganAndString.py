from MorganAndString.morgan_and_string import morganAndString  # Ensure the function is saved in morgan_and_string.py

# Load test input and handle line breaks
with open("morganAndstrings.txt", "r") as f:
    input_data = f.read().strip().splitlines()

# Skip the first line (number of test cases)
input_data = input_data[1:]

# Concatenate lines for `a` and `b`
a = ''.join(input_data[:len(input_data)//2])   # First half for `a`
b = ''.join(input_data[len(input_data)//2:])   # Second half for `b`

# Print to confirm parsing
print("Parsed a:", repr(a[:100]))  # Preview first 100 characters of `a`
print("Parsed b:", repr(b[:100]))  # Preview first 100 characters of `b`
print("Length of a:", len(a))
print("Length of b:", len(b))

# Run the function and capture output
output = morganAndString(a, b)

# Load expected output
with open("morganstrings_output.txt", "r") as f:
    expected_output = f.read().strip()

# Compare and print results
if output == expected_output:
    print("Test Passed")
else:
    print("Test Failed")
    print("Expected Output:", expected_output[:1000])  # Display first 1000 characters
    print("Actual Output:", output[:1000])  # Display first 1000 characters
    print("Length mismatch: Expected length", len(expected_output), "Actual length", len(output))

