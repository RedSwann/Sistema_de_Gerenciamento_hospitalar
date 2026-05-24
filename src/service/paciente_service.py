from core.paciente import ListaPacientes


class PacienteService:

    def __init__(self, lista: ListaPacientes, historico=None):
        self.lista = lista
        self.historico = historico

    # ======================
    # VALIDAÇÕES
    # ======================
    def _validar_dados(self, nome, cpf, idade, telefone):

        nome = str(nome).strip()
        cpf = str(cpf).strip()
        idade = str(idade).strip()
        telefone = str(telefone).strip()

        if not nome:
            return False, "Preencha o campo Nome."

        if not cpf:
            return False, "Preencha o campo CPF."

        if not cpf.isdigit():
            return False, "CPF deve conter apenas números."

        if len(cpf) != 11:
            return False, "CPF deve conter exatamente 11 dígitos."

        if not idade:
            return False, "Preencha o campo Idade."

        if not idade.isdigit():
            return False, "Idade deve conter apenas números."

        idade_int = int(idade)

        if idade_int <= 0 or idade_int > 120:
            return False, "Idade deve estar entre 1 e 120 anos."

        if not telefone:
            return False, "Preencha o campo Telefone."

        if not telefone.isdigit():
            return False, "Telefone deve conter apenas números."

        if len(telefone) != 11:
            return False, "Telefone deve conter exatamente 11 dígitos."

        return True, "Dados válidos."

    # ======================
    # CADASTRAR
    # ======================
    def cadastrar(self, nome, cpf, idade, telefone, deficiencia):

        ok, msg = self._validar_dados(nome, cpf, idade, telefone)

        if not ok:
            return False, msg

        nome = str(nome).strip()
        cpf = str(cpf).strip()
        idade = int(str(idade).strip())
        telefone = str(telefone).strip()

        ok = self.lista.inserir(
            nome,
            cpf,
            idade,
            telefone,
            deficiencia
        )

        if not ok:
            return False, "CPF já cadastrado."

        if self.historico:
            self.historico.registrar(
                "Cadastro de paciente",
                f"Paciente {nome} cadastrado com CPF {cpf}."
            )

        return True, "Paciente cadastrado com sucesso."

    # ======================
    # EXCLUIR
    # ======================
    def excluir(self, cpf):

        ok = self.lista.remover(cpf)

        if not ok:
            return False, "Paciente não encontrado."

        return True, "Paciente removido com sucesso."

    # ======================
    # EDITAR
    # ======================
    def editar(self, cpf, nome, idade, telefone, deficiencia):

        ok, msg = self._validar_dados(nome, cpf, idade, telefone)

        if not ok:
            return False, msg

        ok = self.lista.atualizar(
            str(cpf).strip(),
            str(nome).strip(),
            int(str(idade).strip()),
            str(telefone).strip(),
            deficiencia
        )

        if not ok:
            return False, "Erro ao atualizar."

        return True, "Paciente atualizado com sucesso."
