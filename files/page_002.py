
import streamlit as st
import numpy as np
from scipy.stats import binom
import math

def sampleNumber(f,Rtest,CL):
    res_aux_left = 1-CL
    n = 1
    res_aux_right = binom.cdf(f,n,1-Rtest)
    while res_aux_right >= res_aux_left:
        n +=1
        res_aux_right = binom.cdf(f,n,1-Rtest)
    return n

st.header("Determining Units for Available Test Time (MTTF)")
st.markdown("In this scenario, the Mean Time To Failure (MTTF) is available.")

with st.form("form_pag2"):
    
    holder_box_container = st.empty()
    
    placeholder_help = st.empty()
    button = st.form_submit_button("Run")
    
    holder_text_container = st.empty()

with placeholder_help:
    holder_help = st.checkbox("Help?",value=False)
    
with holder_box_container.container():
    col1, col2, col3 = st.columns([1,1,1])
    mttf_input = col1.number_input("Mean Time To Failure:",value=75.00,min_value=0.00)
    cl_input = col2.slider("Confidence Level:",min_value=0.00,max_value=1.00,value=0.95)
    failure_input = col3.number_input("Number of Failures:",value=0,min_value=0)
    beta_input = col1.number_input("Enter β value (Weibull Shape):",value=1.5,min_value=0.00)
    time_test = col2.number_input("Enter Test Time:",value=60.00,min_value=0.00)

with holder_text_container.container():
    if holder_help == True:
        st.markdown("**Where:**")
        st.markdown("- *Mean Time To Failure*: Desired Mean Time To Failure for a System")
        st.markdown("- *Desired Confidence Level*: Desired confidence level for desired MTTF")
        st.markdown("- *Number of Failures*: Maximum number of failures accepted during test execution")
        st.markdown("- *β*: Shape parameter of Weibull Distribution")
        st.markdown("- *Test Time*: Duration of equipment testing")

if button:
    eta = mttf_input/(math.gamma(1+1/beta_input))
    Rtest = np.exp(-(time_test/eta)**(beta_input))
    
    sample_number = sampleNumber(failure_input,Rtest,cl_input)
    st.markdown(f"#### Sample Number: {sample_number}")