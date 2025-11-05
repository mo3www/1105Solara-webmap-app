import solara

@solara.component
def Page():
    solara.Markdown("# 🏠 Home Page")
    if solara.Button("Go to Global Page"):
        solara.navigate("/globle")