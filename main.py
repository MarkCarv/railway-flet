import logging
import flet as ft
import os


def main(page: ft.Page):
    page.add(ft.Text("Hello, Railway!"))


logging.basicConfig(level=logging.INFO)

ft.app(target=main, view=ft.WEB_BROWSER, port=int(os.getenv("PORT", 8502)))
