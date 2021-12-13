from flask import json
from flask.testing import FlaskClient

import pytest

from app import app

test_app: FlaskClient

def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    global test_app
    app.testing = True
    test_app = app.test_client()

def predict(text):
    return test_app.get(f'classify?inputmessage=${text}').json

def test_response():
    """
    Assert the server responds with a 200 status
    """
    assert test_app.get(f'classify?inputmessage=any').status_code == 200


def test_format():
    """
    Assert the server responds with a string
    """
    response = predict('I love you')

    assert type(response) == str
    
def test_positive():
    """
    Assert the server correctly classifies positive sentences
    """
    assert predict('I love you') == 'positive'
    assert predict('I really enjoyed the weather today') == 'positive'
    assert predict("I'd like to go hiking with you") == 'positive'
    assert predict("Don't worry about it!") == 'positive'

def test_neutral():
    """
    Assert the server correctly classifies positive sentences
    """
    assert predict('How are you?') == 'neutral'
    assert predict('I do not think anything about it.') == 'neutral'
    assert predict("Oh, it is raining today.") == 'neutral'

def test_negative():
    """
    Assert the server correctly classifies negative sentences
    """
    assert predict('I hate you') == 'negative'
    assert predict('I did not like the meal') == 'negative'
    assert predict('I am sad') == 'negative'
    assert predict("Don't worry about it :(") == 'negative'
    
    