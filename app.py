import streamlit as st
from PIL import Image
import sklearn
import pandas as pd
import numpy as np

import pickle 
model = pickle.load(open('gbr.pkl','rb'))
def main():
    img1 = Image.open('v1(1).jpg')
    img1 = img1.resize((600,350))
    st.image(img1,use_column_width=False)
    st.title("Pizza Price Prediction")
if __name__=='__main__':
    main()

company =  st.selectbox('extra_sauce',['A','B'])

 ## Diameter of Pizza
diameter = st.text_input('Diameter of Pizza')

## Topping
topping =  st.selectbox('topping',['chiken','peporoni','beef'])

 ## Varient
variant =  st.selectbox('variant',['spicey','Yes'])

## size
size = st.selectbox('size',['small','Yes'])

# Touchscreen
extra_sauce = st.selectbox('extra_sauce',['No','Yes'])

# IPS
extra_cheese = st.selectbox('extra_cheese',['No','Yes'])


# IPS
extra_mushrooms = st.selectbox('extra_mushrooms',['No','Yes'])

if st.button('Predict Price'):
    if company == 'A':
        company = 1
    elif company =='B':
        company = 2
    else:
        company = 3


   
    if topping == 'chiken':
        topping = 1
    elif topping =='Beef':
        topping = 2
    else:
        topping = 3
    if variant == 'spicey':
        variant = 1
    
    else:
        variant = 2
    
    if size == 'small':
        size = 1
    elif size =='medium':
        size = 2
    else:
        size = 3

    if extra_cheese == 'Yes':
        extra_cheese = 1
    else:
        extra_cheese = 0
    if extra_mushrooms == 'Yes':
        extra_mushrooms = 1
    else:
        extra_mushrooms = 0
    # query
    




    if extra_sauce == 'Yes':
        extra_sauce = 1
    else:
        extra_sauce = 0

    

    prediction=model.predict([[company,diameter,topping,variant,size,extra_sauce,extra_cheese,extra_mushrooms]])
    output=round(prediction[0],2)
    st.success('Predicted price is Rs: {}'.format(output))
