import flet as ft

from src.views.login_view import login_view
from src.views.home_view import home_view
from src.views.settings_view import settings_view


def main(page: ft.Page):
    page.title = "Волейбольна команда"
    page.window_width = 1300
    page.window_height = 850
    page.padding = 0
    page.spacing = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.BLUE

    def page_on_route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(login_view(page))
        elif page.route == "/home":
            page.views.append(home_view(page))
        elif page.route == "/settings":
            page.views.append(settings_view(page))
        page.update()

    page.on_route_change = lambda e: page_on_route_change(e.route)
    page.route = "/"
    page_on_route_change("/")

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)