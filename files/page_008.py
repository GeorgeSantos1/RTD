
import streamlit as st
from scipy.stats import beta


def a0b0(a,b,c):
    e_r0 = (a+4*b+c)/6
    var_r0 = ((c-a)/6)**2

    a0 = e_r0*((e_r0-e_r0**2)/var_r0 -1)         # parameter alpha of beta distribution
    b0 = (1-e_r0)*((e_r0-e_r0**2)/var_r0 -1)

    return [a0,b0]


st.header("Use Prior Expert Opinion on System Reliability")
st.markdown("A non-parametric Bayesian method can be used to design a test using prior knowledge about the system's reliability.")

with st.form("form_pag8"):
    
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
    cl_input = col1.slider("Confidence Level:",min_value=0.00,max_value=1.00,value=0.90)
    sample_size = col2.number_input("Sample Size:",value=20,min_value=0)
    failure_input = col3.number_input("Number of Failures:",value=1,min_value=0)

with holder_text_container.container():
    if holder_help == True:      
        st.markdown("**Where:**")
        st.markdown("- *Lowest Possible Reliability*: Minimum reliability for the system based on prior knowledge (expert opinion).")
        st.markdown("- *Most Likely Reliability*: The reliability value most likely for the system based on prior knowledge (expert opinion).")
        st.markdown("- *Highest Possible Reliability*: Highest Possible Reliability: Maximum reliability for the system based on prior knowledge (expert opinion).")
        st.markdown("- *Desired Confidence Level*: Confidence level desired for the posterior reliability")
        st.markdown("- *Sample Size*: Number of tested equipment units")
        st.markdown("- *Number of Failures*: Maximum number of failures accepted during test execution")
      
if button:
    a0 = a0b0(lowest_r,most_r,highest_r)[0]
    b0 = a0b0(lowest_r,most_r,highest_r)[1]
    a1 = a0 + sample_size - failure_input
    b1 = b0 + failure_input

    R = beta.ppf(1-cl_input,a1,b1)
    R = round(R*100,2)
    st.markdown(f"#### Reliability: {R}%")