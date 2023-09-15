import streamlit as st
import pandas as pd
import numpy as np
from collections import ChainMap
import joblib
import pickle
st.write("# Churn Modelling Based on Classification	:bar_chart:")

def user_input():
    st.sidebar.markdown('''# :orange[Features]   :ballot_box_with_check:''')
    st.sidebar.divider()
    st.sidebar.markdown("***If you choose 0 for a feature that means the feature doesn't exist and If you choose 1 for a feature that means the feature exists***")
    st.sidebar.divider()
    gender = st.sidebar.radio("Set Gender  :man-pouting: :woman-pouting:", ["Male", "Female"])
    if gender == "Male":
        gndr = 1
    else:
        gndr = 0
    st.sidebar.divider()
    seniorsitizen = st.sidebar.slider("SeniorCitizen", min_value=0, max_value=1, step=1)
    st.sidebar.divider()
    partner = st.sidebar.radio('Partner  :man_and_woman_holding_hands:', ["Yes", "No"])
    if partner == "Yes":
        prtnr = 1
    else:
        prtnr = 0
    st.sidebar.divider()
    dependents = st.sidebar.radio('Dependents', ["Yes", "No"])
    if dependents == "Yes":
        dep = 1
    else:
        dep = 0
    st.sidebar.divider()
    tenure = st.sidebar.slider("Tenure", min_value=1, max_value=72, step=1)
    tenr = tenure / 72
    st.sidebar.divider()
    phoneservice = st.sidebar.radio('PhoneService   :telephone:', ["Yes", "No"])
    if phoneservice == "Yes":
        phesrvce = 1
    else:
        phesrvce = 0
    st.sidebar.divider()
    multipleLines = st.sidebar.selectbox('MultipleLines', ('No phone service', 'Yes', 'No'))
    if multipleLines == "Yes":
        mltiple = 1
    else:
        mltiple = 0
    st.sidebar.divider()
    internetservice = st.sidebar.selectbox('InternetService  :globe_with_meridians:', ('DSL', 'Fiber optic', 'No'))
    if internetservice == 'DSL':
        intservice_DSL = 1
    else:
        intservice_DSL = 0
    if internetservice == 'Fiber optic':
        intservice_Fiber = 1
    else:
        intservice_Fiber = 0
    if internetservice == 'No':
        intservice_No = 1
    else:
        intservice_No = 0
    st.sidebar.divider()
    onlinesecurity = st.sidebar.selectbox('OnlineSecurity  :lock:', ('No', 'Yes', 'No internet service'))
    if onlinesecurity == 'Yes':
        onlinesec = 1
    else:
        onlinesec = 0
    st.sidebar.divider()
    onlinebackup = st.sidebar.selectbox('OnlineBackup', ('Yes', 'No', 'No internet service'))
    if onlinebackup == 'Yes':
        onlineback = 1
    else:
        onlineback = 0
    st.sidebar.divider()
    deviceprotection = st.sidebar.selectbox('DeviceProtection', ('No', 'Yes', 'No internet service'))
    if deviceprotection == 'Yes':
        dvcepro = 1
    else:
        dvcepro = 0
    st.sidebar.divider()
    techsupport = st.sidebar.selectbox('TechSupport', ('No', 'Yes', 'No internet service'))
    if techsupport == 'Yes':
        techsup = 1
    else:
        techsup = 0
    st.sidebar.divider()
    streamingtv = st.sidebar.selectbox('StreamingTV  :tv:', ('No', 'Yes', 'No internet service'))
    if streamingtv == 'Yes':
        strmtv = 1
    else:
        strmtv = 0
    st.sidebar.divider()
    streamingmovies = st.sidebar.selectbox('StreamingMovies  :film_projector:', ('No', 'Yes', 'No internet service'))
    if streamingmovies == 'Yes':
        strmmvie = 1
    else:
        strmmvie = 0
    st.sidebar.divider()
    contract = st.sidebar.selectbox('Contract', ('Month-to-month', 'One year', 'Two year'))
    if contract == 'Month-to-month':
        contract_montomon = 1
    else:
        contract_montomon = 0
    if contract == 'One year':
        contract_oneyear = 1
    else:
        contract_oneyear = 0
    if contract == 'Two year':
        contract_twoyear = 1
    else:
        contract_twoyear = 0
    st.sidebar.divider()
    paperlessbilling = st.sidebar.radio('PaperlessBilling  	:scroll:', ["Yes", "No"])
    if paperlessbilling == "Yes":
        paperbilg = 1
    else:
        paperbilg = 0
    st.sidebar.divider()
    paymentmethod = st.sidebar.selectbox('PaymentMethod  :dollar:', ('Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'))
    if paymentmethod == 'Electronic check':
        paymethod_Elec_check = 1
    else:
        paymethod_Elec_check = 0
    if paymentmethod == 'Mailed check':
        paymethod_mail_check = 1
    else:
        paymethod_mail_check = 0
    if paymentmethod == 'Bank transfer (automatic)':
        paymethod_banktrans = 1
    else:
        paymethod_banktrans = 0
    if paymentmethod == 'Credit card (automatic)':
        paymethod_cred = 1
    else:
        paymethod_cred = 0
    st.sidebar.divider()
    monthlycharges = st.sidebar.slider("MonthlyCharges  :heavy_dollar_sign:", min_value=1, max_value=118, step=1)
    monthcharge = monthlycharges / 118
    st.sidebar.divider()
    totalcharges = st.sidebar.slider("TotalCharges  :moneybag:", min_value=18, max_value=8684, step=1)
    totcharges = totalcharges / 8684
    data = {"gender": gndr, "SeniorCitizen": seniorsitizen, "Partner": prtnr,
            "Dependents": dep, "tenure": tenr, "PhoneService": phesrvce, "MultipleLines": mltiple, "OnlineSecurity":onlinesec, "OnlineBackup": onlineback,
            "DeviceProtection": dvcepro, "TechSupport": techsup, "StreamingTV": strmtv, "StreamingMovies": strmmvie, "PaperlessBilling": paperbilg,
            "MonthlyCharges": monthcharge, "TotalCharges": totcharges,
            "InternetService_DSL": intservice_DSL,"InternetService_Fiber optic": intservice_Fiber, "InternetService_No": intservice_No,
            "Contract_Month-to-month": contract_montomon, "Contract_One year": contract_oneyear, "Contract_Two year": contract_twoyear,
            "PaymentMethod_Bank transfer (automatic)": paymethod_banktrans, "PaymentMethod_Credit card (automatic)": paymethod_cred,
            "PaymentMethod_Electronic check": paymethod_Elec_check, "PaymentMethod_Mailed check": paymethod_mail_check}
    features = pd.DataFrame(data, index=[0])
    return features
df = user_input()

model = joblib.load('churn_modeling_model.joblib')


df1 = df.copy()
df1.loc[:,'tenure'] *= 72
df1.loc[:,'MonthlyCharges'] *= 118
df1.loc[:,'TotalCharges'] *= 8684
st.table(df1)
st.divider()

t = st.sidebar.button("Predict")

if t:
    prediction = model.predict(df)
    if int(prediction) == 1:
        st.write('### Our Prediction is : 👍')
        st.divider()
    else:
        st.write('### Our Prediction is : 👎')
        st.divider()


