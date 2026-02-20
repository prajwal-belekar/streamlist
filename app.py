import streamlit as st
import pandas as pd   
import numpy as np

#Displaying text content
st.title("My First Streamlit App") 
st.write("Hello, welcome to my first Streamlit app!")
st.text("This is a simple example to demonstrate how to use Streamlit for building interactive web applications.")   

 #Creating charts using pandas & numpy 
df=pd.DataFrame(np.random.randn(100,2),columns=['x','y'])
st.line_chart(df)
st.bar_chart(df)

#sidebar , image , videos
st.sidebar.title("Navigation")
st.image("C:\\Users\\hp\\OneDrive\\Pictures\\Saved Pictures\\dark.jpg", width=600)
st.video(r"D:\new wallpaper - Made with Clipchamp.mp4")

#file uploader
upload_file=st.file_uploader("Upload a CSV file", type=["csv"])
if upload_file:
    df=pd.read_csv(upload_file)
    st.dataframe(df)

#taking user input 
name=st.text_input("Enter your name")
if st.button("Greet"):
    st.write(f"Hello, {name}! Welcome to Streamlit.")    


#text &markdown formating 
st.header("this is a header")
st.subheader("this is a sub header")
st.markdown("**bold text**, *italic text*, 'code' , [link](https://www.streamlit.io/)")
st.code("print('Hello, Streamlit!')", language="python")

name1 = st.text_input("Enter your name", key="name_input_1")
st.text_area("Enter your message")
st.number_input("Enter a number " , min_value=0, max_value=100, step=1)
st.slider("Choose a range", 0,100)
st.selectbox("Choose an Anime", ["One Piece", "Bleach", "Naruto"])
st.multiselect("Select yout favourite protagonist", ["Luffy", "Ichigo", "Naruto"])
st.radio("Choose your favourite song", ["Kompa Parano", "Blue Bird", "Luz Roja"])
st.checkbox("I agree to the terms and conditions")

#matplotlib integration
import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [10,20,25,30])
st.pyplot(plt)
