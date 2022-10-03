# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 06:05:54 2022

@author: K01486
"""
#pip install plotly==5.10.0
#import re
import pandas as pd
#import plotly.express as px
#import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import string
import plotly.graph_objs as go
#import chart_studio.plotly as py
#import base64
#from plotly.offline import init_notebook_mode, iplot


def col(cell_name: str):
    character = cell_name.split('-')[0]
    
    return character_number_mapping[character.lower()]

    
def row(cell_name: str):
    row_number = int(cell_name.split('-')[1])
    
    return row_number - 1

character_number_mapping = {string.ascii_lowercase[i]:i for i in range(len(string.ascii_lowercase))}



page_bg_img = '''
<style>
body {
background-image: url("https://raw.githubusercontent.com/JhonMedMu/FundAnalizerBetaVersion/main/VicctusBG.png");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Vicctus MFO Mutual Fund Analyzer: Bienvenido, Jhonatan',
                          
                          ['US Equity',
                           'EU Equity',
                           'Global Bond Funds',
                           'US Bond Funds'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'US Equity'):
    
    # page title
    st.title('US Equity')
    
    

if (selected == 'EU Equity'):
    
    # page title
    st.title('EU Equity')
    
if (selected == 'Global Bond Funds'):
    
    # page title
    st.title('Global Bond Funds')
    
if (selected == 'US Bond Funds'):
    
    # page title
    st.title('US Bond Funds')
    file_name='https://github.com/JhonMedMu/FundAnalizerBetaVersion/blob/main/US_Global_Bond_Funds.xlsx?raw=true'
    sheet_to_df_map = pd.read_excel(file_name, sheet_name=None)
    
    xls = pd.ExcelFile('https://github.com/JhonMedMu/FundAnalizerBetaVersion/blob/main/US_Global_Bond_Funds.xlsx?raw=true')
    excel_file = pd.ExcelFile('https://github.com/JhonMedMu/FundAnalizerBetaVersion/blob/main/US_Global_Bond_Funds.xlsx?raw=true', engine='openpyxl')
    
    
    SheetNames=xls.sheet_names  # see all sheet names
    
    dfr = pd.DataFrame()
    
    for sheet_name in SheetNames:
        sheet_data = {'A': []}
        df_tmp = pd.read_excel(excel_file, sheet_name, header=None)
        sheet_data['A'].append(df_tmp.loc[row('A-1'), col('A-1')])

        dfr = pd.concat([dfr, pd.DataFrame(sheet_data)])

    FundsList=dfr.values.tolist()
    
    FundsList = [''.join(ele) for ele in FundsList]
    FundsList = [LMNT.replace("[", "") for LMNT in FundsList]
    FundsList = [s.replace("]", "") for s in FundsList]
    FundsList = [s.replace("'", "") for s in FundsList]

    st.header("Seleccione un fondo")
    Fund2beAnalized = st.selectbox("Elija una opción",options=FundsList)
    IndexFund=FundsList.index(Fund2beAnalized)
    
    DataFromRoll = xls.parse(SheetNames[IndexFund],skiprows=1)

    st.header("Alpha Metrics")
    
    trace_Alpha = go.Scatter(x=DataFromRoll.Time,y=DataFromRoll['Alpha'],
                             name="Factor Alpha",line=dict(color='#17BECF'),
                             opacity=0.8)
    
    trace_TrackingError=go.Scatter(x=DataFromRoll.Time,y=DataFromRoll['Tracking Error'],
                             name="Tracking Error",line=dict(color='#7F7F7F'),
                             opacity=0.8)
    dataAlphTE = [trace_Alpha, trace_TrackingError]
    
    fig=dict(data=dataAlphTE)
    
    st.plotly_chart(fig)
    
    #st.write(Fund2beAnalized)
#df.columns = ['A', 'B', 'C']
    
 #   DataFromRoll = pd.read_excel(xls, 'LU1883851765Equity', index_col=None, usecols = "A", header = 2, nrows=0)

 #, index_col=None, na_values=['NA']
