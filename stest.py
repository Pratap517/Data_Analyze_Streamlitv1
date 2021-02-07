# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:46:24 2021

@author: pratap
"""



import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
import sweetviz as sv
import streamlit.components.v1 as stc
from streamlit_pandas_profiling import st_profile_report
import seaborn as sns
import warnings
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
warnings.filterwarnings("ignore")

#setting page name

PAGE_CONFIG = {'page_title' : 'Data_Analysis_Prathap','layout':'wide'}
st.set_page_config(**PAGE_CONFIG)

st.set_option('deprecation.showPyplotGlobalUse', False)




def main():
    
    menu=['Home', "Detailed Report", 'Simple Analysis','Graphs','About']
    
    #st.title("Simple EDA APP with Streamlit")
    
    st.sidebar.write("click on above X to hide the menu")
    
    st.sidebar.subheader("Menu")
    choice= st.sidebar.radio("",menu)
    
    st.sidebar.markdown(' Created by  **_Prathap_**. :sunglasses:')
    
    
    if choice=="Detailed Report":
        
        st.markdown("""
                    <style>
                   body {
                         color: #034F84;
                  background-color: #F3F3F3;
                               }
                          </style>
                  """, unsafe_allow_html=True)
        
        st.subheader("Get Full Report Here ")
        
        data_file = st.file_uploader("Upload CSV File",type='CSV')
        
        if data_file is not None:
            df=pd.read_csv(data_file)
            st.subheader(" Head of Youre Dataset")
            st.write(df.head())
            profile=ProfileReport(df)
            if st.button(" Click Here To Generate The Detailed Report"):
                st.write("Please wait, it may take few minitues if dataset is large")
                st_profile_report(profile)
                
                
            
            
      
    elif choice=='Simple Analysis':
        
        st.markdown("""
                  <style>
                   body {
                     color: #034F84;
                     background-color: #F3F3F3;
                               }
                          </style>
                  """, unsafe_allow_html=True)
                  
        st.subheader('Know youre Dataset here')
         
        dfile = st.file_uploader("Upload CSV File",type='CSV')
        
        if dfile is not None:
            df=pd.read_csv(dfile)
            st.subheader(" Head of Youre Dataset")
            st.write(df.head())
            if st.checkbox("Check box to Explore More about youre dataset"):
                
                if st.button('Shape of ur Data'):
                   st.write(df.shape)
                
                if st.button(" Total Columns"):
                   st.write(df.columns)
                if st.button(" Total Missing Values"):
                   st.write(df.isnull().sum())
                if st.button(" Data_types"):
                   st.write(df.dtypes)
                if st.button(" Check the Summary"):
                   st.write(df.describe().T)
                
            
            
            
        
            
       
            
            
        
            
            
            
            
            
            
               
    elif   choice=="Graphs":
        st.subheader('Plot Graphs')
        
        st.markdown("""
                    <style>
                   body {
                         color: #034F84;
                  background-color: #F3F3F3;
                               }
                          </style>
                  """, unsafe_allow_html=True)
        
        
    
        file = st.file_uploader("Upload CSV File",type='csv')
        
        if file is not None:
            
            df=pd.read_csv(file)
            st.subheader(" Head of Youre Dataset")
            st.write(df.head())
            if st.button(' Click Here to Generate Pair Plot'):
               st.write("Please wait, it may take few minitues if dataset is large")
               graph=sns.pairplot(df)
               sns.set(rc={'figure.figsize':(11.7,8.27)})
               st.pyplot(graph)
               st.info("Pair Plots are a really simple way to visualize relationships between each variable. It produces a matrix of relationships between each variable in your data for an instant examination of our data")
              
    elif choice=='About':
        
        st.markdown("""
                  <style>
                   body {
                     color: #034F84;
                     background-color: #F3F3F3;
                               }
                          </style>
                  """, unsafe_allow_html=True)
        st.subheader('A little bit about me!')
        st.write("Hello. Prathap Here, a Motivated Data scientist with 3+ years of experience as a Data Analyst. Passionate about building models that fix problems. Relevant skills include machine learning, problem solving, programming, and creative thinking.")
        st.write("Connect me through @ [LinkedIn](https://www.linkedin.com/in/pratap-reddy-2794b91b7/)")
        st.write("Check out The code @ [Github](https://github.com/Pratap517)")
        st.subheader("check out my other tiny projects below ")
        st.write(" Handy tool to Analyze Csv Files [Click Here](https://share.streamlit.io/pratap517/streamlitapp_dataanalysis/main/main_app.py)")
        st.write(" Simple loan Prediction App [Click Here](https://share.streamlit.io/pratap517/ml_deploy_using_streamlit/main/app.py)")
        st.write(" Live Mask Detection App [Click Here](https://mask-detection-5a800.firebaseapp.com/)")
        st.markdown(' Thanks,  **_Prathap_**. :balloon:')
        
   
    else:
        
        #stc.html("<p style = 'color: red;'>This is An Awesome App</p>")
        
        
        html_temp = """
		<div style="background-color:#D4E4F7;padding:10px;border-radius:10px">
		<h1 style="color:black;text-align:center;">Data Visualization with Streamlit Components</h1>
		</div>
		"""
        stc.html(html_temp)
        st.markdown("""
                  <style>
                   body {
                     color: #034F84;
                     background-color: #F3F3F3;
                               }
                          </style>
                  """, unsafe_allow_html=True)
                  
        st.subheader("Please Select the type of report in Menu")
        
        stc.html("""
			<style>
			* {box-sizing: border-box}
			body {font-family: Verdana, sans-serif; margin:0}
			.mySlides {display: none}
			img {vertical-align: middle;}
			/* Slideshow container */
			.slideshow-container {
			  max-width: 1000px;
			  position: relative;
			  margin: auto;
			}
			/* Next & previous buttons */
			.prev, .next {
			  cursor: pointer;
			  position: absolute;
			  top: 50%;
			  width: auto;
			  padding: 16px;
			  margin-top: -22px;
			  color: white;
			  font-weight: bold;
			  font-size: 18px;
			  transition: 0.6s ease;
			  border-radius: 0 3px 3px 0;
			  user-select: none;
			}
			/* Position the "next button" to the right */
			.next {
			  right: 0;
			  border-radius: 3px 0 0 3px;
			}
			/* On hover, add a black background color with a little bit see-through */
			.prev:hover, .next:hover {
			  background-color: rgba(0,0,0,0.8);
			}
			/* Caption text */
			.text {
			  color: #f2f2f2;
			  font-size: 15px;
			  padding: 8px 12px;
			  position: absolute;
			  bottom: 8px;
			  width: 100%;
			  text-align: center;
			}
			/* Number text (1/3 etc) */
			.numbertext {
			  color: #f2f2f2;
			  font-size: 12px;
			  padding: 8px 12px;
			  position: absolute;
			  top: 0;
			}
			/* The dots/bullets/indicators */
			.dot {
			  cursor: pointer;
			  height: 15px;
			  width: 15px;
			  margin: 0 2px;
			  background-color: #bbb;
			  border-radius: 50%;
			  display: inline-block;
			  transition: background-color 0.6s ease;
			}
			.active, .dot:hover {
			  background-color: #717171;
			}
			/* Fading animation */
			.fade {
			  -webkit-animation-name: fade;
			  -webkit-animation-duration: 1.5s;
			  animation-name: fade;
			  animation-duration: 1.5s;
			}
			@-webkit-keyframes fade {
			  from {opacity: .4} 
			  to {opacity: 1}
			}
			@keyframes fade {
			  from {opacity: .4} 
			  to {opacity: 1}
			}
			/* On smaller screens, decrease text size */
			@media only screen and (max-width: 300px) {
			  .prev, .next,.text {font-size: 11px}
			}
			</style>
			</head>
			<body>
			<div class="slideshow-container">
			<div class="mySlides fade">
			  <div class="numbertext">1 / 3</div>
			  <img src="https://www.w3schools.com/howto/img_nature_wide.jpg" style="width:100%">
			  <div class="text">Caption Text</div>
			</div>
			<div class="mySlides fade">
			  <div class="numbertext">2 / 3</div>
			  <img src="https://www.w3schools.com/howto/img_snow_wide.jpg" style="width:100%">
			  <div class="text">Caption Two</div>
			</div>
			<div class="mySlides fade">
			  <div class="numbertext">3 / 3</div>
			  <img src="https://www.w3schools.com/howto/img_mountains_wide.jpg" style="width:100%">
			  <div class="text">Caption Three</div>
			</div>
			<a class="prev" onclick="plusSlides(-1)">&#10094;</a>
			<a class="next" onclick="plusSlides(1)">&#10095;</a>
			</div>
			<br>
			<div style="text-align:center">
			  <span class="dot" onclick="currentSlide(1)"></span> 
			  <span class="dot" onclick="currentSlide(2)"></span> 
			  <span class="dot" onclick="currentSlide(3)"></span> 
			</div>
			<script>
			var slideIndex = 1;
			showSlides(slideIndex);
			function plusSlides(n) {
			  showSlides(slideIndex += n);
			}
			function currentSlide(n) {
			  showSlides(slideIndex = n);
			}
			function showSlides(n) {
			  var i;
			  var slides = document.getElementsByClassName("mySlides");
			  var dots = document.getElementsByClassName("dot");
			  if (n > slides.length) {slideIndex = 1}    
			  if (n < 1) {slideIndex = slides.length}
			  for (i = 0; i < slides.length; i++) {
			      slides[i].style.display = "none";  
			  }
			  for (i = 0; i < dots.length; i++) {
			      dots[i].className = dots[i].className.replace(" active", "");
			  }
			  slides[slideIndex-1].style.display = "block";  
			  dots[slideIndex-1].className += " active";
			}
			</script>
			""")
    
if __name__=="__main__":
    main()