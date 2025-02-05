# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 13:58:32 2024

@author: george.alves
"""

import streamlit as st

page_000 = st.Page(page="page_000.py",title = "Homepage",icon=":material/home:")
page_001 = st.Page(page="page_001.py",title = "Units for Available Test Time",icon=":material/format_list_numbered:")
page_002 = st.Page(page="page_002.py",title = "Units for Available Test Time (MTTF)",icon=":material/format_list_numbered:")
page_003 = st.Page(page="page_003.py",title = "Determining Time for Available Units",icon=":material/timer:")
page_004 = st.Page(page="page_004.py",title = "Determining Time for Available Units (MTTF)",icon=":material/timer:")
page_005 = st.Page(page="page_005.py",title = "Determining Units",icon=":material/format_list_numbered:")
page_006 = st.Page(page="page_006.py",title = "Determining Reliability", icon=":material/trending_up:")
page_007 = st.Page(page="page_007.py",title = "Accumulated Test Time")
page_008 = st.Page(page="page_008.py",title = "Determining Reliability (Prior Expert Opinion)", icon=":material/trending_up:")
page_009 = st.Page(page="page_009.py",title = "Determining Confidence Level (Prior Expert Opinion)")
page_010 = st.Page(page="page_010.py",title = "Determining Units (Prior Expert Opinion)",icon=":material/format_list_numbered:")
page_011 = st.Page(page="page_011.py",title = "Determining Reliability for Units",icon=":material/trending_up:")
page_012 = st.Page(page="page_012.py",title = "Determining MTTF",icon=":material/trending_up:")


pg = st.navigation({"":[page_000],"Parametric Binomial":[page_001,page_002,page_003,page_004,page_011,page_012],
                    "Non-Parametric Binomial":[page_005,page_006],
                    "Constant Failure Rate/Chi-Squared":[page_007],
                    "Bayesian Non-Parametric":[page_008,page_009,page_010]})

st.set_page_config(page_title="Data manager",layout="wide",initial_sidebar_state="expanded",page_icon=":material/vpn_lock:")
pg.run()
