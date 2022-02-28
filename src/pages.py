import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.metrics import roc_auc_score, accuracy_score, confusion_matrix, classification_report,plot_confusion_matrix
from sklearn.model_selection import cross_val_score
plt.style.use('fivethirtyeight')
from config import config as cf


class DataView:
    def __init__(self,input_df,df,col_properties):
        self.input_df = input_df 
        self.df = df
        self.col_properties = col_properties

    def app(self):
        st.header('Data View')

        st.subheader('Raw data') 
        st.dataframe(self.input_df.head())

        st.markdown(f"""
              data has shape `{self.input_df.shape}` \n
              unique identifier: `customerId` \n 
              Target variable: `churn`
              """)

        st.subheader('Processed data') 
        st.dataframe(self.df.head())

        st.subheader('Column properties') 
        st.dataframe(self.col_properties)

class PlotView:
    def __init__(self,df):
        self.df = df
    def app(self):
        st.header('Plots')

        st.subheader('Correlation Matrix')

        fig,ax = plt.subplots(figsize=(7,7))
        ax = sns.heatmap(
            self.df.corr(), 
            vmin=-1, vmax=1, center=0,
            cmap=sns.diverging_palette(20, 220, n=200),
            square=True
        )
        ax.set_xticklabels(
            ax.get_xticklabels(),
            rotation=45,
            horizontalalignment='right'
        )
        st.pyplot(fig)

        st.subheader('Stacked Histograms')
        cols = ['TotalCharges','MonthlyCharges','tenure'] 
        fig,ax = plt.subplots(1,len(cols),figsize=(20,7))

        for i,col in enumerate(cols):
            self.df.pivot(columns='isChurned')[col].plot(kind='hist', stacked=True,ax=ax[i],xlabel=col)
            ax[i].set_xlabel(col)
        st.pyplot(fig)

        st.subheader('Monthly Charges vs Total Charges')
        fig,ax = plt.subplots(figsize = (4,4))
        self.df[self.df['isChurned']==0][['TotalCharges','MonthlyCharges','tenure','isChurned']].plot(kind='scatter',x='MonthlyCharges',y='TotalCharges'
        ,ax=ax,label='Not Churned',c='g',alpha=0.5)
        self.df[self.df['isChurned']==1][['TotalCharges','MonthlyCharges','tenure','isChurned']].plot(kind='scatter',x='MonthlyCharges',y='TotalCharges'
        , label='Churned'
        ,ax=ax
        ,c='r',alpha=0.5)
        st.pyplot(fig)

        st.subheader('Categorical Column distributions')
        cols = ['MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract'] 
        fig,ax = plt.subplots(3,3,figsize=(15,10))

        for i,col in enumerate(cols):
            if i < 3:
                self.df[col].value_counts().plot(kind='pie',ax = ax[i,0])
            elif i < 6:
                self.df[col].value_counts().plot(kind='pie',ax = ax[i-3,1])
            elif i < 9:
                self.df[col].value_counts().plot(kind='pie',ax = ax[i-6,2])
        st.pyplot(fig)

        st.subheader('Churned customers by service type')
        cols = ['MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract'] 
        fig,ax = plt.subplots(3,3,figsize=(15,10))

        for i,col in enumerate(cols):
            if i < 3:
                self.df.groupby('isChurned')[col].value_counts().unstack(0).plot(kind='bar',ax = ax[i,0],rot=45)
                ax[i,0].set_title(col)
                ax[i,0].get_legend().remove()

            elif i < 6:
                self.df.groupby('isChurned')[col].value_counts().unstack(0).plot(kind='bar',ax = ax[i-3,1],rot=45)
                ax[i-3,1].set_title(col)
                ax[i-3,1].get_legend().remove()
            elif i < 9:
                self.df.groupby('isChurned')[col].value_counts().unstack(0).plot(kind='bar',ax = ax[i-6,2],rot=45)
                ax[i-6,2].set_title(col)
                ax[i-6,2].get_legend().remove()
        st.pyplot(fig)

class ModelMetrics:
    def __init__(self,model_metrics):
        self.model_metrics = model_metrics
    def app(self):
        st.header('ML Model Metrics')
        accuracy_score = self.model_metrics["accuracy_score"]
        roc_auc_score = self.model_metrics["roc_auc_score"]
        st.dataframe(pd.DataFrame([[accuracy_score,roc_auc_score]], columns=['accuracy_score','roc_auc_score']))

        st.subheader('Classification Report')
        st.markdown(self.model_metrics["classification_report"])

        st.subheader('Confusion Matrix')
        fig,ax = plt.subplots(figsize=(5,5))
        ax = sns.heatmap(self.model_metrics["confusion_matrix"],annot=True,fmt='g')
        ax.set_xlabel('Predicted labels')
        ax.set_ylabel('True labels')
        ax.xaxis.set_ticklabels(['Not Churned', 'Churned']); ax.yaxis.set_ticklabels(['Not Churned', 'Churned'])
        st.pyplot(fig)


