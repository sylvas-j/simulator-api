
import os

# ml libraries
import pandas as pd
import numpy as np
import ast
import nltk, time
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
# Import Dictionary
from gensim.corpora.dictionary import Dictionary
from keras.utils import to_categorical
import collections, itertools
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
# from keras_preprocessing.sequence import pad_sequences
from sklearn.preprocessing import (LabelBinarizer, OrdinalEncoder,LabelEncoder,MinMaxScaler)
from keras.models import load_model
# gui
from ml_helpers.EncodeDecode import TextLabelEncoderDummy as ed
from .converters import ResultSummary, OrderedLabelEncoder, TextLabelEncoderDummy


# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))    
model_r = os.path.join(directory, 'court_cases/regression_lstm.h5')
model_c = os.path.join(directory, 'court_cases/classification_lstm.h5')
# print(model)
# activity = pd.read_csv(os.path.join(directory, 'court_cases_classification/court_cases/sherloc_court_cases_7.csv'), index_col=False) 

class Predict:
    def y_cat_r():
        y = [0,1]
        y = np.array(y)
        encoded_Y, encoder_r = ed.labelencoder(y)
        dummy_y, uniques = ed.encoded_to_dummy(encoded_Y)
        return uniques, dummy_y, encoder_r

    # uniques_r, dummy_y, encoder_r = y_cat_r()

    def y_cat_c():
        y = ['money laundry', 'other crimes', 'trafficking in firearms',
                'trafficking in persons',
                'participation in organized criminal group', 'drug offences',
                'cybercrime', 'smuggling of migrants']
        y = np.array(y)
        encoded_Y, encoder_c = ed.labelencoder(y)
        dummy_y, uniques = ed.encoded_to_dummy(encoded_Y)
        return uniques, dummy_y, encoder_c

    # uniques_c, dummy_y, encoder_c = y_cat_c()

    # Function to tokenize the tweets
    def custom_tokenize(text):
        """Function that tokenizes text"""
        if not text:
            print('The text to be tokenized is a None type. Defaulting to blank string.')
            text = ''
        return word_tokenize(text)

    def clean_up(data):
        """Function that cleans up the data into a shape that can be further used for modeling"""
        data.drop_duplicates() # drop duplicate tweets
        data['text'].dropna(inplace=True) # drop any rows with missing tweets
        tokenized = data['text'].apply(Predict.custom_tokenize) # Tokenize tweets
        lower_tokens = tokenized.apply(lambda x: [t.lower() for t in x]) # Convert tokens into lower case
        alpha_only = lower_tokens.apply(lambda x: [t for t in x if t.isalpha()]) # Remove punctuations
        no_stops = alpha_only.apply(lambda x: [t for t in x if t not in stopwords.words('english')]) # remove stop words
        # no_stops.apply(lambda x: [x.remove(t) for t in x if t=='rt']) # remove acronym "rt"
        return no_stops

    def get_wordnet_pos(word):
        """Map POS tag to first character lemmatize() accepts"""
        tag = nltk.pos_tag([word])[0][1][0].upper()
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}

        return tag_dict.get(tag, wordnet.NOUN)

    def transform_text(df):
        # clean df text
        cleaned_text_chunk = Predict.clean_up(df)
        # create word dict
        dictionary = Dictionary(cleaned_text_chunk)
        # creaate corpus
        corpus = cleaned_text_chunk.apply(lambda x: dictionary.doc2bow(x))
        # rename columns
        df.rename(columns={'text':'raw_text'}, inplace=True)
        df = pd.concat([df,cleaned_text_chunk],axis=1)
        df.rename(columns={'text':'tokenized_cleaned_text'}, inplace=True)

        # Lemmatize tokens
        lemmatizer = WordNetLemmatizer()
        df['lemmatized'] = df['tokenized_cleaned_text'].apply(lambda x: [lemmatizer.lemmatize(word, Predict.get_wordnet_pos(word)) for word in x])
        df['tokens_back_to_text'] = [' '.join(map(str, l)) for l in df['lemmatized']]

        ddd = df['tokens_back_to_text'].values
        # prepare tokenizer
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(ddd)

        # integer encode the documents
        sequences = tokenizer.texts_to_sequences(ddd)
        maxlen = 25
        X = pad_sequences(sequences, maxlen=maxlen)

        return X

    def pred_r(X):
        uniques_r, dummy_y, encoder_r = Predict.y_cat_r()
        lstm = load_model(model_r)
        predictions = lstm.predict(X)
        reverse_dummy_predicted =ed.reverse_dummy_to_encoded(predictions,uniques_r)
        # reverse_encoded_y_predicted = ed.reverse_encoded_to_text(reverse_dummy_predicted)
        return reverse_dummy_predicted

    def pred_c(X):
        uniques_c, dummy_y, encoder_c = Predict.y_cat_c()
        lstm = load_model(model_c)
        predictions = lstm.predict(X)
        reverse_dummy_predicted =ed.reverse_dummy_to_encoded(predictions,uniques_c)
        reverse_encoded_y_predicted = ed.reverse_encoded_to_text(reverse_dummy_predicted,encoder_c)
        return reverse_encoded_y_predicted
