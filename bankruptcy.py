# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 01:38:27 2024

@author: 13579
"""

import pickle 
import streamlit as st 

load = open('final_svc.pkl',"rb")
model = pickle.load (load)

def predict (industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk) : 
    prediction  = model.predict([[industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk]])
    return predict 

def main(): 
    html_temp = """
    <div style="background-color:aqua;padding:10px">
    <h2 style="color:white;text-align:center;">BANKRUPTCY DETECTOR </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    industrial_risk=st.number_input("INDUSTRIAL RISK : ")
    management_risk=st.number_input("MANAGEMENT RISK : ") 
    financial_flexibility=st.number_input("FINANCIAL FLEXIBILITY : ")
    credibility=st.number_input("CREDIBILITY : ")
    competitiveness=st.number_input("COMPETITIVENESS :")
    operating_risk=st.number_input("OPERATING RISK :")
    
    if st.button('PREDICT'):
        result= predict(industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk)
        if  result==0:
            st.success("BANKRUPTCY ")
        else:
            st.success("NO BANKRUPTCY")
            
            
if __name__=='__main__':
    main()            