ARG AWS_ACCOUNT_NUMBER
ARG ENVIRONMENT

FROM python:3.8

ARG BASE_DIR=/bootcamp
ENV BASE_DIR=$BASE_DIR
ENV IMAGE_REPOSITORY bootcamp-dbt-image
ENV DBT_PROFILES_DIR=$BASE_DIR

# Create new dir for image, copy application and requirements.txt to your docker image
RUN mkdir $BASE_DIR
COPY bootcamp $BASE_DIR
COPY requirements.txt $BASE_DIR/requirements.txt

RUN pip install -r $BASE_DIR/requirements.txt
WORKDIR $BASE_DIR
