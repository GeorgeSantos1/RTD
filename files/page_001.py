
import streamlit as st
import numpy as np
from scipy.stats import binom


def sampleNumber(f,Rtest,CL):
    res_aux_left = 1-CL
    n = 1
    res_aux_right = binom.cdf(f,n,1-Rtest)
    while res_aux_right >= res_aux_left:
        n +=1
        res_aux_right = binom.cdf(f,n,1-Rtest)
    return n

st.header("Determining Units for Available Test Time")


with st.form("form_pag1"):
    
    placeholder_radio = st.empty()
    holder_box_container = st.empty()
    
    placeholder_help = st.empty()
    button = st.form_submit_button("Run")
    
    holder_text_container = st.empty()

with placeholder_radio:
    holder_box = st.checkbox("Desired Reliability Available?",value=True)

with placeholder_help:
    holder_help = st.checkbox("Help?",value=False)

with holder_box_container.container():
    if holder_box == False:
        col1, col2, col3 = st.columns([1,1,1])
        time_input = col1.number_input("Enter Test Time:",value=48.00,min_value=0.00)
        failure_input = col2.number_input("Enter Number of Failures:",value=0,min_value=0)
        eta_input = col3.number_input("Enter $\eta$ value:",value=448.3,min_value=0.00)
        beta_input = col1.number_input("Enter β value:",value=1.5,min_value = 0.00)
        cl_input = col2.slider("Enter Confidence Level:",min_value=0.00,max_value=1.00,value=0.95)
                 
    else:
        col1, col2, col3 = st.columns([1,1,1])
        reliability_input = col1.slider("Enter Desired Reliability:",min_value=0.00,max_value=1.00,value=0.90)
        cl_input = col2.slider("Enter Desired Confidence Level:",min_value=0.00,max_value=1.00,value=0.95)
        time_miss = col3.number_input("Enter Desired Mission Time",value=100.00,min_value=0.00)
        failure_input = col1.number_input("Enter Number of Failures:",value=0,min_value=0)
        time_test = col2.number_input("Enter Test Time:",value=48.00,min_value=0.00)
        beta_input = col3.number_input("Enter β value (Weibull Shape):",value=1.5,min_value=0.00)

with holder_text_container.container():
    if holder_box == True and holder_help == True:      
        st.markdown("**Where:**")
        st.markdown("- *Desired Reliability*: Desired reliability level in *mission time*")
        st.markdown("- *Desired Confidence Level*: Desired confidence level for desired reliability in *mission time*")
        st.markdown("- *Desired Mission Time*: Desired mission time for equipment under study")
        st.markdown("- *Number of Failures*: Maximum number of failures accepted during test execution")
        st.markdown("- *Test Time*: Duration of equipment testing")
        st.markdown("- *β*: Shape parameter of Weibull Distribution")
    
    elif holder_box == False and holder_help == True:
        st.markdown("**Where:**")
        st.markdown("- *Test Time*: Duration of equipment testing")
        st.markdown("- *Number of Failures*: Maximum number of failures accepted during test execution")
        st.markdown("""- *$\eta$*: Scale parameter of Weibull Distribution""")
        st.latex(r'''\eta = \frac{t_{Mission}}{(-ln(R_{Desired}))^\frac{1}{b}}''')
        st.markdown("- *β*: Shape parameter of Weibull Distribution")
        st.markdown("- *Desired Confidence Level*: Desired confidence level for desired reliability in *mission time*")
        
if button:
    if holder_box == False:
        Rtest = np.exp(-(time_input/eta_input)**(beta_input))
        sample_number = sampleNumber(failure_input, Rtest, cl_input)
        st.write(f"""#### Sample Number: {sample_number}""")
        st.write(f"""#### Reliability in test time: {round(Rtest*100,2)}%""")
    else:
        eta =   time_miss/((-np.log(reliability_input))**(1/beta_input))
        Rtest = np.exp(-(time_test/eta)**(beta_input))
        sample_number = sampleNumber(failure_input, Rtest, cl_input)
        Rmiss = np.exp(-(time_miss/eta)**(beta_input))
        st.markdown(f"""#### Sample Number: {sample_number}""")
        st.markdown(f"""#### Reliability in Mission Time: {round(Rmiss*100,2)}%""")
        st.markdown(f"""#### Reliability in Test Time: {round(Rtest*100,2)}%""")