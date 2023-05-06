FROM python:slim

RUN apt -y update && apt -y install git
RUN pip install pytest pylint flake8 coverage

WORKDIR /mnt
