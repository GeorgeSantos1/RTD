
import streamlit as st
import numpy as np
from scipy.stats import binom
import math


def frNPB(R,f,n,CL):
    result = binom.cdf(f,n,1-R) - (1-CL)
    return result

def d_frNPB(R,f,n,CL):
    h= 1e-5
    result = (frNPB(R+h,f,n,CL)-frNPB(R-h,f,n,CL))/(2*h)
    return result

# t = t
# t = t - fx(t,f=f,n=n,beta=beta,eta=eta,CL=CL)/d_fx(t,f=f,n=n,beta=beta,eta=eta,CL=CL)

# Newton-Rapson
def desired_rNPB(f,n,CL,absolute=1e-5,r=0.9):
    R = r
    error  = 1e4
    while error > absolute:
        R_plus = R - frNPB(R,f=f,n=n,CL=CL)/d_frNPB(R,f=f,n=n,CL=CL)
        error = abs(R_plus - R)
        R = R_plus
    return R

def desired_rNPBOP(f,n,CL,absolute=1e-5):
    R = 1
    i = 0
    iv = np.arange(0.0, 1.0, 0.001)
    while isinstance(R, float) == False:
        R = iv[i]
        R = desired_rNPB(f,n,CL,absolute=1e-5,r=R)
        if math.isnan(R) or math.isinf(R):
            R = 1
            i = i +1
    return R

st.header("Determining Reliability under Non-Parametric Binomial")

with st.form("form_pag5"):
    
    holder_box_container = st.empty()
    
    placeholder_help = st.empty()
    button = st.form_submit_button("Run")
    
    holder_text_container = st.empty()

with placeholder_help:
    holder_help = st.checkbox("Help?",value=False)

with holder_box_container.container():
    
    col1, col2, col3 = st.columns([1,1,1])
    sample_size = col2.number_input("Sample Size:",value=11,min_value=0)
    cl_input = col3.slider("Confidence Level:",min_value=0.00,max_value=1.00,value=0.90)
    failure_input = col1.number_input("Number of Failures:",value=0,min_value=0)

with holder_text_container.container():
    if holder_help == True:      
        st.markdown("**Where:**")
        st.markdown("- *Number of Failures*: Maximum number of failures accepted during test execution")
        st.markdown("- *Sample Size*: Number of tested equipment units")
        st.markdown("- *Desired Confidence Level*: Desired confidence level for desired reliability in *mission time*")
      
if button:
    reliability = desired_rNPBOP(f=failure_input,n=sample_size,CL=cl_input,absolute=1e-5)
    reliability = round(reliability*100,2)
    st.markdown(f"#### Reliability: {reliability}%")