string = "This tool is cool. But that owl is awful. MAGIC TOOLS Ltd."
words = string.split()
matched_words = []
for word in words:
    o_count = word.lower().count('o')
    if o_count == 2:
        matched_words.append(word.capitalize())
print(' '.join(matched_words))