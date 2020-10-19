ARG AWS_ACCOUNT_NUMBER
ARG ENVIRONMENT

FROM python:3.8

ARG BASE_DIR=/crypto_extract
ENV BASE_DIR=$BASE_DIR
ENV IMAGE_REPOSITORY crypto_extract-image

# Create new dir for image, copy application and requirements.txt to your docker image
RUN mkdir $BASE_DIR
COPY src $BASE_DIR
COPY requirements.txt $BASE_DIR/requirements.txt

RUN pip install -r $BASE_DIR/requirements.txt
WORKDIR $BASE_DIR
