from core.paciente import ListaPacientes


class PacienteService:

    def __init__(self, lista: ListaPacientes):
        self.lista = lista

    # ======================
    # CADASTRAR
    # ======================
    def cadastrar(self, nome, cpf, idade, telefone, deficiencia):

        if not nome or not cpf or not idade or not telefone:
            return False, "Preencha todos os campos."

        if not cpf.isdigit() or len(cpf) != 11:
            return False, "CPF inválido."

        if not str(idade).isdigit():
            return False, "Idade inválida."

        ok = self.lista.inserir(
            nome,
            cpf,
            int(idade),
            telefone,
            deficiencia
        )

        if not ok:
            return False, "CPF já cadastrado."

        return True, "Paciente cadastrado."

    # ======================
    # EXCLUIR
    # ======================
    def excluir(self, cpf):

        ok = self.lista.remover(cpf)

        if not ok:
            return False, "Paciente não encontrado."

        return True, "Paciente removido."

    # ======================
    # EDITAR
    # ======================
    def editar(self, cpf, nome, idade, telefone, deficiencia):

        ok = self.lista.atualizar(
            cpf,
            nome,
            idade,
            telefone,
            deficiencia
        )

        if not ok:
            return False, "Erro ao atualizar."

        return True, "Paciente atualizado."