FROM python:3
RUN mkdir /tictactoe
WORKDIR /tictactoe
COPY requirements.txt /tictactoe/
RUN pip install -r requirements.txt
COPY ./tictactoe /tictactoe/