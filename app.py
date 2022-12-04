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

company =  st.selectbox('company',['DOMINO’S','CHICAGO PIZZA','SMOKIN’ JOE’S PIZZA','BON PIZZA'])

 ## Diameter of Pizza
diameter = st.selectbox('diameter',['8','12','14','18','22'])

## Topping
topping =  st.selectbox('topping',['Chicken','Papproni','mushrooms','Smoked_beef','Mozzarella','BlackPapper','Tuna','Meat','Sausage','Onion','Vegitable'])

 ## Varient
variant =  st.selectbox('variant',['Double Signature','American Favorite','Super Supreme','Meat lovers','Double mix','Classic','Crunchy','NewYork','Double Decker','Spicy Tuna','BBQ Meat fiesta','BBQ Faufage','Extra vaganza'])

## size
size = st.selectbox('size',['jumbo','Regular','Medium','Small','Large','xl'])

# Touchscreen
extra_sauce = st.selectbox('extra_sauce',['No','Yes'])

# IPS
extra_cheese = st.selectbox('extra_cheese',['No','Yes'])


# IPS
extra_mushrooms = st.selectbox('extra_mushrooms',['No','Yes'])

if st.button('Predict Price'):
    if company == 'DOMINO’S':
        company = 0
    elif company =='CHICAGO PIZZA':
        company = 1
    elif company =='SMOKIN’ JOE’S PIZZA':
         company = 2
    else:
        company =3


   
    if topping == 'BlackPapper':
        topping = 1
    elif topping =='Chicken':
        topping = 2
    elif topping =='Meat':
        topping = 3
    elif topping =='Mozzarella':
        topping = 4
    elif topping =='mushrooms':
         topping = 5
    elif topping =='Onion':
        topping = 6
    elif topping =='Papproni':
        topping = 7
    elif topping =='Sausage':
        topping = 8
    elif topping =='Smoked_beef':
        topping = 9
    elif topping =='Tuna':
        topping = 10

    else:
        topping = 11

    if variant == 'Double Signature':
        variant = 8
    elif variant =='American Favorite':
        variant = 3
    elif variant =='Super Supreme':
        variant = 18
    elif variant =='Meat lovers':
        variant = 13
    elif variant =='Double mix':
        variant = 7
    elif variant =='Classic':
        variant = 4
    elif variant =='Crunchy':
        variant = 5
    elif variant =='NewYork':
        variant= 15
    elif variant =='Double Decker':
        variant = 6
    elif variant =='Spicy Tuna':
        variant = 17
    elif variant =='BBQ Meat fiesta':
        variant = 0
    elif variant =='BBQ Faufage':
        variant = 1
    else:
        variant = 2
    
    if size == 'small':
        size = 5
    elif size =='medium':
        size = 3
    elif size =='jumbo':
        size = 1
    elif size =='Regular':
        size = 4
    elif size =='Large':
        size = 2
    else:
        size = 6

    if extra_cheese == 'Yes':
        extra_cheese = 1
    else:
        extra_cheese = 0
    if extra_mushrooms == 'Yes':
        extra_mushrooms = 1
    else:
        extra_mushrooms = 0
    
    




    if extra_sauce == 'Yes':
        extra_sauce = 1
    else:
        extra_sauce = 0

    

    prediction=model.predict([[company,diameter,topping,variant,size,extra_sauce,extra_cheese,extra_mushrooms]])
    output=round(prediction[0],2)
    st.success('Predicted price is Rs: {}'.format(output))