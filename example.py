import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer

# nltk.download('punkt_tab')
# nltk.download('averaged_perceptron_tagger_eng')
# nltk.download('stopwords')
#nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

# Function to map NLTK POS tags to WordNet POS tags
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  

class preprocessing:
    def __init__(self,text):
        self.text = text
    def output(self):
        sentences = sent_tokenize(self.text)
        processed_text = []
        for sentence in sentences:
            words = word_tokenize(sentence)
            words = [word for word in words if word.lower() not in stop_words]
    
            pos_tags = pos_tag(words)
            lemmatized_words =[lemmatizer.lemmatize(word,get_wordnet_pos(tag))
            for word, tag in pos_tags]
            processed_sentence = " ".join(lemmatized_words)
            processed_text.append(processed_sentence)

        return print("Processed Text:", processed_text)
