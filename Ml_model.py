from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
sid_obj = SentimentIntensityAnalyzer()


def predict(text):
    
    """ Predict the sentiment of a given text. """
    sentiment_dict = sid_obj.polarity_scores(text)
    return to_sentiment(sentiment_dict['compound'])


def to_sentiment(score):

    """ 
    Decide the sentiment as positive, negative and neutral from a compound score. 
    :param compund_score: A float between -1 and 1
    """
    if score <= -0.05:
        return "negative"
    elif score >= 0.05:
        return "positive"
    else:
        return "neutral"


def get_model_accuracy():
    """
    Returns the accuracy of the model on our dataset
    """
    df = pd.read_csv('dataset.tsv', sep='\t', names=['index', 'score', 'tweet'])

    df['real_sentiment'] = df['score'].apply(lambda score: to_sentiment(score))
    df['prediction'] = df['tweet'].apply(lambda tweet: predict(tweet))

    correct_predictions = (df['real_sentiment'] == df['prediction']).sum()

    return correct_predictions / len(df)



def main():
    #test with a dataset
    print('Accuracy:', get_model_accuracy())


if __name__ == "__main__" :
    main()





