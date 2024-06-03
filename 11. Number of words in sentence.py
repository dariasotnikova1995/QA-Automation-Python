def count_words_in_sentences(sentences):
    sentences_list = sentences.split('. ')
    words_count_list = []
    for sentence in sentences_list:
        words = sentence.strip().split(' ')
        words_count = len(words)
        words_count_list.append(words_count)
    return words_count_list
sentences = "Hello all. Here's pretty cold and hot. Choose yourself."
result = count_words_in_sentences(sentences)
print(result)

