import flet as ft


class StartView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = "/"
        self.width = 400
        self.controls = [ft.AppBar(title=ft.Text("Start"))]

        self.controls = [
            ft.AppBar(
                title=ft.Text("Welcome"),
                bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            ),
            ft.ElevatedButton("Login", on_click=lambda _: page.go("/login")),
        ]
