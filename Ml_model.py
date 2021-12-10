from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import tensorflow as tf
import pandas as pd
sid_obj = SentimentIntensityAnalyzer()


def predict(text):
    
    """ Predict the sentiment of a given text. """
    sentiment_dict = sid_obj.polarity_scores(text)
    return get_sentiment_from_compound(sentiment_dict['compound'])


def get_sentiment_from_compound(compound_score):

    """ 
    Decide the sentiment as positive, negative and neutral from a compound score. 
    :param compund_score: A float between -1 and 1
    """
    if compound_score >= 0.05:
        return "positive"
    if compound_score <= -0.05:
        return "negative"
    return "neutral"


def test_model_accuracy():
    with open("dataset.txt") as file:
        for line in file.readlines():
            id, compound, text = line.strip().split('\t')

            sentiment = get_sentiment_from_compound(float(compound))
            predicted_sentiment = predict(text)

def conf_matrix(x):
    if x[1] == 1 and x[2] == 1:
        return 'TP'
    elif x[1] == 1 and x[2] == -1:
        return 'FN'
    elif x[1] == -1 and x[2] == 1:
        return 'FP'
    elif x[1] == -1 and x[2] == -1:
        return 'TN'
    else:
        return 0

def create_dataset():
    (train_data_raw, train_labels), (test_data_raw, test_labels) = tf.keras.datasets.imdb.load_data(index_from=3)
    words2idx = tf.keras.datasets.imdb.get_word_index()
    idx2words = {idx:word for word, idx in words2idx.items()}
    print('yes')
    train_ex = [idx2words[x-3] for x in train_data_raw[0][1:]] # We use x-3 because when we load the data above, we used index_form=3
    train_ex = ' '.join(train_ex)
    print(train_ex)
    imdb_reviews = []
    for review, label in zip(train_data_raw, train_labels):
        try:
            tokens = [idx2words[x-3] for x in review[1:]]
            text = ' '.join(tokens)
            imdb_reviews.append([text, label])
        except: # There is a distorted observation. For that, we need to handle the error
            print('Small index number')
            pass
    imdb_df = pd.DataFrame(imdb_reviews,columns=['Text', 'Label'])
    print(imdb_df.info())
    print('fdp')
    print(imdb_df.head(10))
    print('lessgo')
    imdb_slice = imdb_df
    print('lessgo1?')
    imdb_slice['Prediction'] = imdb_slice['Text'].apply(lambda x: 1 if sid_obj.polarity_scores(x)['compound'] >= 0 else -1)
    print("stress test 0")
    # Edit Label column 1 for Positive, -1 for Negative
    imdb_slice['Label'] = imdb_slice['Label'].apply(lambda x: -1 if x == 0 else 1)
    print("stress test 1")
    # Check if the Label column and Prediction column match for accuracy calculation
    imdb_slice['Accuracy'] = imdb_slice.apply(lambda x: 1 if x[1] == x[2] else 0, axis=1)
    print("stress test 2")
    imdb_slice['Conf_Matrix'] = imdb_slice.apply(lambda x: conf_matrix(x), axis=1)
    print("stress test 3")
    print(imdb_slice.tail(10))
    imdb_slice.to_csv('dataset.csv',index=False, encoding='utf-8')




def main():
    #test with a dataset
    create_dataset()



if __name__ == "__main__" :
    main()




