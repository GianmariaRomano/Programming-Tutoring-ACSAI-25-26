'''
Define a function initials(text) to analyze a string of words
and return a dictionary that maps unique initial latters to the
total count of words containing that letter.
The function must first process the input string to identify all
unique initial letters and convert all words and initials to
lowercase for consistent processing
'''

def update_frequency(freq_dict, k):
    freq_dict[k] = freq_dict.get(k, 0) + 1 # Using .get(k, 0) sets the value to 0 if the key is not present.

def initials(text):
    words = [word.lower() for word in text.split() if word]
    initials = set(word[0] for word in words)
    initials_frequency = {}
    for l in initials:
        for word in words:
            if l in word:
                update_frequency(initials_frequency, l)
    return initials_frequency