# Importando os módulos necessários
import flet as ft
import tela1, tela2, tela3

# Inicializando variáveis globais
def init(p):
    global page, telas, cadastros        
    page = p
    cadastros = []    
    telas = {
        '0': tela1.view(),
        '1': tela2.view(),
        '2': tela3.view(),
    }
    

# Função chamada quando há uma mudança de rota (página)
def route_change(route):
    # Limpa as views na página
    page.views.clear()    
    # Adiciona a view correspondente à rota atual
    page.views.append(
        telas[page.route]
    )          
    page.update()

# Função para atualizar a tabela na tela2
def menu(e):
    # Atualiza as linhas da tabela com os dados atuais
    tela2.components["tabela"].current.rows = tela2.data_table()
