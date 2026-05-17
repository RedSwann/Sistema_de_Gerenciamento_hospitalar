import streamlit as st
from ui.menu_cadastro import ui_cadastro
from ui.menu_fila import ui_fila


def ui_menu():

    # ================= MENU PRINCIPAL =================
    if st.session_state.pagina == "menu":

        st.title("Sistema de Atendimento - HealthCore")

        col1, col2 = st.columns(2)

        if col1.button("Banco de Pacientes", use_container_width=True):
            st.session_state.pagina = "cadastro"
            st.rerun()

        if col2.button("Fila de Atendimento", use_container_width=True):
            st.session_state.pagina = "fila"
            st.rerun()

    # ================= MENU DE CADASTRO =================
    elif st.session_state.pagina == "cadastro":
        ui_cadastro()

    # ================= MENU DE FILA =================
    elif st.session_state.pagina == "fila":
        ui_fila()