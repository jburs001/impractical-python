"""
Title: Palingram Detector
Author: Jon Burstein
Description: Find palindromes in a dictionary file.
"""
import load_dictionary
word_list = load_dictionary.load('dictionary.txt')
pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print("\nNumber of Palindromes Found = {}\n".format(len(pali_list)))
print(*pali_list, sep='\n')

