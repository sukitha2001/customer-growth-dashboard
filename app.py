import streamlit as st
from streamlit_option_menu import option_menu

from views import overview, advance_analysis, more_plots, experience_analysis, time_analysis

st.set_page_config(page_title="Venue Analytics Dashboard", layout="wide")

selected = option_menu(
    menu_title=None,
    options=["Overview", "Revenue", "Customers", "Experience", "Time Analysis"],
    icons=["house", "currency-dollar", "people", "star", "calendar3", "info-circle"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#000000"},
        "icon": {"color": "orange", "font-size": "18px"},
        "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#151e7c"},
    }
)

if selected == "Overview":
    overview.show()
elif selected == "Revenue":
    advance_analysis.show()
elif selected == "Customers":
    more_plots.show()
elif selected == "Experience":
    experience_analysis.show()
elif selected == "Time Analysis":
    time_analysis.show()