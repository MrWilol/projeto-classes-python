from produto import Produto


class Desktop(Produto):
  def __init__(self, modelo, cor, preco, categoria, potenciaDaFonte):
    super().__init__(modelo, cor, preco, categoria)
    self._potenciaDaFonte = potenciaDaFonte

  def getInformacoes(self):
    informacoes = super().getInformacoes()
    informacoes["potenciaDaFonte"] = self._potenciaDaFonte
    return informacoes

  def cadastrar(self):
    print(f"Cadastrando desktop: {self.modelo}")

  def getPotenciaDaFonte(self):
    return self._potenciaDaFonte

  def setPotenciaDaFonte(self, potenciaDaFonte):
    self._potenciaDaFonte = potenciaDaFonte