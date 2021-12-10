from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

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

def main():
    #test some sentences 
    text="I'm so happy"
    
    sentiment_predict = predict(text) #score
    print("sentence Overall Rated As ", sentiment_predict)



if __name__ == "__main__" :
    main()




