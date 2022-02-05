import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import sys,os

PROJECTPATH = 'C:\\Users\\rohit\\Downloads\\mh\\workspace\\ML-Framework'

if PROJECTPATH not in sys.path:
    sys.path.append(PROJECTPATH)

from sklearn.model_selection import cross_val_score

from pathlib import Path
import logging
#import library.components as lib
from library.components import Data, Model
from library.custom_preprocess import extract_features
from config import config as cf
import mlflow, mlflow.sklearn

from pages import DataView,PlotView,ModelMetrics

plt.style.use('fivethirtyeight')

@st.cache
def run_model():
       
    try:
        params = cf.params["data"]
        input_file_path = os.path.join(cf.PROJECT_PATH,Path(params["file_path"]))
        logger = logging.getLogger("root")
        mlflow.set_experiment(experiment_name='CustomerChurn')
        mlflow.start_run(run_name='v1')        
        
        input_df = pd.read_csv(input_file_path)
        df = extract_features(input_df)

        data = Data(df,params)
        logger.debug(f'data obj created. df shape {df.shape}')
        mlflow.log_param("No. of x columns ", len(data.x_cols))
        dataview = DataView(input_df,df,data.col_properties().astype(str))
        plotview = PlotView(df)

        model_obj = Model(data)
        logger.debug(f'model obj created')
        model = model_obj.get_model()
        #model_obj.persist_model()
        model_metrics = model_obj.get_model_metrics()
        modelview = ModelMetrics(model_metrics)
        
        logger.info(f'confusion_matrix: {model_metrics["confusion_matrix"]}')
        logger.info(f'classification_report: {model_metrics["classification_report"]}')
        logger.info(f'cross_val_scores :{model_metrics["cross_val_scores"]}')

        mlflow.log_metric("accuracy_score", model_metrics["accuracy_score"])
        mlflow.log_metric("roc_auc_score", model_metrics["roc_auc_score"])

        true_positive = model_metrics["confusion_matrix"][0][0]
        true_negative = model_metrics["confusion_matrix"][1][1]
        false_positive = model_metrics["confusion_matrix"][0][1]
        false_negative = model_metrics["confusion_matrix"][1][0]

        mlflow.log_metric("true_positive", true_positive)
        mlflow.log_metric("true_negative", true_negative)
        mlflow.log_metric("false_positive", false_positive)
        mlflow.log_metric("false_negative", false_negative)
        # mlflow.log_metric("cross_val_scores", model_metrics["cross_val_scores"])

        mlflow.sklearn.log_model(model, "model")
        mlflow.end_run() 
        return logger,dataview,plotview,modelview
    except Exception as e:
        logger.critical(f'{type(e).__name__} exception: {str(e)}')

def main(logger,dataview,plotview,modelview):

    try:
        PAGES = {
        "Explore Data": "plots",
        "Data View": "data_view",
        "Model Metrics": "model_metrics",
        "Make Predictions":"model_serving"
    }
        st.title('Customer Churn Model')
        st.sidebar.title('Navigation')
        selection = st.sidebar.radio("Go to", list(PAGES.keys()))
        page = PAGES[selection]
        print(f'page: {page}')
        if page=="data_view":
            dataview.app()
        if page=="plots":
            plotview.app()
        if page=="model_metrics":
            modelview.app()

        logger.debug('run completed')

    except Exception as e:
        logger.critical(f'{type(e).__name__} exception: {str(e)}')

if __name__ == "__main__":
    logger,dataview,plotview,modelview = run_model()
    main(logger,dataview,plotview,modelview)

