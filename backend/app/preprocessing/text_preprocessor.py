import re

import nltk

from nltk.corpus import stopwords

from nltk.stem import WordNetLemmatizer

from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

class TextPreprocessor:

    def __init__(self):

        self.stop_words=set(stopwords.words("english"))

        self.lemmatizer=WordNetLemmatizer()

    def preprocess(self,text):

        text=text.lower()

        text=re.sub(r"[^a-zA-Z ]"," ",text)

        tokens=word_tokenize(text)

        tokens=[

            self.lemmatizer.lemmatize(word)

            for word in tokens

            if word not in self.stop_words

        ]

        return " ".join(tokens)