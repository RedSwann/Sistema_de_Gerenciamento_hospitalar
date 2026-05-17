import streamlit as st
from service.fila_service import FilaService
from core.fila_atendimento import FilaAtendimento
from core.paciente import ListaPacientes
from core.pilha_acoes import Pilha


def ui_fila():

    if st.button("⬅ Voltar ao Menu"):
        st.session_state.pagina = "menu"
        st.rerun()

    # ================= INSTÂNCIAS =================
    if "lista" not in st.session_state:
        st.session_state.lista = ListaPacientes()

    if "fila" not in st.session_state:
        st.session_state.fila = FilaAtendimento()

    if "pilha" not in st.session_state:
        st.session_state.pilha = Pilha()

    if "fila_service" not in st.session_state:
        st.session_state.fila_service = FilaService(
            st.session_state.lista,
            st.session_state.fila,
            st.session_state.pilha
        )

    service = st.session_state.fila_service
    fila = st.session_state.fila

    st.title("Fila de Atendimento")

    # ================= ADICIONAR PACIENTE =================
    with st.form("fila_form"):

        cpf = st.text_input("CPF do Paciente")

        nivel = st.selectbox(
            "Nível de Emergência",
            ["Vermelho", "Laranja", "Amarelo", "Verde"]
        )

        enviar = st.form_submit_button("Adicionar")

        if enviar:
            ok, msg = service.adicionar(cpf, nivel)

            if ok:
                st.success(msg)
            else:
                st.error(msg)

            st.rerun()

    # ================= BOTÕES DE CONTROLE =================
    col1, col2 = st.columns(2)

    if col1.button("Atualizar fila", use_container_width=True):
        fila.atualizar_fila()
        st.rerun()

    if col2.button("Atender próximo", use_container_width=True):
        ok, msg = service.atender()

        if ok:
            st.success(msg)
        else:
            st.warning(msg)

        st.rerun()

    if st.button("Desfazer última ação", use_container_width=True):

        ok, msg = service.desfazer()

        if ok:
            st.success(msg)
        else:
            st.warning(msg)

        st.rerun()

    # ================= FILA ATUAL =================
    st.divider()
    st.subheader("Fila Atual")

    atual = fila.inicio

    if not atual:
        st.info("Fila vazia.")
    else:
        i = 1
        while atual:
            st.write(
                f"{i}. {atual.paciente.nome} | "
                f"CPF: {atual.paciente.cpf} | "
                f"Nível: {atual.nivel}"
            )
            atual = atual.proximo
            i += 1