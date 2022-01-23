# Grab the Python base image
FROM python:3.8

# Install python and pip
# COPY requirements.txt ./requirements.txt

# Add our code
COPY . /ProjectRootDir
ARG PROJECT_HOME=/ProjectRootDir


EXPOSE 8501
#ENV PATH=${PATH}:${PROJECT_HOME}
ENV PYTHONPATH=${PYTHONPATH}:${PROJECT_HOME}
#ENV PATH="${PATH}:$PWD"
#ARG p = "/ProjectRootDir"
#RUN export PATH="$PATH":./ProjectRootDir
#RUN export PATH="$PATH:/ProjectRootDir"
#RUN export PATH="$PATH:$PWD"
WORKDIR /ProjectRootDir

# Install dependencies
RUN pip install -r requirements.txt

# Run the image
CMD streamlit run --server.port $PORT ./src/app.py
#CMD streamlit run ./src/app.py
