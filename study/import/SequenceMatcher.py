from difflib import SequenceMatcher

str1 = 'abc'
str2 = 'abc'

ratio = SequenceMatcher(None, str1, str2).ratio()
print(ratio)
