import pandas as pd
import streamlit as st
from core.pilha_acoes import Pilha


def ui_historico():

    if st.button("⬅ Voltar ao Menu"):
        st.session_state.pagina = "menu"
        st.rerun()

    if "historico" not in st.session_state:
        st.session_state.historico = Pilha()

    historico = st.session_state.historico

    st.title("Histórico de Ações")
    st.caption("Exibe as ações mais recentes.")

    dados = historico.listar()

    if not dados:
        st.info("Nenhuma ação registrada ainda.")
        return

    tabela = pd.DataFrame(dados)

    st.write(f"Total de ações salvas: {historico.tamanho()} / 50")
    st.dataframe(
        tabela,
        use_container_width=True,
        hide_index=True
    )
