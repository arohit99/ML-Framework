# ML Framework

This project aims to build and deploy a machine learning app adhering to the best practises in the industry. The UI is build using streamlit, scikit-learn to machine learning, mlflow for tracking, matplotlib for plots, github actions to containerise the application and deploy to heroku. The app can be viewed [here](https://mlappframework.herokuapp.com). Data scientists today frequently use notebook based environments to run experiments. While this facilitates rapid development, these are not efficient in production environment. This project builds upon concepts like OOPS, clean code, code modularisation (modules and packages), logging, config setting etc. The key steps in the development approach are:

* create an virtual environment and install dependcies using requirements.txt
* explore data, run experiments using jupyter notebooks. However notebooks will not be used as part of final application package
* create params.yml to pass parameters
* create logs_config.yml to set up logging
* config.py reads values from params/ logs_config and initilizes variables
* custom_preprocess.py will handle data cleaning and data transformations. The functions will be specific to the input dataset and will return stardadised datasets ready for plotting, ML
* components.py contains core logic for data exploration and machine learning
* pages.py builds streamlit views
* app.py is the main module that connects all modules. It also takes care of logging/ mlflow tracking.
* While python scipts created the application, we have few other components such as- dockerfile to build container image that packages all code and its dependcies into a single deployable unit, herokudeployment.yml that triggers a github action to build and push docker image to heroku platform

## Set up process:

### Run locally

To build docker image and run streamlit app locally, clone the repository and run following commands from project root directory. Open `http://localhost:8501/` to access the webapp

```bash
$ docker build -t app:latest .
$ docker run -it -p 8501:8501 --name MLApp app:latest
```

To manually push the docker image to heroku, run the following command. Access the heroku app at `https://mlappframework.herokuapp.com`


```bash
$ heroku login
$ heroku container:login
$ heroku create mlappframework
$ heroku container:push -a mlappframework web
$ heroku container:release -a mlappframework web
$ heroku open
```
