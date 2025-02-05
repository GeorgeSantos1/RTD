
import streamlit as st
from scipy.stats import beta
import math

def a0b0(a,b,c):
    e_r0 = (a+4*b+c)/6
    var_r0 = ((c-a)/6)**2

    a0 = e_r0*((e_r0-e_r0**2)/var_r0 -1)         # parameter alpha of beta distribution
    b0 = (1-e_r0)*((e_r0-e_r0**2)/var_r0 -1)

    return [a0,b0]

def fnbeta(R,r,a0,b0,CL,n):
    result = 1-beta.cdf(R,a0+n-r,b0+r)-CL
    return result

def d_fnbeta(R,r,a0,b0,CL,n):
    h= 1e-5
    result = (fnbeta(R,r,a0,b0,CL,n+h)-fnbeta(R,r,a0,b0,CL,n-h))/(2*h)
    return result

def sampleSize(R,r,a0,b0,CL,absolute=1e-5,n=20):
    n = n
    error  = 1e4
    while error > absolute:
        n_plus = n - fnbeta(R,r,a0,b0,CL,n)/d_fnbeta(R,r,a0,b0,CL,n)
        error = abs(n_plus - n)
        n = n_plus
    return n

def fibo(n):
    result = [0,1]
    for i in range(len(result)-1,n):
        result.append(result[i] + result[i-1])
    return result[-1]

def sampleSizeOP(R,r,a0,b0,CL,absolute=1e-5):
    n = 1
    i = 1
    while isinstance(n, float) == False:
        n = sampleSize(R,r,a0,b0,CL,absolute=1e-5,n=n)
        if math.isnan(n) or math.isinf(n):
            i = i+1
            n = fibo(i)
    return n


st.header("Determining Sample Size for design test:")
st.markdown("A non-parametric Bayesian method can be used to design a test using prior knowledge about the system's reliability.")

with st.form("form_pag10"):
    
    holder_box_container = st.empty()
    
    placeholder_help = st.empty()
    button = st.form_submit_button("Run")
    
    holder_text_container = st.empty()

with placeholder_help:
    holder_help = st.checkbox("Help?",value=False)

with holder_box_container.container():
    
    col1, col2, col3 = st.columns([1,1,1])
    lowest_r = col1.slider("Lowest possible reliability:",min_value=0.00,max_value=1.00,value=0.80)
    most_r = col2.slider("Most likely reliability:",min_value=0.00,max_value=1.00,value=0.85)
    highest_r = col3.slider("Highest possible reliability:",min_value=0.00,max_value=1.00,value=0.97)
    reliability_input = col1.slider("Desired Reliability:",min_value=0.00,max_value=1.00,value=0.90)
    cl_input = col2.slider("Confidence Level:",min_value=0.00,max_value=1.00,value=0.80)
    failure_input = col3.number_input("Number of Failures:",value=1,min_value=0)

with holder_text_container.container():
    if holder_help == True:      
        st.markdown("**Where:**")
        st.markdown("- *Lowest Possible Reliability*: Minimum reliability for the system based on prior knowledge (expert opinion).")
        st.markdown("- *Most Likely Reliability*: The reliability value most likely for the system based on prior knowledge (expert opinion).")
        st.markdown("- *Highest Possible Reliability*: Highest Possible Reliability: Maximum reliability for the system based on prior knowledge (expert opinion).")
        st.markdown("- *Desired Reliability*: Desired posterior reliability for the system being tested.")
        st.markdown("- *Desired Confidence Level*: Confidence level desired for the posterior reliability")
        st.markdown("- *Number of Failures*: Maximum number of failures accepted during test execution")
        
if button:
    a0 = a0b0(lowest_r,most_r,highest_r)[0]
    b0 = a0b0(lowest_r,most_r,highest_r)[1]
    
    sample = sampleSizeOP(reliability_input,failure_input,a0,b0,cl_input,absolute=1e-5)
    sample = math.ceil(sample)
    
    st.markdown(f"#### Sample Size: {sample}")