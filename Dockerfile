FROM python:3.7

COPY . /ProjectRootDir
ARG PROJECT_HOME=/ProjectRootDir
EXPOSE 8501
ENV PYTHONPATH=${PYTHONPATH}:${PROJECT_HOME}
WORKDIR /ProjectRootDir
RUN pip install -r requirements.txt

#CMD streamlit run --server.port $PORT ./src/app.py
CMD streamlit run ./src/app.py
