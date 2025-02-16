empty_string = ""  # Empty string
single_quoted = 'Single quoted string'
double_quoted = "Double quoted string"
multiline_string = """This is a
multiline string."""

############################################
text = "Python"
print(text[-1])
print(text[1:4])

############################################
text = "  Hello, World!  "

print(text.strip())
print(text.lower())
print(text.upper())
print(text.replace("World", "Python"))
print(text.split(","))
print("Hello" in text)
print(text.find("World"))  # Output: 9
print(text.count("l"))  # Output: 3

#########################################
name = "Alice"
age = 25
print("My name is %s and I am %d years old." % (name, age))
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")

greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"

print(greeting * 3)  # HelloHelloHello

print("This is a line.\nThis is a new line.")  # Newline
print("This is a tab\tcharacter.")  # Tab
print("This is a backslash: \\")  # Backslash
print('She said, "Hello!"')  # Quotes inside a string

name[::-1]

# Count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


print(count_vowels("Hello, World!"))  # Output: 3
