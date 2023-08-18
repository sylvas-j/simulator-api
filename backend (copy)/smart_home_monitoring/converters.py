import pandas as pd
import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# get_ipython().magic(u'matplotlib inline')

from sklearn.metrics import(
    classification_report, confusion_matrix, accuracy_score, mean_squared_error, mean_absolute_error
)
from sklearn.preprocessing import (
    StandardScaler, LabelBinarizer, FunctionTransformer,PolynomialFeatures, OrdinalEncoder,LabelEncoder,MinMaxScaler
)
# from keras.utils import np_utils
from keras import utils

from sklearn.utils.validation import column_or_1d


class ResultSummary:
  # matrix = classification_report(actual,predicted,labels=[1,0])
  def classification_reportx(y_test,y_predicted):
    matrix = classification_report(y_test,y_predicted, labels=pd.unique(y_predicted))
    # matrix = classification_report(reverse_encoded_y_test,reverse_encoded_y_predicted, labels=pd.unique(reverse_encoded_y_predicted))
    print(matrix)
  # classification_reportx(reverse_encoded_y_test,reverse_encoded_y_predicted)


  # confusion_matrix(reverse_encoded_y_test, reverse_encoded_y_predicted)
  # pd.crosstab(reverse_encoded_y_test, reverse_encoded_y_predicted, rownames=['True'], colnames=['Predicted'], margins=True)
  # def confusion_matrixx(y_test, y_pred,figsize1,figsize2):
  #   %matplotlib inline
  #   # fig, ax = plt.subplots(figsize=(12,10))
  #   fig, ax = plt.subplots(figsize=(figsize1,figsize2))
  #   # cm = confusion_matrix(reverse_encoded_y_test, reverse_encoded_y_predicted)
  #   cm = confusion_matrix(y_test, y_pred)
  #   # df_cm = pd.DataFrame(cm, index=pd.unique(reverse_encoded_y_test), columns=pd.unique(reverse_encoded_y_test))
  #   df_cm = pd.DataFrame(cm, index=pd.unique(y_test), columns=pd.unique(y_test))
  #   ax = sns.heatmap(df_cm,  cbar = False, cmap="BuGn", annot=True, fmt="d", linewidths=.5, ax=ax)
  #   # plt.setp(ax.get_xticklabels(), rotation=45)
  #   plt.ylabel('True label', fontweight='bold', fontsize = 18)
  #   plt.xlabel('Predicted label', fontweight='bold', fontsize = 18) 
  #   plt.show()
  # # confusion_matrixx(reverse_encoded_y_test, reverse_encoded_y_predicted,12,10)
  


  def actual_n_predictions(reverse_encoded_y_test,reverse_encoded_y_predicted):
    for i in range(len(reverse_encoded_y_test)):
      print("Test: %s -------- Predicted: (%s)" % (reverse_encoded_y_test[i], reverse_encoded_y_predicted[i]))



def ordered_encode_python(values, uniques=None, encode=False):
    # only used in _encode below, see docstring there for details
    if uniques is None:
        uniques = list(dict.fromkeys(values))
        uniques = np.array(uniques, dtype=values.dtype)
    if encode:
        table = {val: i for i, val in enumerate(uniques)}
        try:
            encoded = np.array([table[v] for v in values])
        except KeyError as e:
            raise ValueError("y contains previously unseen labels: %s"
                             % str(e))
        return uniques, encoded
    else:
        return uniques

class OrderedLabelEncoder(LabelEncoder):
    def fit(self, y):
        y = column_or_1d(y, warn=True)
        self.classes_ = ordered_encode_python(y)
    def fit_transform(self, y):
        y = column_or_1d(y, warn=True)
        self.classes_, y = ordered_encode_python(y, encode=True)
        return y

# class for Y convertions
class TextLabelEncoderDummy:

  def labelencoder(y_df):
    # encoder = LabelEncoder()
    encoder = OrderedLabelEncoder()
    encoder.fit(y_df)
    encoded_Y = encoder.transform(y_df)
    return encoded_Y, encoder


  def encoded_to_dummy(encoded_Y):
    # convert encoder variable to dummy variable
    uniques, ids = np.unique(encoded_Y, return_inverse=True)
    dummy_y = utils.to_categorical(ids, len(uniques))
    # dummy_y = np_utils.to_categorical(encoded_Y)
    return dummy_y, uniques


  def reverse_dummy_to_encoded(y_test,uniques=None):
    reverse_dummy = uniques[y_test.argmax(1)]
    return reverse_dummy


  def reverse_encoded_to_text(reverse_dummy,encoder=None):
    reverse_encoded = encoder.inverse_transform(reverse_dummy)
    return reverse_encoded




