from categoria import Categoria
from produto import Produto
from desktop import Desktop
from notebook import Notebook

# Criando categorias
categoria_desktop = Categoria(1, "Desktop")
categoria_notebook = Categoria(2, "Notebook")

# Criando produtos
desktop_1 = Desktop("Dell XPS", "Preto", 5000.00, categoria_desktop, "750W")
desktop_2 = Desktop("HP Pavilion", "Branco", 3500.00, categoria_desktop, "500W")

notebook_1 = Notebook("MacBook Pro", "Cinza Espacial", 12000.00, categoria_notebook, "8 horas")
notebook_2 = Notebook("Lenovo Ideapad", "Prata", 5500.00, categoria_notebook, "6 horas")

# Imprimindo informações dos produtos
print("**Informações do Desktop 1:**")
print(desktop_1.getInformacoes())

print("\n**Informações do Desktop 2:**")
print(desktop_2.getInformacoes())

print("\n**Informações do Notebook 1:**")
print(notebook_1.getInformacoes())

print("\n**Informações do Notebook 2:**")
print(notebook_2.getInformacoes())

# Alterando a potência da fonte do Desktop 1
desktop_1.setPotenciaDaFonte("1000W")

# Imprimindo informações atualizadas do Desktop 1
print("\n**Informações atualizadas do Desktop 1:**")
print(desktop_1.getInformacoes())