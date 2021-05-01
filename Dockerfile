FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /tictactoe
ADD ./tictactoe
RUN pip install -r requirements.txt