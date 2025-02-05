
import streamlit as st
from scipy.stats import binom


def sampleNumber(f,Rtest,CL):
    res_aux_left = 1-CL
    n = 1
    res_aux_right = binom.cdf(f,n,1-Rtest)
    while res_aux_right >= res_aux_left:
        n +=1
        res_aux_right = binom.cdf(f,n,1-Rtest)
    return n

st.header("Determining Units under Non-Parametric Binomial")


with st.form("form_pag5"):
    
    holder_box_container = st.empty()
    
    placeholder_help = st.empty()
    button = st.form_submit_button("Run")
    
    holder_text_container = st.empty()

with placeholder_help:
    holder_help = st.checkbox("Help?",value=False)

with holder_box_container.container():
    
    col1, col2, col3 = st.columns([1,1,1])
    reliability_input = col2.slider("Desired Reliability:",min_value=0.00,max_value=1.00,value=0.80)
    cl_input = col3.slider("Confidence Level:",min_value=0.00,max_value=1.00,value=0.90)
    failure_input = col1.number_input("Number of Failures:",value=0,min_value=0)

with holder_text_container.container():
    if holder_help == True:      
        st.markdown("**Where:**")
        st.markdown("- *Number of Failures*: Maximum number of failures accepted during test execution")
        st.markdown("- *Desired Reliability*: Desired reliability level in *mission time*")
        st.markdown("- *Desired Confidence Level*: Desired confidence level for desired reliability in *mission time*")
      
if button:
    sample_number = sampleNumber(failure_input, reliability_input, cl_input)
    st.markdown(f"#### Sample Number: {sample_number}")