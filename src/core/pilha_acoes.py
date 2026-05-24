import json
import os
from datetime import datetime


class NoPilha:

    def __init__(self, acao):
        self.acao = acao
        self.proximo = None


class Pilha:

    def __init__(self, arquivo="src/data/historico_acoes.json", limite=50):
        self.topo = None
        self.arquivo = arquivo
        self.limite = limite
        self.carregar_json()

    # =========================
    # PUSH / EMPILHAR
    # =========================
    def empilhar(self, acao):
        novo = NoPilha(acao)
        novo.proximo = self.topo
        self.topo = novo
        self._limitar_tamanho()
        self.salvar_json()

    # =========================
    # REGISTRAR AÇÃO NO HISTÓRICO
    # =========================
    def registrar(self, acao, detalhes):
        registro = {
            "acao": acao,
            "detalhes": detalhes,
            "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }

        self.empilhar(registro)

    # =========================
    # POP / DESEMPILHAR
    # =========================
    def desempilhar(self):
        if not self.topo:
            return None

        removido = self.topo
        self.topo = self.topo.proximo
        self.salvar_json()

        return removido.acao

    # =========================
    # VERIFICAR VAZIA
    # =========================
    def vazia(self):
        return self.topo is None

    # =========================
    # LISTAR DO MAIS RECENTE PARA O MAIS ANTIGO
    # =========================
    def listar(self):
        dados = []
        atual = self.topo

        while atual:
            dados.append(atual.acao)
            atual = atual.proximo

        return dados

    # =========================
    # CONTAR ELEMENTOS
    # =========================
    def tamanho(self):
        contador = 0
        atual = self.topo

        while atual:
            contador += 1
            atual = atual.proximo

        return contador

    # =========================
    # SALVAR JSON
    # =========================
    def salvar_json(self):
        dados = self.listar()

        pasta = os.path.dirname(self.arquivo)
        if pasta:
            os.makedirs(pasta, exist_ok=True)

        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    # =========================
    # CARREGAR JSON
    # =========================
    def carregar_json(self):
        if not os.path.exists(self.arquivo):
            return

        try:
            with open(self.arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
        except json.JSONDecodeError:
            return

        # O JSON fica salvo do mais recente para o mais antigo.
        # Para reconstruir a pilha mantendo essa ordem, empilha de trás para frente.
        for acao in reversed(dados):
            novo = NoPilha(acao)
            novo.proximo = self.topo
            self.topo = novo

        self._limitar_tamanho()

    # =========================
    # MANTER APENAS AS ÚLTIMAS AÇÕES
    # =========================
    def _limitar_tamanho(self):
        if self.limite <= 0:
            self.topo = None
            return

        atual = self.topo
        contador = 1

        while atual and contador < self.limite:
            atual = atual.proximo
            contador += 1

        if atual:
            atual.proximo = None
