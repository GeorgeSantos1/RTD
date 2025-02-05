
import streamlit as st
import numpy as np
from scipy.stats import chi2
import math


def accTime(MTTF,f,CL):
    result  = (MTTF*chi2.ppf(1-(1-CL),2*f+2))/2
    return result

st.header("Determining necessary accumulated test time for a demonstrated reliability")

with st.form("form_pag7"):
    
    holder_box_container = st.empty()
    
    placeholder_help = st.empty()
    button = st.form_submit_button("Run")
    
    holder_text_container = st.empty()

with placeholder_help:
    holder_help = st.checkbox("Help?",value=False)

with holder_box_container.container():
    
    col1, col2, col3 = st.columns([1,1,1])
    reliability = col1.slider("Desired Reliability:",min_value=0.00,max_value=1.00,value=0.85)
    cl_input = col2.slider("Confidence Level:",min_value=0.00,max_value=1.00,value=0.90)
    time_miss = col3.number_input("Mission Time",value=500.00,min_value=0.00)
    failure_input = col1.number_input("Number of Failures:",value=2,min_value=0)

with holder_text_container.container():
    if holder_help == True:      
        st.markdown("**Where:**")
        st.markdown("- *Desired Reliability*: Desired reliability level in *mission time*")
        st.markdown("- *Desired Confidence Level*: Desired confidence level for desired reliability in *mission time*")
        st.markdown("- *Desired Mission Time*: Desired mission time for equipment under study")
        st.markdown("- *Number of Failures*: Maximum number of failures accepted during test execution")
      
if button:
    MTTF = time_miss/-np.log(reliability)
    acctime = math.ceil(accTime(MTTF,failure_input,cl_input))
    st.markdown(f"#### Accumulated Time: {acctime}")