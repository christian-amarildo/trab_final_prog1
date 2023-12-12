# Importa os módulos flet e control para utilizar as funcionalidades dessas bibliotecas.
import flet as ft
import control as c

# Define a função main que recebe um parâmetro page do tipo ft.Page.
def main(page: ft.Page):        
# Inicializa o controle da página usando a função init do módulo control, passando a página como parâmetro.  
    c.init(page)
# Define o título da página como "Sistema de cadastro".    
    page.title = "Sistema de cadastro"
# Configura a função route_change do módulo control como a função a ser chamada quando houver uma mudança de rota.         
    page.on_route_change = c.route_change  
# Define o modo de tema da página como "dark".    
    page.theme_mode  = "dark"
# Navega para a rota '0'. Isso pode indicar que o aplicativo está indo para a tela inicial.  
    page.go('0')
# Define um esquema de cores para o tema da página. Nesse caso, um esquema de cores com a semente 'green' (verde).    
    page.theme = ft.Theme(color_scheme_seed='green')
# Atualiza a página com as configurações e alterações feitas anteriormente.    
    page.update()
    

# Inicia o aplicativo usando a função app do módulo flet. Passa a função main como o alvo principal do aplicativo.
ft.app(target=main)

