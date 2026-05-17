import streamlit as st
from ui.menu_inicial import ui_menu

st.set_page_config(
    page_title="HealthCore",
    layout="wide"
)

if "pagina" not in st.session_state:
    st.session_state.pagina = "menu"

# chama o menu
ui_menu()