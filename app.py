from shiny import App, Inputs, Outputs, Session, ui
from pathlib import Path
# Import app-modules
from source.mod_01_introduction import welcome_ui

css_path = Path(__file__).parent / "www" / "demoShinyPy-styles.css"

app_ui = ui.page_fluid(
    ui.navset_tab(
        welcome_ui('welcome_tab'),
    )    
)

def server(input: Inputs, output: Outputs, session: Session):
    pass

app = App(app_ui, server)

