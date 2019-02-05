#Title: This is the Trigram script"
# Change log (Who,When,What)
#bshahabi,2/2/2019,Created the file"

def process_text(text):
    text = text.lower()
    text = text.replace(',', ' ')
    text = text.replace('--', ' ')
    text = text.replace('(', ' ')
    text = text.replace('-', ' ')

    return text.split()


def generate_ngrams(words_list, n):
    ngrams_list = []

    for num in range(0, len(words_list)):
        ngram = ' '.join(words_list[num:num + n])
        ngrams_list.append(ngram)

    return ngrams_list



if __name__ == '__main__':
    def readFile():
        try:
            fname = input(str("Please enter the text file's path on your local machine which like to trigram:"))
            with open(fname) as f:
                text1 = f.read().replace('\n', ' ')
            words_list = process_text(text1)
            trigrams = generate_ngrams(words_list, 3)
            print(trigrams)
        except:
            print("Wrong file name - please try again")
            fname = input(str("Please enter the text file's path on your local machine which like to trigram:"))
            with open(fname) as f:
                text1 = f.read().replace('\n', ' ')
            words_list = process_text(text1)
            trigrams = generate_ngrams(words_list, 3)
            print(trigrams)


readFile()