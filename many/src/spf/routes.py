import flet as ft
from flet import Page
from spf.views import LoginView, StartView, MapView


route_map = {
    "/": StartView,
    "/login": LoginView,
    "/map": MapView,
}


def on_route_change(route, page: Page):
    page.views.clear()
    page.views.append(StartView(page))
    if page.route != "/":
        page.views.append(route_map[str(page.route)](page))
    page.update()


def on_view_pop(view, page):
    page.views.pop()
    top_view = page.views[-1]

    page.go(top_view.route)
