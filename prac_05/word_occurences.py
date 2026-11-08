"""
Word Occurrences
Estimate: 30 minutes
Actual: 47 minutes
"""

words_in_sentence = {}
# sentence = input("Write a sentence: ")
sentence = "mama bear papa bear baby bear"
split_words = sentence.split()
# print(words_in_sentence)
for word in split_words:
    count = words_in_sentence.get(word,0)
    words_in_sentence[word] = count + 1
maximum = max((len(word) for word in split_words))
for word in sorted(words_in_sentence):
    print(f"{word:{maximum}} : {words_in_sentence[word]}")


