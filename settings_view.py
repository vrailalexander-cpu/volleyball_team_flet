import flet as ft

from src.controllers.settings_controller import SettingsController

from src.views.components import (
    top_navigation,
    show_snackbar
)

def settings_view(page: ft.Page):
    settings = SettingsController.load_settings()
    notification_checkbox = ft.Checkbox(
        label="Увімкнути сповіщення",
        value=settings.get(
            "notifications",
            True
        )
    )
    theme_dropdown = ft.Dropdown(
        label="Тема",
        width=300,
        value=settings.get(
            "theme",
            "LIGHT"
        ),
        options=[
            ft.DropdownOption("LIGHT"),
            ft.DropdownOption("DARK")
        ]
    )

    def save_settings(e):
        data = {
            "notifications":
            notification_checkbox.value,
            "theme":
            theme_dropdown.value
        }
        SettingsController.save_settings(data)

        if theme_dropdown.value == "DARK":
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        show_snackbar(
            page,
            "Налаштування збережено"
        )
        page.update()

    return ft.View(
        route="/settings",
        controls=[
            top_navigation(page),
            ft.Container(
                expand=True,
                alignment=ft.Alignment.CENTER,
                gradient=ft.LinearGradient(
                    colors=[
                        ft.Colors.BLUE,
                        ft.Colors.CYAN
                    ]
                ),
                padding=30,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            width=400,
                            padding=40,
                            border_radius=25,
                            alignment=ft.Alignment.CENTER,
                            bgcolor="#adadad",
                            shadow=ft.BoxShadow(
                                blur_radius=20,
                                color=ft.Colors.BLACK_26
                            ),
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=25,
                                controls=[
                                    ft.Text(
                                        "Налаштування",
                                        size=32,
                                        color=ft.Colors.BLACK,
                                        weight=ft.FontWeight.BOLD
                                    ),
                                    notification_checkbox,
                                    theme_dropdown,
                                    ft.Button(
                                        "Зберегти",
                                        icon=ft.Icons.SAVE,
                                        bgcolor=ft.Colors.BLUE,
                                        color=ft.Colors.WHITE,
                                        on_click=save_settings
                                    )
                                ]
                            )
                        )
                    ]
                )
            )
        ]
    )