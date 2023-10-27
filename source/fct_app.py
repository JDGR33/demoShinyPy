from shiny import ui
def modal_welcome()->ui.modal_show:

    m = ui.modal(
        ui.div(
            ui.p("I will be adding more text and information shortly!"),
            ui.modal_button("Ok!"),# To close the modal
        ),
        title="Welcome to my Shiny Demo app",
        easy_close=True,
        footer=None,
    )
    return ui.modal_show(m)