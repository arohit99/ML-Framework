# import sys
# from pathlib import Path

#PROJECTPATH = Path(__file__).parent.parent.absolute()
PROJECTPATH = 'C:\\Users\\rohit\\Downloads\\mh\\workspace\\ML-Framework'

# if PROJECTPATH not in sys.path:
#     sys.path.append(PROJECTPATH)

# print(sys.path)

# import streamlit as st

# st.title('Customer Churn Model')

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import cross_val_score
import sys,os
from pathlib import Path
import logging
import mlflow, mlflow.sklearn

if PROJECTPATH not in sys.path:
    sys.path.append(PROJECTPATH)

#import library.components as lib
from library.components import Data, Model
from library.custom_preprocess import extract_features
from config import config as cf
from pages import DataView,PlotView,ModelMetrics