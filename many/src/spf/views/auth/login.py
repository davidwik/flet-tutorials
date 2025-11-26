import flet as ft


class LoginView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = "/login"
        self.width = 400
        self.controls = [ft.AppBar(title=ft.Text("LoginPage"))]

        self.controls = [
            ft.AppBar(
                title=ft.Text("LOGIN PAGE"),
                bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            ),
            ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
            ft.ElevatedButton("View map", on_click=lambda _: page.go("/map")),
        ]
