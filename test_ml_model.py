import pytest
import Ml_model


def test_sentiment():
    assert Ml_model.predict("I love sushis") == "positive"
    assert Ml_model.predict("There is a dog") == "neutral"
    assert Ml_model.predict("I hate this food") == "negative"

def test_accuracy():
    assert Ml_model.get_model_accuracy() >= 0.8, "vader accuracy is < 0.8"