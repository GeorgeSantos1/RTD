
import streamlit as st
import numpy as np
from scipy.stats import binom
import math


np.seterr(all='ignore')
# 
def ft(t,f,n,beta,eta,CL):
    result = binom.cdf(f,n,1-np.exp(-(t/eta)**(beta))) - (1-CL)
    return result

def d_ft(t,f,n,beta,eta,CL):
    h= 1e-5
    result = (ft(t+h,f,n,beta,eta,CL)-ft(t-h,f,n,beta,eta,CL))/(2*h)
    return result

def fibo(n):
    result = [0,1]
    for i in range(len(result)-1,n):
        result.append(result[i] + result[i-1])
    return result[-1]

# Newton-Rapson
def timeAvaUnits(f,n,beta,eta,CL,absolute=1e-5,t=10):
    t = t
    error  = 1e4
    while error > absolute:
        t_plus = t - ft(t,f=f,n=n,beta=beta,eta=eta,CL=CL)/d_ft(t,f=f,n=n,beta=beta,eta=eta,CL=CL)
        error = abs(t_plus - t)
        t = t_plus
    return t

def timeAvaUnitsOP(f,n,beta,eta,CL,absolute=1e-5):
    t = 1
    i = 1
    while isinstance(t, float) == False:
        t = timeAvaUnits(f=f,n=n,beta=beta,eta=eta,CL=CL,absolute=1e-4,t=t)
        if math.isnan(t) or math.isinf(t):
            i = i+1
            t = fibo(i)
    return t

st.header("Determining Time for Available Units (MTTF)")
st.markdown("In this scenario, the Mean Time To Failure (MTTF) is available.")

with st.form("form_pag4"):
    
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
    sample_size = col2.number_input("Sample Size:",value=5,min_value=0)

with holder_text_container.container():
    if holder_help == True:
        st.markdown("**Where:**")
        st.markdown("- *Mean Time To Failure*: Desired Mean Time To Failure for a System")
        st.markdown("- *Desired Confidence Level*: Desired confidence level for desired MTTF")
        st.markdown("- *Number of Failures*: Maximum number of failures accepted during test execution")
        st.markdown("- *β*: Shape parameter of Weibull Distribution")
        st.markdown("- *Test Time*: Duration of equipment testing")
        st.markdown("- *Sample Size*: Number of tested equipment units")

if button:
    eta = mttf_input/(math.gamma(1+1/beta_input))
    
    time = math.ceil(timeAvaUnitsOP(f=failure_input,n=sample_size,beta=beta_input,eta=eta,CL=cl_input,absolute=1e-4))
    st.write(f"""#### Time for Avaliable Units: {time}""")