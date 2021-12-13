FROM python:3.6
WORKDIR /code
ENV FLASK_APP=app.py 
ENV FLASK_RUN_HOST=0.0.0.0
COPY *  ./
RUN pip install -r requirements.txt

RUN ["python", "-m", "pytest", "--disable-warnings"]

EXPOSE 5000
CMD ["flask","run"]