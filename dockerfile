FROM python:slim

RUN pip install pylint flake8 coverage \
    && apt -y update \
    && apt -y install git

WORKDIR /mnt/09_01_add_mult
