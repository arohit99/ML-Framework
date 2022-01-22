# Grab the Python base image
FROM python:3.8

# Install python and pip
COPY requirements.txt ./requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Add our code
COPY . /rootdir
WORKDIR /rootdir
EXPOSE 8501

# Run the image
CMD streamlit run --server.port $PORT ./src/app.py
#CMD streamlit run ./src/app.py
