import streamlit as st
from streamlit.elements.arrow import Data
try:
    from pynse import *
    import datetime
    import matplotlib.pyplot as plt
    import mplfinance as mpf
    import plotly.express as px
    import pandas as pd
    from datetime import date
    from plotly import graph_objs as go

except ModuleNotFoundError as e:
    st.error(
        f"Looks like requirements are not installed: '{e}'. Run the following command to install requirements"
    )
    st.code(
        "pip install streamlit matplotlib mplfinance plotly git+https://github.com/StreamAlpha/pynse.git"
    )
else:
    nse = Nse()
    def bhavcopy_display():
        with st.sidebar:
            st.write("Bhavcopy Inputs")
            req_date = st.date_input("Select Date", datetime.date.today())
            segment = st.selectbox("Select Segment", ["Cash", "FnO"])

        req_date = None if req_date >= datetime.date.today() else req_date

        if segment == "Cash":
            bhavcopy = nse.bhavcopy(req_date)
        else:
            bhavcopy = nse.bhavcopy_fno(req_date)

        st.write(f"{segment} bhavcopy for {req_date}")

        st.download_button(
            "Download", bhavcopy.to_csv(), file_name=f"{segment}_bhav_{req_date}.csv"
        )
        st.write(bhavcopy)

                
        
    analysis_dict = {
        "Bhavcopy": bhavcopy_display,        
    }
    with st.sidebar:
            st.markdown(
            'App Created For F.I.R.E.'
            )
            st.write("---")            
            selected_analysis = st.radio("Select Analysis", list(analysis_dict.keys()))
            
            st.write("---")
    st.header(selected_analysis)
    analysis_dict[selected_analysis]()

#Run these 2 commands in 2 terminals
#streamlit run main.py & 
#npx localtunnel --port 8501