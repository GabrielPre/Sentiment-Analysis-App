# **Data Engineering Project - Sentiment Analysis Application**

## **Invitation to our Notion**
[https://www.notion.so/invite/030e457e84bb305e5f93fd9cfa967855b3924097](https://www.notion.so/invite/030e457e84bb305e5f93fd9cfa967855b3924097)

## **Running the docker image**

To run the docker image, use the following command:
```
docker run -p 5000:5000 bluplip/app:sentiment-analysis-app
```

The website is now accessible on [http://localhost:5000](http://localhost:5000).

## **Building the docker image**

Building the docker image:
```
docker build -t "sentiment-analysis" -f Dockerfile.dockerfile .
```

This will run all tests while building the image.

You can run the local image using the following command:
```
docker run -p 5000:5000 "sentiment-analysis"
```

## **Tests**
Runnig the tests is as easy as:
```
pytest --disable-warnings
```
# **Project Management**
We chose Notion for our project management because some of us had a great experience using this tool as it implement various features from many productivity tools on the market.

We divided the project in Milestones and Tasks that are part of thoses Milestones.
## **Milestones**
This was our main view with the state of our tasks, the tasks associated with a progress bar that's a custom function based on the completition of the tasks.

![Main View Tasks](./pictures/Milestones.png)
This board view allowed us to have an overview of our progress for this project.

![Board View Milestone](./pictures/Milestones_2.png)

## **Tasks**
This view was our backlog where we splitted the work for all Milestones and where we updated our progress.
![Main View Tasks](./pictures/Tasks.png)
This view gave us an overview of each tasks in each Milestone and their progress.
![Board View Tasks](./pictures/Tasks_2.png)
# **Authors**

Céline YE

Gabriel PRECIGOUT

Louis TARDY