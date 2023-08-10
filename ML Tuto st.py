# with Streamlit ML Tuto
import streamlit as st
import pandas as pd
import numpy as np
import pickle  #to load a saved model
import base64  #to open .gif files in streamlit app


# @st.cache is a caching mechanism that allows your app to stay performant 
# even when loading data from the web, manipulating large datasets, or performing expensive computations.

# The @st.cache(suppress_st_warning=True) decorator before the get_fvalue() 
# function indicates that the function's output should be cached by Streamlit to improve performance.
# The suppress_st_warning=True argument suppresses any warnings that may be generated by the caching process.
@st.cache(suppress_st_warning=True)

# In this app, we will use multiple widgets as sliders: selectbox and radio in the sidebar menu, 
# for which we will prepare some Python functions.The example will be a simple demo that has two pages. 
# On the homepage, it will show the data that we selected, 
# whereas the Exploration page will allow you to visualize variables in plots, and the 
# Prediction page will contain variables with a button named Predict that will allow you to estimate the loan status. The code below gives you a selectbox on the sidebar which allows you to select a page. The data is cached so that it does not need to reload constantly.

# map the string values "No" and "Yes" to the integer values 1 and 2, respectively.
def get_fvalue(val):
    feature_dict = {"No":1,"Yes":2}
    for key,value in feature_dict.items():
        if val == key:
            return value

# if val is equal to a key in the dictionary.
# If it is, the corresponding value is returned.
def get_value(val,my_dict):    
    for key,value in my_dict.items():        
        if val == key:            
            return value
        
# The variable app_mode is defined using the st.sidebar.selectbox() function from the Streamlit library.
# This function creates a dropdown menu in the sidebar of a Streamlit app with the options "Home" and "Prediction".
# The selected option is stored in the app_mode variable.

app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction']) #two pages


if app_mode=='Home':    
    st.title('LOAN PREDICTION :')      
    st.image('loan_image.jpg')    
    st.markdown('Dataset :')    
    data=pd.read_csv('loan_dataset.csv')    
    st.write(data.head())    
    st.markdown('Applicant Income VS Loan Amount ')    
    st.bar_chart(data[['ApplicantIncome','LoanAmount']].head(20))
elif app_mode == 'Prediction':    
    st.image('slider-short-3.jpg')    
    st.subheader('Sir/Mme , YOU need to fill all necessary informations in order    to get a reply to your loan request !')    
    st.sidebar.header("Informations about the client :")    
    gender_dict = {"Male":1,"Female":2}    
    feature_dict = {"No":1,"Yes":2}    
    edu={'Graduate':1,'Not Graduate':2}    
    prop={'Rural':1,'Urban':2,'Semiurban':3}    
    ApplicantIncome=st.sidebar.slider('ApplicantIncome',0,10000,0,)    
    CoapplicantIncome=st.sidebar.slider('CoapplicantIncome',0,10000,0,)    
    LoanAmount=st.sidebar.slider('LoanAmount in K$',9.0,700.0,200.0)    
    Loan_Amount_Term=st.sidebar.selectbox('Loan_Amount_Term',(12.0,36.0,60.0,84.0,120.0,180.0,240.0,300.0,360.0))
    Credit_History=st.sidebar.radio('Credit_History',(0.0,1.0))    
    Gender=st.sidebar.radio('Gender',tuple(gender_dict.keys()))    
    Married=st.sidebar.radio('Married',tuple(feature_dict.keys()))    
    Self_Employed=st.sidebar.radio('Self Employed',tuple(feature_dict.keys()))    
    Dependents=st.sidebar.radio('Dependents',options=['0','1' , '2' , '3+'])    
    Education=st.sidebar.radio('Education',tuple(edu.keys()))    
    Property_Area=st.sidebar.radio('Property_Area',tuple(prop.keys()))    
    class_0 , class_3 , class_1,class_2 = 0,0,0,0    
    if Dependents == '0':        
        class_0 = 1    
    elif Dependents == '1':        
        class_1 = 1    
    elif Dependents == '2' :        class_2 = 1    
    else:        class_3= 1    
    Rural,Urban,Semiurban=0,0,0    
    if Property_Area == 'Urban' :        
        Urban = 1    
    elif Property_Area == 'Semiurban' :        
        Semiurban = 1    
    else : Rural=1


data1= {'Gender':Gender, 'Married':Married, 'Dependents':[class_0,class_1,class_2,class_3], 'Education':Education, 'ApplicantIncome':ApplicantIncome, 'CoapplicantIncome':CoapplicantIncome, 'Self Employed':Self_Employed, 'LoanAmount':LoanAmount, 'Loan_Amount_Term':Loan_Amount_Term, 'Credit_History':Credit_History,    'Property_Area':[Rural,Urban,Semiurban],    }    
feature_list=[ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,get_value(Gender,gender_dict),get_fvalue(Married),data1['Dependents'][0],data1['Dependents'][1],data1['Dependents'][2],data1['Dependents'][3],get_value(Education,edu),get_fvalue(Self_Employed),data1['Property_Area'][0],data1['Property_Area'][1],data1['Property_Area'][2]]    
# the (1,-1) means we scaling one row and variable columns
single_sample = np.array(feature_list).reshape(1,-1)


if st.button("Predict"):        
    file_ = open("6m-rain.gif", "rb")        
    contents = file_.read()        
    data_url = base64.b64encode(contents).decode("utf-8")        
    file_.close()        
    file = open("green-cola-no.gif", "rb")        
    contents = file.read()        
    data_url_no = base64.b64encode(contents).decode("utf-8")        
    file.close()        
    loaded_model = pickle.load(open('Random_Forest.sav', 'rb'))        
    prediction = loaded_model.predict(single_sample)        
    if prediction[0] == 0 :            
        st.error(    'According to our Calculations, you will not get the loan from Bank'    )            
        st.markdown(    f'<img src="data:image/gif;base64,{data_url_no}" alt="cat gif">',    unsafe_allow_html=True,)        
    elif prediction[0] == 1 :            
        st.success(    'Congratulations!! you will get the loan from Bank'    )            
        st.markdown(    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',    unsafe_allow_html=True,    )




 