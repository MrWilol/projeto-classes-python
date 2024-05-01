from produto import Produto


class Notebook(Produto):
    def __init__(self, modelo, cor, preco, categoria, tempoDeBateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
        informacoes = super().getInformacoes()
        informacoes["tempoDeBateria"] = self.__tempoDeBateria
        return informacoes

    def cadastrar(self):
        print(f"Cadastrando notebook: {self.modelo}")