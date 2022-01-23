# Custom data preprocessing based on file input
import pandas as pd

def extract_features(df):

    df['TotalCharges'] = df['TotalCharges'].replace(" ",None)\
                                        .astype('float64')
    df = df.assign(isGenderMale = df['gender'].replace({'Male':1,'Female':0}) \
                                .astype('boolean')) \
        .drop('gender',axis=1)
    df = df.assign(isSeniorCitizen = df['SeniorCitizen'].astype('boolean')) \
       .drop('SeniorCitizen',axis=1)
    df = df.assign(hasPartner = df['Partner'].replace({'Yes':1,'No':0}) \
                                        .astype('boolean')) \
      .drop('Partner',axis=1)
    df = df.assign(hasDependents = df['Dependents'].replace({'Yes':1,'No':0}) \
                                        .astype('boolean')) \
      .drop('Dependents',axis=1)
    df = df.assign(hasPhoneService = df['PhoneService'].replace({'Yes':1,'No':0}) \
                                        .astype('boolean')) \
      .drop('PhoneService',axis=1)
    df = df.assign(hasPaperlessBilling = df['PaperlessBilling'].replace({'Yes':1,'No':0}) \
                                        .astype('boolean')) \
      .drop('PaperlessBilling',axis=1)
    df = df.assign(isChurned = df['Churn'].replace({'Yes':1,'No':0}) \
                                        .astype('boolean')) \
      .drop('Churn',axis=1)
    return df
