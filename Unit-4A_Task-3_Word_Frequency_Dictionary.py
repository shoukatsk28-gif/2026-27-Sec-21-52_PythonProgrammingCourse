sentence = "to be or not to be"   # e.g. "to be or not to be"
words = sentence.split()          # split into words
dict_data = {}

for word in words:
    dict_data[word] = dict_data.get(word, 0) + 1

print("Frequency:", dict_data)