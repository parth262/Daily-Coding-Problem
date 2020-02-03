'''
From: Twitter
Difficulty: Medium

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''

alphabets = "abcdefghijklmnopqrstuvwxyz"

def calculate_hash(ch):
    i = alphabets.index(ch.lower()) + 1
    return str(i**2 + i + 41)


hash_dict = {}


def hash_broken_word(broken_words):
    prev_hash = None
    for word in broken_words:
        word_hash = ""
        for ch in word:
            word_hash += calculate_hash(ch)
        if prev_hash:
            if prev_hash not in hash_dict:
                hash_dict[prev_hash] = []
            if word_hash not in hash_dict[prev_hash]:
                hash_dict[prev_hash].append(word_hash)

        prev_hash = word_hash
    return prev_hash

def break_and_hash_word(word):
    word_hash = ""
    broken_words = []
    for i in range(len(word)):
        broken_words.append(word[0:i+1])

    hash_dict[hash_broken_word(broken_words)] = word

def save_words_in_ds(words):
    for word in words:
        word_hashes=break_and_hash_word(word)

save_words_in_ds(["dog", "donkey", "deer", "deal"])

def get_value(input_hash, mem=[]):
    value = hash_dict[input_hash]
    if not isinstance(value, list):
        mem.append(value)
    else:
        for v in value:
            get_value(v, mem)
    return mem

def autocomplete(input):
    input_hash = ""
    for ch in input:
        input_hash += calculate_hash(ch)

    suggestions = get_value(input_hash)
    print(suggestions)

autocomplete("dea")




        
