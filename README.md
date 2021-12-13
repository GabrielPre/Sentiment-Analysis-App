# Data Engineering Project - Sentiment Analysis

## Invitation to our Notion
[https://www.notion.so/invite/030e457e84bb305e5f93fd9cfa967855b3924097](https://www.notion.so/invite/030e457e84bb305e5f93fd9cfa967855b3924097)

## Running the docker image

To run the docker image, use the following command:
```
docker run -p 5000:5000 bluplip/app:DataEngineeringProject
```

The website is now accessible on [http://localhost:5000](http://localhost:5000).

## Building the docker image

Building the docker image:
```
docker build -t "sentiment-analysis" -f Dockerfile.dockerfile .
```

This will run all tests while building the image.

You can run the local image using the following command:
```
docker run -p 5000:5000 "sentiment-analysis"
```

## Tests
Runnig the tests is as easy as:
```
pytest --disable-warnings
```

# Authors

Céline YE

Gabriel PRECIGOUT

Louis TARDY