from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer




def main():
    #test some sentences 
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores("i'm so happy")
    print("sentence was rated as", sentiment_dict['neg']*100,"% Negative")
    print("sentence was rated as", sentiment_dict['neu']*100,"% Neutral")
    print("sentence was rated as", sentiment_dict['pos']*100,"% Positive")
    print("sentence Overall Rated As", end= " ")

    if sentiment_dict['compound'] >= 0.05 :
        print("Positive")
    elif sentiment_dict['compound'] >= 0.05 :
        print("Negative")
    else :
        print("Neutral")


if __name__ == "__main__" :
    main()




