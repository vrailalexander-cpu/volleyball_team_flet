import flet as ft
import asyncio

from src.controllers.home_controller import HomeController

from src.views.components import (
    top_navigation,
    show_snackbar
)

def home_view(page: ft.Page):
    selected_index = {"value": None}
    name_field = ft.TextField(
        label="Ім'я гравця",
        width=300,
        prefix_icon=ft.Icons.PERSON
    )
    number_field = ft.TextField(
        label="Номер",
        width=300,
        prefix_icon=ft.Icons.NUMBERS
    )
    position_dropdown = ft.Dropdown(
        label="Позиція",
        width=300,
        options=[
            ft.DropdownOption("Нападник"),
            ft.DropdownOption("Ліберо"),
            ft.DropdownOption("Зв'язуючий"),
        ]
    )
    players_column = ft.Column(
        scroll=ft.ScrollMode.AUTO,
        spacing=10
    )

    async def load_players():
        await asyncio.sleep(0.2)
        players_column.controls.clear()
        players = HomeController.get_players()
        for index, player in enumerate(players):
            players_column.controls.append(
                ft.Container(
                    padding=15,
                    border_radius=20,
                    bgcolor=ft.Colors.BLUE,
                    shadow=ft.BoxShadow(
                        blur_radius=8,
                        color=ft.Colors.BLACK,
                    ),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Column(
                                spacing=5,
                                controls=[
                                    ft.Text(
                                        f"{player['name']}",
                                        size=20,
                                        color=ft.Colors.WHITE,
                                        weight=ft.FontWeight.BOLD
                                    ),
                                    ft.Text(
                                        f"Номер: {player['number']}",
                                        color=ft.Colors.WHITE,
                                    ),
                                    ft.Text(
                                        f"Позиція: {player['position']}",
                                        color=ft.Colors.WHITE,
                                    ),
                                    ft.Text(
                                        f"Дата: {player['created_at']}",
                                        color=ft.Colors.WHITE,
                                    ),
                                ]
                            ),

                            ft.Row(
                                controls=[
                                    ft.IconButton(
                                        icon=ft.Icons.EDIT,
                                        icon_color=ft.Colors.YELLOW,
                                        on_click=lambda e,
                                        i=index,
                                        p=player:
                                        fill_fields(i, p)
                                    ),

                                    ft.IconButton(
                                        icon=ft.Icons.DELETE,
                                        icon_color=ft.Colors.RED,
                                        on_click=lambda e,
                                        i=index:
                                        delete_player(i)
                                    )
                                ]
                            )
                        ]
                    )
                )
            )
        page.update()

    def fill_fields(index, player):
        selected_index["value"] = index
        name_field.value = player["name"]
        number_field.value = player["number"]
        position_dropdown.value = player["position"]
        page.update()

    async def create_player_async():
        await asyncio.sleep(0.2)
        if not name_field.value.isalpha():
            show_snackbar(
                page,
                "Ім'я повинно містити лише літери"
            )
            return

        if not number_field.value.isdigit():
            show_snackbar(
                page,
                "Номер повинен містити лише цифри"
            )
            return

        if not position_dropdown.value:
            show_snackbar(
                page,
                "Оберіть позицію гравця"
            )
            return
        HomeController.create_player(
            name_field.value,
            number_field.value,
            position_dropdown.value
        )
        show_snackbar(
            page,
            "Гравця створено"
        )
        clear_fields()
        await load_players()

    async def update_player_async():
        await asyncio.sleep(0.2)
        if selected_index["value"] is None:
            show_snackbar(
                page,
                "Оберіть гравця"
            )
            return

        HomeController.update_player(
            selected_index["value"],
            {
                "name": name_field.value,
                "number": number_field.value,
                "position": position_dropdown.value
            }
        )

        show_snackbar(
            page,
            "Дані оновлено"
        )
        clear_fields()
        await load_players()

    def delete_player(index):
        HomeController.delete_player(index)
        show_snackbar(
            page,
            "Гравця видалено"
        )
        page.run_task(load_players)

    def clear_fields():
        name_field.value = ""
        number_field.value = ""
        position_dropdown.value = None
        selected_index["value"] = None
        page.update()
    page.run_task(load_players)

    return ft.View(
        route="/home",
        controls=[
            top_navigation(page),
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(
                    colors=[
                        ft.Colors.BLUE,
                        ft.Colors.CYAN
                    ]
                ),
                padding=20,
                content=ft.Row(
                    spacing=20,
                    controls=[
                        ft.Container(
                            width=350,
                            padding=20,
                            border_radius=25,
                            bgcolor=ft.Colors.WHITE,
                            shadow=ft.BoxShadow(
                                blur_radius=12,
                                color=ft.Colors.BLACK_12
                            ),
                            content=ft.Column(
                                spacing=20,
                                controls=[
                                    ft.Text(
                                        "Гравці",
                                        size=28,
                                        color=ft.Colors.BLACK,
                                        weight=ft.FontWeight.BOLD
                                    ),
                                    name_field,
                                    number_field,
                                    position_dropdown,
                                    ft.Button(
                                        "Створити",
                                        icon=ft.Icons.ADD,
                                        bgcolor="#2196F3",
                                        color=ft.Colors.WHITE,
                                        on_click=lambda e:
                                        page.run_task(
                                            create_player_async
                                        )
                                    ),
                                    ft.Button(
                                        "Оновити",
                                        icon=ft.Icons.UPDATE,
                                        bgcolor="#00BCD4",
                                        color=ft.Colors.WHITE,
                                        on_click=lambda e:
                                        page.run_task(
                                            update_player_async
                                        )
                                    )
                                ]
                            )
                        ),
                        ft.Container(
                            expand=True,
                            padding=20,
                            border_radius=25,
                            bgcolor=ft.Colors.WHITE,
                            shadow=ft.BoxShadow(
                                blur_radius=12,
                                color=ft.Colors.BLACK_12
                            ),

                            content=ft.Column(
                                controls=[
                                    ft.Text(
                                        "Список гравців",
                                        size=28,
                                        color=ft.Colors.BLACK,
                                        weight=ft.FontWeight.BOLD
                                    ),
                                    ft.ListView(
                                        expand=True,
                                        spacing=15,
                                        controls=[
                                            players_column
                                        ]
                                    )
                                ]
                            )
                        )
                    ]
                )
            )
        ]
    )