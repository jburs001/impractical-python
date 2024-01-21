"""
Program to take a sentence and output how many times
a letter appears in a bar chart.
Author: Jon Burstein
"""
from pprint import pprint
from collections import defaultdict

sentence = input("Please enter a sentence\n")

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

#default dict builds dictionary keys
barchart = defaultdict(list)
for letter in sentence:
    letter = letter.lower()
    if letter in ALPHABET:
        barchart[letter].append(letter)

pprint(barchart, width = 110)