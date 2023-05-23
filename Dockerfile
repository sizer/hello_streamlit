# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

EXPOSE 8080

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD streamlit run --server.port 8080 --server.enableCORS false main.py