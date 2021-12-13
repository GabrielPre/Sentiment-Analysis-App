import pytest
import Ml_model


def test_sentiment():
    assert Ml_model.predict("I love cake") == "Positive"
    assert Ml_model.predict("There is a cat") == "Neutral"
    assert Ml_model.predict("I hate this project") == "Negative"

def test_accuracy():
    assert Ml_model.test_model_accuracy() >= 0.6, "vader accuracy is < 0.6"