from nltk.stem import PorterStemmer

pst = PorterStemmer()

words_stem = ["give", "given", "giving", "gave"]

for word in words_stem:
    print(word ,":", pst.stem(word))

from nltk.stem import LancasterStemmer

lst = LancasterStemmer()

for word in words_stem:
    print(word ," : ", lst.stem(word))