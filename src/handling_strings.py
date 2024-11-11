print ("Handling Strings")
print("1. Searching for a substring in a string")
text = "This is a text that contains a lot of words and one key word that is repeated several times."
key_word = "word"
print("The keyword " + key_word + " was found " + str(text.count(key_word))  + " times")

print("2. Replacing a substring in a string")
text = "This is a text that contains a lot of words and one key word that is repeated several times."
key_word = "word"
new_word = "letter"
new_text = text.replace(key_word, new_word)
print(new_text)

print("3. Splitting a string into a list of substrings")
text = "This is a text that contains a lot of words and one key word that is repeated several times."
words = text.split(" ")
print(words)

print("4. Joining a list of substrings into a single string")
words = ["This", "is", "a", "text", "that", "contains", "a", "lot", "of", "words", "and", "one", "key", "word", "that", "is", "repeated", "several", "times."]
text = " ".join(words)
print(text)

print("5. Converting a string to uppercase")
text = "This is a text that contains a lot of words and one key word that is repeated several times."
upper_text = text.upper()
print(upper_text)

print("6. Converting a string to lowercase")
text = "This is a text that contains a lot of words and one key word that is repeated several times."
lower_text = text.lower()
print(lower_text)

print("7. Removing leading and trailing whitespace from a string")
text = "   This is a text that contains a lot of words and one key word that is repeated several times.   "
trimmed_text = text.strip()
print(trimmed_text)

print("8. Checking if a string starts with a specific substring")
text = "This is a text that contains a lot of words and one key word that is repeated several times."
key_word = "This"
if text.startswith(key_word):
    print("The text starts with the key word")
else:
    print("The text does not start with the key word")

print("9. Checking if a string ends with a specific substring")
text = "This is a text that contains a lot of words and one key word that is repeated several times."
key_word = "times."
if text.endswith(key_word):
    print("The text ends with the key word")
else:
    print("The text does not end with the key word")


print("10. Getting the index of the first occurrence of a substring in a string")
text = "This is a text that contains a lot of words and one key word that is repeated several times."
key_word = "word"
index = text.find(key_word)
print("The index of the key word is: " + str(index))

print("11. Getting the index of the last occurrence of a substring in a string")
text = "This is a text that contains a lot of words and one key word that is repeated several times."
key_word = "word"
index = text.rfind(key_word)
print("The index of the key word is: " + str(index))

print("12. Checking if a string contains only alphabetic characters")
text = "This is a text that contains a lot of words and one key word that is repeated several times."
if text.isalpha():
    print("The text contains only alphabetic characters")
else:
    print("The text contains non-alphabetic characters")

print("13. Checking if a string contains only numeric characters")
text = "12345"
if text.isnumeric():
    print("The text contains only numeric characters")
else:
    print("The text contains non-numeric characters")


