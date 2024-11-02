from morgan_and_string import morganAndString  # Ensure your function is in morgan_and_string.py

# Load test input and skip the first line
with open("morganAndstrings.txt", "r") as f:
    input_data = f.readlines()

# Assign `a` and `b` based on the corrected line numbers
a = input_data[1].strip()  # Second line is `a`
b = input_data[2].strip()  # Third line is `b`

# Print parsed content and confirm lengths
print("String a (first 100 chars):", repr(a[:100]))  # Preview first 100 characters of `a`
print("String b (first 100 chars):", repr(b[:100]))  # Preview first 100 characters of `b`
print("Length of a:", len(a))
print("Length of b:", len(b))

# Run the function
output = morganAndString(a, b)

# Load expected output
with open("morganstrings_output.txt", "r") as f:
    expected_output = f.read().strip()

# Compare and find the divergence point
if output == expected_output:
    print("Test Passed")
else:
    print("Test Failed")
    # Find where the outputs start to differ
    min_len = min(len(output), len(expected_output))
    for index in range(min_len):
        if output[index] != expected_output[index]:
            print(f"Divergence at index {index}:")
            print(f"Expected: {expected_output[index:index+20]}")
            print(f"Actual  : {output[index:index+20]}")
            break
    # If one output is longer, log that as well
    if len(output) != len(expected_output):
        print(f"Length mismatch: Expected length {len(expected_output)}, Actual length {len(output)}")

