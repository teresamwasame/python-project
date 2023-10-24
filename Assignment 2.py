def check_letter(letter):
    vowels = "AEIOUaeiou"

    # Check if the letter is an alphabet
    if letter.isalpha() and len(letter) == 1:
        if letter in vowels:
            return "Vowel"
        else:
            return "Consonant"
    else:
        return "Invalid input"


# Test
letter = input("Enter a single letter: ")
result = check_letter(letter)
print(f"{letter} is {result}.")