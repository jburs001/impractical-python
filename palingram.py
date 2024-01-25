"""
Title: Palingram Finder
Author: Jon Burstein
Description: Program to search english language dictionary
for two word palingrams
"""
import load_dictionary

word_list = load_dictionary.load('dictionary.txt')

#find word-pair palingrams
def find_palingrams():
    """find dictionary palingrams"""
    pali_list = []
    for word in word_list:
        end = len(word) # find length used to determine indexes the program uses to slice through words
        rev_word = word[::-1] # negatively slice through word
        if end > 1:
            for i in range(end):
                # The back end of the word must be palindromic and the front end to be a reverse word in the word list (a real word)
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in word_list:
                    pali_list.append((word, rev_word[end-i:]))
                # 
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in word_list:
                    pali_list.append((rev_word[:end-i],word))
    return pali_list

palingrams = find_palingrams()

# sort palingram on first word
palingram_sorted = sorted(palingrams)

#display list of palingrams
print("\nNumber of palingrams = {}\n".format(len(palingram_sorted)))
for first, second in palingram_sorted:
    print("{}{}".format(first,second))


