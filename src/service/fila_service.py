from core.fila_atendimento import FilaAtendimento
from core.paciente import ListaPacientes
from core.pilha_acoes import Pilha


class FilaService:

    def __init__(self, lista, fila, pilha):
        self.lista = lista
        self.fila = fila
        self.pilha = pilha

    # ======================
    # ADICIONAR NA FILA
    # ======================
    def adicionar(self, cpf, nivel):

        paciente = self.lista.buscar(cpf)

        if not paciente:
            return False, "Paciente não cadastrado."

        ok = self.fila.adicionar(paciente, nivel)

        if not ok:
            return False, "Paciente já está na fila."

        self.pilha.empilhar({
            "tipo": "adicionar_fila",
            "paciente": paciente,
            "nivel": nivel
        })

        return True, "Paciente adicionado."

    # ======================
    # ATENDER PRÓXIMO
    # ======================
    def atender(self):

        paciente = self.fila.atender_proximo()

        if not paciente:
            return False, "Fila vazia."

        self.pilha.empilhar({
            "tipo": "atender",
            "paciente": paciente.paciente,
            "nivel": paciente.nivel
        })

        return True, f"Atendendo {paciente.paciente.nome}"

    # ======================
    # DESFAZER ÚLTIMA AÇÃO
    # ======================
    def desfazer(self):

        acao = self.pilha.desempilhar()

        if not acao:
            return False, "Nada para desfazer."

        if acao["tipo"] == "adicionar_fila":
            self.fila.remover(acao["paciente"].cpf)

        elif acao["tipo"] == "atender":
            self.fila.adicionar(
                acao["paciente"],
                acao["nivel"]
            )

        return True, "Ação desfeita."