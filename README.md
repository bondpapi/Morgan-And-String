# Morgan and a String

## Problem Description

Jack and Daniel love collecting uppercase letters from newspapers. Each of them has a collection of letters stored in stacks (strings). They want to combine their collections into a single lexicographically smallest string by selecting letters from the top of each stack.

Given two strings a and b, this program creates a lexicographically minimal string by picking one character at a time from either a or b, based on which stack has the smaller "top" character. The program continues until all characters from both strings are used.

## Solution Approach

The solution uses a two-pointer approach to efficiently merge the two strings in lexicographical order:

1. ### Two Pointers:
   . We maintain pointers i and j for the current character in a and b respectively, and build the result string by picking characters  based on lexicographical order.
   . If a[i] is lexicographically smaller than b[j], we append a[i] to the result and move the pointer i forward. Otherwise, we append b[j] and move j.

2. ### Handling Ties:
    . If a[i] and b[j] are equal, we compare the substrings starting from a[i:] and b[j:] to determine which one is lexicographically smaller. This ensures that we always choose the correct character to achieve the smallest lexicographical order.
3. ### Sentinel Value:
    . We append a sentinel character 'z' to both a and b to simplify the end-of-string comparisons, ensuring we don't have to check if either pointer has reached the end of its respective string.

## Complexity

    . Time Complexity: 0(n+m) where n and m are the lengths of a and b.
    This is achieved by processing each character exactly once.

    . Space Complexity: O(n+m) for storing the final merged string.

## Usage

1. Clone or download the repository containing this code.

2. Run the script from the command line.
```python
python script_name.py
```
3. Enter the number of test cases.

4. For each test case, provide the two strings a and b.

5. The program will output the lexicographically minimal merged string for each test case.

## Edge Cases

. **One Empty String**: If one of the strings is empty, the result will be the other string.

. **Identical Strings**: If both strings are identical, the result will consist of all characters of a and b interleaved.

. **Long Strings**: The solution is optimized to handle very large strings without performance issues.

## Contributing

Feel free to submit issues or pull requests if you have any suggestions or improvements.

## License

This project is open-source and available under the MIT License.

