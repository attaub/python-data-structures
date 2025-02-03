# 1. What is a String?
# A string is a sequence of characters enclosed in single, double, or triple quotes.
string1 = 'Hello, World!'
string2 = "Python is fun!"
string3 = """This is a multiline string."""

# 2. Creating a String
empty_string = ""  # Empty string
single_quoted = 'Single quoted string'
double_quoted = "Double quoted string"
multiline_string = """This is a
multiline string."""

# 3. Accessing String Characters
# Strings are indexed, starting from 0.
text = "Python"
print(text[0])  # Output: P
print(text[-1])  # Output: n (negative indexing starts from the end)

# 4. String Slicing
# Extract a substring using slicing.
print(text[1:4])  # Output: yth (from index 1 to 3)
print(text[:3])   # Output: Pyt (from start to index 2)
print(text[3:])   # Output: hon (from index 3 to end)

# 5. String Methods
# Python provides many built-in methods for strings.
text = "  Hello, World!  "

# Strip whitespace
print(text.strip())  # Output: "Hello, World!"

# Convert to lowercase
print(text.lower())  # Output: "  hello, world!  "

# Convert to uppercase
print(text.upper())  # Output: "  HELLO, WORLD!  "

# Replace substrings
print(text.replace("World", "Python"))  # Output: "  Hello, Python!  "

# Split into a list
print(text.split(","))  # Output: ['  Hello', ' World!  ']

# Check if a substring exists
print("Hello" in text)  # Output: True

# Find the index of a substring
print(text.find("World"))  # Output: 9

# Count occurrences of a substring
print(text.count("l"))  # Output: 3

# 6. String Formatting
# Use f-strings, format(), or %-formatting for string formatting.
name = "Alice"
age = 25

# f-strings (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")

# format() method
print("My name is {} and I am {} years old.".format(name, age))

# %-formatting (older style)
print("My name is %s and I am %d years old." % (name, age))

# 7. String Operations
# Concatenation
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)  # Output: Hello, Alice!

# Repetition
print(greeting * 3)  # Output: HelloHelloHello

# 8. Escape Characters
# Use escape characters for special formatting.
print("This is a line.\nThis is a new line.")  # Newline
print("This is a tab\tcharacter.")  # Tab
print("This is a backslash: \\")  # Backslash
print('She said, "Hello!"')  # Quotes inside a string

# 9. Multiline Strings
# Use triple quotes for multiline strings.
multiline = """This is line 1.
This is line 2.
This is line 3."""
print(multiline)

# 10. Practice Exercises
# Exercise 1: Reverse a string
def reverse_string(s):
    return s[::-1]

print(reverse_string("Python"))  # Output: nohtyP

# Exercise 2: Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False

# Exercise 3: Count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print(count_vowels("Hello, World!"))  # Output: 3
