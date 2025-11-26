from flet import CrossAxisAlignment, app, Page, AppView
from spf.routes import on_route_change, on_view_pop
# from spf.pages.login import LoginPage


def main(page: Page):
    page.title = "SPF"
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    page.on_route_change = lambda e: on_route_change(e, page)
    page.on_view_pop = lambda e: on_view_pop(e, page)

    page.go(page.route)


app(main, AppView.WEB_BROWSER)  # type: ignore
