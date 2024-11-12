import nltk
#nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize


class txt_preprocessing:
    def __init__(self,text):
      self.text = text
      
    def to_lower(self):
      self.text = self.text.lower()
      return self.text    
    def sentence_tokenize(self):
      return sent_tokenize(self.text)
    def word_tokenize(self):
      return nltk.word_tokenize(self.text)  



      
      
      
  
  
  
  # from nltk.tokenize import word_tokenize
# corpus = '''The quick brown fox jumps over the lazy dog. Say hello to my little friend. Are you talkiing to me?'''
# #print(corpus)
# #print(sent_tokenize(corpus))
# #a = word_tokenize(corpus)

# #from nltk.stem import WordNetLemmatizer


