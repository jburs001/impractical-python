"""Progrom to convert words to pig latin"""

"""Function to determine if a word bgins with a vowel"""
def vowel(word):
    vowels = ('a', 'e', 'i', 'o','u')
    is_vowel = False
    if word.startswith(vowels):
        is_vowel = True
    return is_vowel

"""Function to convert words to piglatin"""
def piglatin(word):
    is_vowel = vowel(word)
    vowel_end = "way"
    cons_end = "ay"
    if is_vowel is True:
        word = word + vowel_end
        return word
        
    mod_word = word[1:] + word[0]
    mod_word = mod_word + cons_end
    return mod_word

word = input("Please enter a word.\n")
print(f"{word} in pig latin is {piglatin(word)}")


