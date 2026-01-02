#!/usr/bin/env python3
"""
Flet FilePicker Test App
A simple test application to demonstrate FilePicker functionality in Flet on macOS.
"""

import flet as ft


def main(page: ft.Page):
    page.title = "Flet FilePicker Test"
    page.window.width = 600
    page.window.height = 500
    page.padding = 20
    
    # Create a result text display
    result_text = ft.Text(
        "No file selected yet",
        size=16,
        selectable=True
    )
    
    # Status text
    status_text = ft.Text(
        "Ready to pick files",
        color=ft.colors.BLUE_400,
        size=14,
        italic=True
    )
    
    # FilePicker result handler
    def pick_files_result(e: ft.FilePickerResultEvent):
        if e.files:
            selected_files = "\n".join([f.path for f in e.files])
            result_text.value = f"Selected file(s):\n{selected_files}"
            status_text.value = f"{len(e.files)} file(s) selected"
            status_text.color = ft.colors.GREEN_400
        else:
            result_text.value = "No file selected (cancelled)"
            status_text.value = "File selection cancelled"
            status_text.color = ft.colors.ORANGE_400
        page.update()
    
    def pick_directory_result(e: ft.FilePickerResultEvent):
        if e.path:
            result_text.value = f"Selected directory:\n{e.path}"
            status_text.value = "Directory selected"
            status_text.color = ft.colors.GREEN_400
        else:
            result_text.value = "No directory selected (cancelled)"
            status_text.value = "Directory selection cancelled"
            status_text.color = ft.colors.ORANGE_400
        page.update()
    
    def save_file_result(e: ft.FilePickerResultEvent):
        if e.path:
            result_text.value = f"Save file path:\n{e.path}"
            status_text.value = "Save path selected"
            status_text.color = ft.colors.GREEN_400
        else:
            result_text.value = "Save file cancelled"
            status_text.value = "Save operation cancelled"
            status_text.color = ft.colors.ORANGE_400
        page.update()
    
    # Create FilePicker instances
    file_picker = ft.FilePicker(on_result=pick_files_result)
    directory_picker = ft.FilePicker(on_result=pick_directory_result)
    save_file_picker = ft.FilePicker(on_result=save_file_result)
    
    # Add pickers to overlay
    page.overlay.extend([file_picker, directory_picker, save_file_picker])
    
    # Button handlers
    def pick_single_file(e):
        status_text.value = "Opening file picker..."
        status_text.color = ft.colors.BLUE_400
        page.update()
        file_picker.pick_files(
            allowed_extensions=["txt", "pdf", "png", "jpg", "jpeg"],
            dialog_title="Pick a single file"
        )
    
    def pick_multiple_files(e):
        status_text.value = "Opening file picker..."
        status_text.color = ft.colors.BLUE_400
        page.update()
        file_picker.pick_files(
            allow_multiple=True,
            dialog_title="Pick multiple files"
        )
    
    def pick_dir(e):
        status_text.value = "Opening directory picker..."
        status_text.color = ft.colors.BLUE_400
        page.update()
        directory_picker.get_directory_path(
            dialog_title="Pick a directory"
        )
    
    def save_file(e):
        status_text.value = "Opening save dialog..."
        status_text.color = ft.colors.BLUE_400
        page.update()
        save_file_picker.save_file(
            dialog_title="Save file as...",
            file_name="output.txt",
            allowed_extensions=["txt", "log", "md"]
        )
    
    # Create UI
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "Flet FilePicker Test Application",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.BLUE_700
                    ),
                    ft.Divider(height=20, color=ft.colors.BLUE_200),
                    ft.Text(
                        "Test FilePicker functionality on macOS:",
                        size=16,
                        weight=ft.FontWeight.W_500
                    ),
                    ft.Container(height=10),
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                "Pick Single File",
                                icon=ft.icons.FILE_OPEN,
                                on_click=pick_single_file,
                                style=ft.ButtonStyle(
                                    color=ft.colors.WHITE,
                                    bgcolor=ft.colors.BLUE_700,
                                )
                            ),
                            ft.ElevatedButton(
                                "Pick Multiple Files",
                                icon=ft.icons.FILE_OPEN,
                                on_click=pick_multiple_files,
                                style=ft.ButtonStyle(
                                    color=ft.colors.WHITE,
                                    bgcolor=ft.colors.BLUE_500,
                                )
                            ),
                        ],
                        wrap=True,
                        spacing=10
                    ),
                    ft.Container(height=5),
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                "Pick Directory",
                                icon=ft.icons.FOLDER_OPEN,
                                on_click=pick_dir,
                                style=ft.ButtonStyle(
                                    color=ft.colors.WHITE,
                                    bgcolor=ft.colors.GREEN_700,
                                )
                            ),
                            ft.ElevatedButton(
                                "Save File",
                                icon=ft.icons.SAVE,
                                on_click=save_file,
                                style=ft.ButtonStyle(
                                    color=ft.colors.WHITE,
                                    bgcolor=ft.colors.ORANGE_700,
                                )
                            ),
                        ],
                        wrap=True,
                        spacing=10
                    ),
                    ft.Container(height=20),
                    ft.Divider(height=1, color=ft.colors.GREY_300),
                    ft.Container(height=10),
                    status_text,
                    ft.Container(height=10),
                    ft.Container(
                        content=result_text,
                        bgcolor=ft.colors.GREY_100,
                        border=ft.border.all(1, ft.colors.GREY_300),
                        border_radius=8,
                        padding=15,
                        expand=True
                    ),
                ],
                scroll=ft.ScrollMode.AUTO,
                spacing=5
            ),
            expand=True
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
