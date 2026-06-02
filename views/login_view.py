import flet as ft
import asyncio

from src.controllers.auth_controller import AuthController

from src.views.components import (
    change_route,
    show_snackbar
)

def login_view(page: ft.Page):
    name_field = ft.TextField(
        label="Ім'я",
        width=350,
        border_radius=15,
        prefix_icon=ft.Icons.PERSON
    )
    password_field = ft.TextField(
        label="Пароль",
        width=350,
        password=True,
        can_reveal_password=True,
        border_radius=15,
        prefix_icon=ft.Icons.LOCK
    )

    async def login_async():
        await asyncio.sleep(0.5)
        is_valid = AuthController.login(
            name_field.value,
            password_field.value
        )

        if is_valid:
            page.session.store.set(
                "user",
                name_field.value
            )
            show_snackbar(
                page,
                "Успішний вхід"
            )
            await asyncio.sleep(1)
            change_route(page, "/home")
        else:
            show_snackbar(
                page,
                "Некоректне ім'я або пароль"
            )

    def login_click(e):
        page.run_task(login_async)

    return ft.View(
        route="/",
        controls=[
            ft.Container(
                expand=True,
                alignment=ft.Alignment.CENTER,
                gradient=ft.LinearGradient(
                    colors=[
                        ft.Colors.BLUE,
                        ft.Colors.CYAN
                    ]
                ),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            width=500,
                            padding=40,
                            border_radius=25,
                            alignment=ft.Alignment.CENTER,
                            bgcolor=ft.Colors.WHITE,
                            shadow=ft.BoxShadow(
                                blur_radius=20,
                                color=ft.Colors.BLACK_26
                            ),
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=25,
                                controls=[
                                    ft.Icon(
                                        ft.Icons.SPORTS_VOLLEYBALL,
                                        size=90,
                                        color="#2196F3"
                                    ),
                                    ft.Text(
                                        "Волейбольна команда",
                                        size=32,
                                        weight=ft.FontWeight.BOLD,
                                        color="#1565C0"
                                    ),
                                    name_field,
                                    password_field,
                                    ft.Button(
                                        "Увійти",
                                        width=350,
                                        height=50,
                                        bgcolor="#2196F3",
                                        color=ft.Colors.WHITE,
                                        icon=ft.Icons.LOGIN,
                                        on_click=login_click
                                    ),
                                    ft.OutlinedButton(
                                        "Реєстрація",
                                        width=350,
                                        height=50,
                                        icon=ft.Icons.APP_REGISTRATION
                                    )
                                ]
                            )
                        )
                    ]
                )
            )
        ]
    )