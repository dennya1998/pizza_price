import streamlit as st
from PIL import Image


import pickle 

#import joblib
#model = pickle.load(open('modelForPrediction.sav', 'rb'))
#Load the model from the file

#model = joblib.load('pizza_price_predictx.pkl','rb')
model = pickle.load(open('gbr.pkl','rb'))

def main():
    img1 = Image.open('v1(1).jpg')
    img1 = img1.resize((600,350))
    st.image(img1,use_column_width=False)
    st.title("Pizza Price Prediction")
## Account No
    Companey_Name = st.text_input('Companey Name')

 ## Diameter of Pizza
    Diameter_of_Pizza = st.text_input('Diameter of Pizza')

## Topping
    Topping = st.text_input('Topping')

 ## Varient
    Varient = st.text_input('Varient')

## size
    size = st.text_input('size')
    Extra_Sauce= st.text_input('Extra_Sauce')
    Extra_Cheese= st.text_input('Extra_Cheese')
    Extra_mushrooms= st.text_input('Extra_mushrooms')



    # Extra_Sauce_display = ('1','0')
    # Extra_Sauce_options = list(range(len(Extra_Sauce_display)))
    # Extra_Sauce = st.selectbox("Extra Sauce Yes(1),No(0)", Extra_Sauce_options, format_func=lambda x: Extra_Sauce_display[x])

    # Extra_Cheese_display = ('1','0')
    # Extra_Cheese_options = list(range(len(Extra_Cheese_display)))
    # Extra_Cheese = st.selectbox("Extra Cheese Yes(1),No(0)", Extra_Cheese_options, format_func=lambda x: Extra_Cheese_display[x])

    # Extra_mushrooms_display = ('1','0')
    # Extra_mushrooms_options = list(range(len(Extra_mushrooms_display)))
    # Extra_mushrooms = st.selectbox("Extra mushrooms Yes(1),No(0)", Extra_mushrooms_options, format_func=lambda x: Extra_mushrooms_display[x])
    if st.button("Predict"):
        #df = [[Companey_Name, Diameter_of_Pizza, Topping,Varient,size,Extra_Sauce,Extra_Cheese,Extra_mushrooms]]
        
        prediction=model.predict([[Companey_Name, Diameter_of_Pizza, Topping,Varient,size,Extra_Sauce,Extra_Cheese,Extra_mushrooms]])
        output=round(prediction[0],2)
        st.success('Predicted price is: {}'.format(output))

if __name__=='__main__':
    main()

        
        