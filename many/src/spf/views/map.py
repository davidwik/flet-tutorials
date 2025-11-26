import flet as ft
import flet_map as map


class MapView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = "/map"
        self.width = 400
        self.controls = [ft.AppBar(title=ft.Text("Map"))]

        self.controls = [
            ft.AppBar(
                title=ft.Text("Map"),
                bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            ),
            map.Map(
                expand=True,
                initial_center=map.MapLatitudeLongitude(
                    55.621015769185284, 12.572095542019923
                ),
                initial_zoom=19.5,
                on_init=lambda e: print("Map Init"),
                on_tap=self.handle_tap,
                layers=[
                    map.TileLayer(
                        url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png"
                    )
                ],
            ),
        ]

    def handle_tap(self, e: map.MapTapEvent):
        print(e)
