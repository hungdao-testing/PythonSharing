short_string = "Welcome to the world of the Python programming language."

# 1. Get the length of the string.
print(len(short_string))

# 2. Get the first character of the short_string.
print(short_string[0])


# 3. Get the last character of the short_string.
# a. By using the negative index.
print(short_string[-1])

# b. By using the "length" of the string.
print(short_string[len(short_string) - 1])

# c. Modiying the string by using index <<<< COULD NOT DO
#short_string[len(short_string) - 1] = "@"
# TypeError: 'str' object does not support item assignment

# 4. Get the substring 'the world of the Python' by using slicing.
print(short_string[11:34])

# 5. Check a substring "world of the" existing on the short_string
print("world of the" in short_string)

# 6. Check the short_string end with a suffix "language."
print(short_string.endswith("language."))

# 6. Check the short_string start with a suffix "Welcome"
print(short_string.startswith("Welcome"))

# 7. Replace the string by another string, using replace()
original_string = "Disney Land Disney"
new_string = original_string.replace("Disney", "Fairytale")
print(new_string)

# 8. Format the string by built-in function
first_name = "John"
last_name = "Lenon"
full_name = f"{first_name} {last_name}"
print(full_name)

# 9. Escape characters: using `\`
#https://www.learnbyexample.org/python-string/
print("hello \n baby")
