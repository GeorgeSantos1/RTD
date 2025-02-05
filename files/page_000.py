
import streamlit as st
import sys
from streamlit.web import cli as stcli

st.markdown("""
## Reliability Demonstration Tests  

Manufacturers are often required to prove that a product achieves a specified reliability level within a given time frame and confidence level.
To support engineers in this verification process, several statistical methods can be applied, including the Cumulative Binomial, Non-Parametric Binomial, Exponential Chi-Squared, and Non-Parametric Bayesian approaches.  

-  **Parametric Binomial**: This approach is useful when the test period differs from the reliability target time, as it assumes an underlying probability distribution.  
-  **Non-Parametric Binomial**: Suitable for cases where no distribution assumption is needed, particularly for single-use items.
-  **Exponential Chi-Squared**: Designed specifically for scenarios where failure times follow an exponential distribution.
-  **Non-Parametric Bayesian**: Integrates Bayesian principles with the conventional non-parametric binomial approach.
            
""")