class NoPilha:

    def __init__(self, acao):
        self.acao = acao
        self.proximo = None


class Pilha:

    def __init__(self):
        self.topo = None

    # PUSH
    def empilhar(self, acao):

        novo = NoPilha(acao)
        novo.proximo = self.topo
        self.topo = novo

    # POP
    def desempilhar(self):

        if not self.topo:
            return None

        removido = self.topo
        self.topo = self.topo.proximo

        return removido.acao

    # VERIFICAR VAZIA
    def vazia(self):
        return self.topo is None