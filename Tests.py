import pytest
import Ml_model


def test_sentiment():
    assert Ml_model.predict("I love sushis") == "Positive"
    assert Ml_model.predict("There is a dog") == "Neutral"
    assert Ml_model.predict("I hate this food") == "Negative"

def test_accuracy():
    assert Ml_model.test_model_accuracy() >= 0.8, "vader accuracy is < 0.8"