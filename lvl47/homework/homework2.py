def vowel_count(w):
    return sum(1 for x in w.lower() if x in "aeiou")