import flet as ft

def change_route(page, route):
    page.route = route
    if page.on_route_change:
        page.on_route_change(
            type(
                "RouteEvent",
                (),
                {"route": route}
            )
        )

def show_snackbar(page, message):
    snack = ft.SnackBar(
        content=ft.Text(message),
        action="Закрити"
    )
    page.overlay.append(snack)
    snack.open = True
    page.update()

def top_navigation(page):
    return ft.BottomAppBar(
        bgcolor=ft.Colors.BLUE,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.IconButton(
                    icon=ft.Icons.HOME,
                    icon_color=ft.Colors.WHITE,
                    icon_size=32,
                    tooltip="Головна",
                    on_click=lambda e:
                    change_route(page, "/home")
                ),
                ft.IconButton(
                    icon=ft.Icons.SETTINGS,
                    icon_color=ft.Colors.WHITE,
                    icon_size=32,
                    tooltip="Налаштування",
                    on_click=lambda e:
                    change_route(page, "/settings")
                ),
            ]
        )
    )