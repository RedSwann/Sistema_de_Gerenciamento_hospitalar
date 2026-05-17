import streamlit as st
from core.paciente import ListaPacientes
from service.paciente_service import PacienteService


def ui_cadastro():

    if st.button("⬅ Voltar ao Menu"):
        st.session_state.pagina = "menu"
        st.rerun()

    # ================= INSTÂNCIAS =================
    if "lista" not in st.session_state:
        st.session_state.lista = ListaPacientes()

    if "paciente_service" not in st.session_state:
        st.session_state.paciente_service = PacienteService(
            st.session_state.lista
        )

    service = st.session_state.paciente_service
    lista = st.session_state.lista

    if "editando" not in st.session_state:
        st.session_state.editando = None

    st.title("Cadastro de Pacientes")

    # ================= CADASTRAR PACIENTE =================
    with st.form("form_cadastro"):

        c1, c2, c3, c4, c5 = st.columns(5)

        nome = c1.text_input("Nome")
        cpf = c2.text_input("CPF")
        idade = c3.text_input("Idade")
        telefone = c4.text_input("Telefone")
        deficiencia = c5.selectbox(
            "Portador de deficiência",
            ["Não", "Sim"]
        )

        salvar = st.form_submit_button("Salvar")

        if salvar:

            ok, msg = service.cadastrar(
                nome,
                cpf,
                idade,
                telefone,
                deficiencia
            )

            if ok:
                st.success(msg)
            else:
                st.error(msg)

            st.rerun()

    # ================= EDITAR PACIENTE =================
    if st.session_state.editando:

        paciente = lista.buscar(st.session_state.editando)

        st.divider()
        st.subheader("Editar Paciente")

        with st.form("editar"):

            nome = st.text_input("Nome", paciente.nome)
            idade = st.number_input("Idade", 0, 120, paciente.idade)
            telefone = st.text_input("Telefone", paciente.telefone)

            deficiencia = st.selectbox(
                "Portador de deficiência",
                ["Não", "Sim"],
                index=0 if paciente.deficiencia == "Não" else 1
            )

            col1, col2 = st.columns(2)

            salvar = col1.form_submit_button("Salvar alterações")
            cancelar = col2.form_submit_button("Cancelar")

            if salvar:

                ok, msg = service.editar(
                    paciente.cpf,
                    nome,
                    idade,
                    telefone,
                    deficiencia
                )

                st.session_state.editando = None

                if ok:
                    st.success(msg)
                else:
                    st.error(msg)

                st.rerun()

            if cancelar:
                st.session_state.editando = None
                st.rerun()

    # ================= LISTAR PACIENTES =================
    lista.ordenar_por_nome()

    st.divider()
    st.subheader("Pacientes Cadastrados")

    df = lista.dataframe()

    if df.empty:
        st.info("Nenhum paciente cadastrado.")
    else:

        for _, p in df.iterrows():

            cols = st.columns([2,2,1,2,2,1,1])

            cols[0].write(p["Nome"])
            cols[1].write(p["CPF"])
            cols[2].write(str(p["Idade"]))
            cols[3].write(p["Telefone"])
            cols[4].write(p["Portador de deficiência"])

            if cols[5].button("Editar", key=f"editar_{p['CPF']}"):
                st.session_state.editando = p["CPF"]
                st.rerun()

            if cols[6].button("Excluir", key=f"excluir_{p['CPF']}"):

                ok, msg = service.excluir(p["CPF"])

                if ok:
                    st.success(msg)
                else:
                    st.error(msg)

                st.rerun()