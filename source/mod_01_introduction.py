from shiny import module, ui

@module.ui
def welcome_ui():
    welcome_text = "Welcome to Our Web App!\nIn this page you will find an introduction to the App when tabs are added."

    return  ui.nav('Introduction', welcome_text)