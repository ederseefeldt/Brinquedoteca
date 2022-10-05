from PyQt5.QtWidgets import QMessageBox
from PyQt5 import uic,QtWidgets

dicionario = {}

def adicionar():
    nome = janela.nome.text()
    idade = janela.idade.text()
    if (nome == "" or idade == ""):
        QMessageBox.about(janela, "Alerta", "Você não inseriu o nome ou a idade")
    else:
        dicionario.update({nome: idade})
        janela.filtro.addItem(idade)
        janela.nome.clear()
        janela.idade.clear()
        janela.nome.setFocus()
        
    
def fechar():
    result = QMessageBox.question(janela, "Saindo do sistema", "Deseja mesmo sair do sistema?", QMessageBox.Yes, QMessageBox.No)
    if result == QMessageBox.Yes:
        janela.close()
        
def limpar():
    janela.lista.clear()
    janela.nome.clear()
    janela.idade.clear()
    janela.nome.setFocus()

def listar():
    janela.lista.clear()
    filtro_idade = janela.filtro.currentText()
    for chave in dicionario.keys():
        if (filtro_idade != 'Filtro'):
            if (filtro_idade == dicionario[chave]):
                janela.lista.addItem(chave+" - "+ dicionario[chave])
        else:
            janela.lista.addItem(chave+" - "+ dicionario[chave])
            
#Programa
app=QtWidgets.QApplication([])
janela=uic.loadUi("tela.ui")

#Chamadas das funções
janela.btn_adicionar.clicked.connect(adicionar)
janela.btn_fechar.clicked.connect(fechar)
janela.btn_listar.clicked.connect(listar)
janela.btn_limpar.clicked.connect(limpar)

#Chama a interface e executa o código
janela.show()
app.exec()