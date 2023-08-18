from keras.utils import to_categorical
import numpy as np
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt



# class for Y convertions
class TextLabelEncoderDummy:

    def labelencoder(y_df):
        encoder = LabelEncoder()
        encoder.fit(y_df)
        encoded_Y = encoder.transform(y_df)
        return encoded_Y, encoder


    def encoded_to_dummy(encoded_Y):
        # convert encoder variable to dummy variable
        uniques, ids = np.unique(encoded_Y, return_inverse=True)
        dummy_y = to_categorical(ids, len(uniques))
        # dummy_y = np_utils.to_categorical(encoded_Y)
        return dummy_y, uniques


    def reverse_dummy_to_encoded(y_test,uniques):
        reverse_dummy = uniques[y_test.argmax(1)]
        return reverse_dummy


    def reverse_encoded_to_text(reverse_dummy,encoder):
        reverse_encoded = encoder.inverse_transform(reverse_dummy)
        return reverse_encoded
    

# usage
# encoded_Y, encoder_r = ed.labelencoder(y)
# dummy_y, uniques = ed.encoded_to_dummy(encoded_Y)

# reverse_dummy_predicted =ed.reverse_dummy_to_encoded(predictions,uniques_c)
# reverse_encoded_y_predicted = ed.reverse_encoded_to_text(reverse_dummy_predicted,encoder_c)

class ResultSummary:
  def classification_reportx(y_test,y_predicted):
    matrix = classification_report(y_test,y_predicted, labels=pd.unique(y_test))
    print(matrix)


  def confusion_matrixx(y_test, y_pred,figsize1,figsize2):
    # %matplotlib inline
    fig, ax = plt.subplots(figsize=(figsize1,figsize2))
    cm = confusion_matrix(y_test, y_pred)
    df_cm = pd.DataFrame(cm, index=pd.unique(y_test), columns=pd.unique(y_test))
    ax = sns.heatmap(df_cm,  cbar = False, cmap="BuGn", annot=True, fmt="d", linewidths=.5, ax=ax)
    plt.ylabel('True label', fontweight='bold', fontsize = 18)
    plt.xlabel('Predicted label', fontweight='bold', fontsize = 18) 
    plt.show()  


  def actual_n_predictions(reverse_encoded_y_test,reverse_encoded_y_predicted):
    for i in range(len(reverse_encoded_y_test)):
      print("Test: %s -------- Predicted: (%s)" % (reverse_encoded_y_test[i], reverse_encoded_y_predicted[i]))
