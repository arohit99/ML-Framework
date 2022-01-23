import pandas as pd
import numpy as np 
import os,sys
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, StandardScaler
from sklearn.impute import SimpleImputer 
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split,cross_val_score,GridSearchCV
from sklearn.metrics import roc_auc_score, accuracy_score, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier
import joblib, logging
from config import config as cf
#from custom_preprocess import extract_features

logger = logging.getLogger("root")

class Data:

    def __init__(self,df,params):
        self.df = df
        self.params = params
        self.columns = df.columns
        self.x_cols = self.params["x_cols"]
        self.y_col = self.params["y_col"]
        self.x_numeric = self.params["x_numeric"]
        self.x_categorical = [c for c in self.x_cols if c not in self.x_numeric]

    def get_df(self):
        return self.df

    def column_common_values(self):
        cols_common_values = [self.df[c].value_counts().index[:4].tolist() 
                                for c in self.columns]
                                
        ser = pd.Series(cols_common_values,index=self.columns)
        return ser

    def col_properties(self):
        return pd.DataFrame( 
            {
                'type':self.df.dtypes,
                'NumofUnique':self.df.nunique(),
                'NumOfNulls':self.df.isnull().sum(),
                'CommonValues': self.column_common_values()
            }
        ).reset_index()

    def prep_data(self):

        x,y = self.df[self.x_cols],self.df[self.y_col]
        y = y.astype('int64')
        y = np.ravel(y)

        return train_test_split(x, y, test_size=0.3, random_state=0)

class Model:

    def __init__(self,data):
        self.data = data
        self.params = data.params
        self.x_train,self.x_test, self.y_train, self.y_test = data.prep_data()

        self.numeric_pipeline = Pipeline(steps=[('scale', StandardScaler())])
        self.categorical_pipeline = Pipeline(steps=[('onehot', OneHotEncoder(handle_unknown='ignore', sparse=False,drop='first'))])
        self.model_pipeline = RandomForestClassifier(n_estimators=500,max_leaf_nodes=16, n_jobs=-1)

        self.preprocess_pipeline = ColumnTransformer(transformers=[
                                                            ('number', self.numeric_pipeline, self.data.x_numeric),
                                                            ('category', self.categorical_pipeline, self.data.x_categorical)
                                                        ])
        
    def get_model(self):
        self.model = Pipeline(steps=[
                            ('preprocess', self.preprocess_pipeline),
                            ('model', self.model_pipeline)])

        return self.model.fit(self.x_train,self.y_train)

    def persist_model(self):
        model_file_path = os.path.join(cf.PROJECT_PATH,self.params['model_path'])
        joblib.dump(self.model, model_file_path)
        return 1

    def get_model_metrics(self):
        y_pred = self.model.predict(self.x_test)
        y_test = self.y_test
        model_metrics = dict()
        model_metrics['accuracy_score'] = round(accuracy_score(y_test, y_pred),2).astype(np.float64)
        model_metrics['roc_auc_score'] = round(roc_auc_score(y_test, y_pred),2).astype(np.float64)
        model_metrics['confusion_matrix'] = confusion_matrix(y_test, y_pred)
        model_metrics['classification_report'] = classification_report(y_test, y_pred)
        model_metrics['cross_val_scores'] = np.round(cross_val_score(self.model, self.x_train, self.y_train, cv=3, scoring="accuracy"),2).astype(np.float64)
        return model_metrics

