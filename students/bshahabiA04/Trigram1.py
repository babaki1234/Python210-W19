#--------------------------#
#Title: This is the Trigram script"
# Change log (Who,When,What)
#bshahabi,2/2/2019,Created the file"


def process_text(text):
    text = text.upper()
    text = text.replace(',', '/')
    text = text.replace('/', ' ')
    text = text.replace('(', ' ')
    text = text.replace(')', ' ')
    text = text.replace('.', ' ')

    return text.split()


def create_trigrams(words_list, n):
    ngrams_list = []

    for num in range(0, len(words_list)):
        ngram = ' '.join(words_list[num:num + n])
        ngrams_list.append(ngram)

    return ngrams_list


if __name__ == '__main__':

    text = 'This is a test for Babak Shahabi'
    words_list = process_text(text)
    trigrams = create_trigrams(words_list, 3)

    print(trigrams)