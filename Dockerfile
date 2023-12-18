# Dockerfile
FROM python:3.11

WORKDIR /app

# Install pipenv
RUN pip install pipenv

# Copy the Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock ./

# Install dependencies
RUN pipenv install --system --deploy

# Copy any python files and the model we had to the working directory of Docker 
COPY ["predict.py", "model.joblib", "preprocessor.joblib",  "./"]

# We need to expose the 9696 port because we're not able to 
# communicate with Docker outside it
EXPOSE 9696

# If we run the Docker image, we want our churn app to be running
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "predict:app"]