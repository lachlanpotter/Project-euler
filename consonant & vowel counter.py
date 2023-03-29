#This program will take in an input string and output the number of space, vowels, consonants and other characters

text = input("please type in the text that you would like to be analysed: ")

vowels = "AEIOUaeiou"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

#initialising values
num_of_vowels = 0
num_of_consonants = 0
num_of_spaces = 0

#counting vowels
for char1 in text:
    for char2 in vowels:
            if char1 == char2:
                num_of_vowels += 1

#counting consonants
for char1 in text:
    for char2 in consonants:
            if char1 == char2:
                num_of_consonants += 1

#counting spaces
for char1 in text:
        if char1 == " ":
            num_of_spaces += 1

#initialising output
output_string = "Your input text has: "

#adding vowels to the output string
output_string += str(num_of_vowels)
if num_of_vowels == 1:
    output_string += " vowel, "
else:
    output_string += " vowels, "

#adding consonants to the output string
output_string += str(num_of_consonants)
if num_of_consonants == 1:
    output_string += " consonant, "
else:
    output_string += " consonants, "

#adding spaces to the output string
output_string += str(num_of_spaces)
if num_of_spaces == 1:
    output_string += " space and "
else:
    output_string += " spaces and "

#adding other characters
num_of_other_characters = len(text) - num_of_vowels - num_of_consonants - num_of_spaces
output_string += str(num_of_other_characters)
if num_of_other_characters == 1:
    output_string += " other character."
else:
    output_string += " other characters."

print(output_string)