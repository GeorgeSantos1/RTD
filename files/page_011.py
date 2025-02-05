
import streamlit as st
import numpy as np
from scipy.stats import binom
import math


np.seterr(all='ignore')
# 
def fEta(t,f,n,beta,eta,CL):
    # eta = td/(-np.log(R))**(1/beta)
    result = binom.cdf(f,n,1-np.exp(-(t/eta)**(beta))) - (1-CL)
    return result

def d_fEta(t,f,n,beta,eta,CL):
    h= 1e-5
    result = (fEta(t,f,n,beta,eta+h,CL)-fEta(t,f,n,beta,eta-h,CL))/(2*h)
    return result

def etaAvaUnits(t,f,n,beta,CL,absolute=1e-5,eta=300):
    eta = eta
    error  = 1e4
    while error > absolute:
        eta_plus = eta - fEta(eta=eta,t=t,f=f,n=n,beta=beta,CL=CL)/d_fEta(eta=eta,t=t,f=f,n=n,beta=beta,CL=CL)
        error = abs(eta_plus - eta)
        eta = eta_plus
    return eta

def fibo(n):
    result = [0,1]
    for i in range(len(result)-1,n):
        result.append(result[i] + result[i-1])
    return result[-1]

def etaAvaUnitsOP(t,f,n,beta,CL,absolute=1e-5):
    eta = 1
    i = 1
    while isinstance(eta, float) == False:
        eta = etaAvaUnits(f=f,n=n,beta=beta,eta=eta,CL=CL,absolute=1e-5,t=t)
        if math.isnan(eta) or math.isinf(eta):
            i = i+1
            eta = fibo(i)
    return eta

st.header("Determining Reliability for Units")

with st.form("form_pag11"):
    
    holder_box_container = st.empty()
    
    placeholder_help = st.empty()
    button = st.form_submit_button("Run")
    
    holder_text_container = st.empty()

with placeholder_help:
    holder_help = st.checkbox("Help?",value=False)
    
with holder_box_container.container():
    col1, col2, col3 = st.columns([1,1,1])
    cl_input = col1.slider("Enter Desired Confidence Level:",min_value=0.00,max_value=1.00,value=0.95)
    time_miss = col2.number_input("Enter Desired Mission Time",value=100.00,min_value=0.00)
    time_test = col3.number_input("Enter Test Time:",value=48.00,min_value=0.00)
    sample_size = col1.number_input("Sample Size:",value=86,min_value=0)
    failure_input = col2.number_input("Enter Number of Failures:",value=0,min_value=0)
    beta_input = col3.number_input("Enter β value (Weibull Shape):",value=1.5,min_value=0.00)

with holder_text_container.container():
    if holder_help == True:
        st.markdown("**Where:**")
        st.markdown("- *Desired Confidence Level*: Desired confidence level for estimated reliability in *mission time*")
        st.markdown("- *Desired Mission Time*: Desired mission time for equipment under study")
        st.markdown("- *Test Time*: Duration of equipment testing")
        st.markdown("- *Sample Size*: Number of tested equipment units")
        st.markdown("- *Number of Failures*: Maximum number of failures accepted during test execution")
        st.markdown("- *β*: Shape parameter of Weibull Distribution")

if button:
    eta = etaAvaUnitsOP(t=time_test,f=failure_input,n=sample_size,beta=beta_input,CL=cl_input)
    reliability = np.exp(-(time_miss/eta)**(beta_input))
    reliability = round(reliability*100,2)
    # time = math.ceil(timeAvaUnitsOP(f=failure_input,n=sample_size,beta=beta_input,eta=eta,CL=cl_input,absolute=1e-4))
    st.markdown(f"#### Reliability: {reliability}%")