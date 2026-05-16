import streamlit as st

st.set_page_config(page_title="HealthCore", layout="wide")

st.title("Sistema de atendimento - HealthCore")

col1, col2 = st.columns(2)

with col1:
    if st.button("Banco de Pacientes", use_container_width=True):
        st.switch_page("pages/Cadastro.py")

with col2:
    if st.button("Fila de Atendimento", use_container_width=True):
        st.switch_page("pages/Fila.py")
