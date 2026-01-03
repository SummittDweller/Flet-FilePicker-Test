#!/usr/bin/env python3
"""
Flet FilePicker Test App
A simple test application to demonstrate FilePicker functionality in Flet on macOS.
"""

import flet as ft
from datetime import datetime
import os

# File extension filters
SINGLE_FILE_EXTENSIONS = ["txt", "pdf", "png", "jpg", "jpeg"]
SAVE_FILE_EXTENSIONS = ["txt", "log", "md"]

# Log storage
log_entries = []


def log_message(message):
    """Add a timestamped log entry."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    entry = f"[{timestamp}] {message}"
    log_entries.append(entry)
    print(entry)
    return entry


def main(page: ft.Page):
    page.title = "Flet FilePicker Test"
    page.padding = 20
    
    # Set app icon for dock and window (use ICNS for macOS)
    icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "app_icon.icns"))
    if os.path.exists(icon_path):
        page.window.icon = icon_path
        page.update()  # Update to apply icon
        log_message(f"App icon set: {icon_path}")
    else:
        log_message(f"App icon not found: {icon_path}")
    
    log_message("Application started")
    
    # Create a result text display
    result_text = ft.Text(
        "No file selected yet",
        size=16,
        selectable=True
    )
    
    # Status text
    status_text = ft.Text(
        "Ready to pick files",
        color=ft.Colors.BLUE_400,
        size=14,
        italic=True
    )
    
    # Button handlers
    async def pick_single_file(e):
        log_message("Pick Single File button clicked")
        status_text.value = "Opening file picker..."
        status_text.color = ft.Colors.BLUE_400
        page.update()
        
        files = await file_picker.pick_files(
            allowed_extensions=SINGLE_FILE_EXTENSIONS,
            dialog_title="Pick a single file"
        )
        
        if files:
            selected_files = "\n".join([f.path for f in files])
            result_text.value = f"Selected file(s):\n{selected_files}"
            status_text.value = f"{len(files)} file(s) selected"
            status_text.color = ft.Colors.GREEN_400
            log_message(f"Selected {len(files)} file(s): {', '.join([f.name for f in files])}")
        else:
            result_text.value = "No file selected (cancelled)"
            status_text.value = "File selection cancelled"
            status_text.color = ft.Colors.ORANGE_400
            log_message("File selection cancelled")
        page.update()
    
    async def pick_multiple_files(e):
        log_message("Pick Multiple Files button clicked")
        status_text.value = "Opening file picker..."
        status_text.color = ft.Colors.BLUE_400
        page.update()
        
        files = await file_picker.pick_files(
            allow_multiple=True,
            dialog_title="Pick multiple files"
        )
        
        if files:
            selected_files = "\n".join([f.path for f in files])
            result_text.value = f"Selected file(s):\n{selected_files}"
            status_text.value = f"{len(files)} file(s) selected"
            status_text.color = ft.Colors.GREEN_400
            log_message(f"Selected {len(files)} file(s): {', '.join([f.name for f in files])}")
        else:
            result_text.value = "No files selected (cancelled)"
            status_text.value = "File selection cancelled"
            status_text.color = ft.Colors.ORANGE_400
            log_message("Multiple file selection cancelled")
        page.update()
    
    async def pick_dir(e):
        log_message("Pick Directory button clicked")
        status_text.value = "Opening directory picker..."
        status_text.color = ft.Colors.BLUE_400
        page.update()
        
        path = await directory_picker.get_directory_path(
            dialog_title="Pick a directory"
        )
        
        if path:
            result_text.value = f"Selected directory:\n{path}"
            status_text.value = "Directory selected"
            status_text.color = ft.Colors.GREEN_400
            log_message(f"Selected directory: {path}")
        else:
            result_text.value = "No directory selected (cancelled)"
            status_text.value = "Directory selection cancelled"
            status_text.color = ft.Colors.ORANGE_400
            log_message("Directory selection cancelled")
        page.update()
    
    async def save_file(e):
        log_message("Save File button clicked")
        status_text.value = "Opening save dialog..."
        status_text.color = ft.Colors.BLUE_400
        page.update()
        
        path = await save_file_picker.save_file(
            dialog_title="Save log file as...",
            file_name="flet_filepicker_test.log",
            allowed_extensions=SAVE_FILE_EXTENSIONS
        )
        
        if path:
            try:
                # Write log entries to file
                with open(path, 'w') as f:
                    f.write("Flet FilePicker Test App - Activity Log\n")
                    f.write("=" * 50 + "\n\n")
                    for entry in log_entries:
                        f.write(entry + "\n")
                
                result_text.value = f"Log file saved to:\n{path}\n\nTotal log entries: {len(log_entries)}"
                status_text.value = "Log file saved successfully"
                status_text.color = ft.Colors.GREEN_400
                log_message(f"Log file saved to: {path} ({len(log_entries)} entries)")
            except Exception as ex:
                result_text.value = f"Error saving file:\n{str(ex)}"
                status_text.value = "Error saving file"
                status_text.color = ft.Colors.RED_400
                log_message(f"Error saving log file: {str(ex)}")
        else:
            result_text.value = "Save file cancelled"
            status_text.value = "Save operation cancelled"
            status_text.color = ft.Colors.ORANGE_400
            log_message("Save file operation cancelled")
        page.update()
    
    # Create FilePicker instances
    file_picker = ft.FilePicker()
    directory_picker = ft.FilePicker()
    save_file_picker = ft.FilePicker()
    
    # Add pickers to services (not overlay - FilePicker is a Service, not a Control)
    page.services.append(file_picker)
    page.services.append(directory_picker)
    page.services.append(save_file_picker)
    
    # Create UI
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "Flet FilePicker Test Application",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_700
                    ),
                    ft.Divider(height=20, color=ft.Colors.BLUE_200),
                    ft.Text(
                        "Test FilePicker functionality on macOS:",
                        size=16,
                        weight=ft.FontWeight.W_500
                    ),
                    ft.Container(height=10),
                    ft.Row(
                        [
                            ft.Button(
                                "Pick Single File",
                                icon=ft.Icons.FILE_OPEN,
                                on_click=pick_single_file,
                                style=ft.ButtonStyle(
                                    color=ft.Colors.WHITE,
                                    bgcolor=ft.Colors.BLUE_700,
                                )
                            ),
                            ft.Button(
                                "Pick Multiple Files",
                                icon=ft.Icons.FILE_OPEN,
                                on_click=pick_multiple_files,
                                style=ft.ButtonStyle(
                                    color=ft.Colors.WHITE,
                                    bgcolor=ft.Colors.BLUE_500,
                                )
                            ),
                        ],
                        wrap=True,
                        spacing=10
                    ),
                    ft.Container(height=5),
                    ft.Row(
                        [
                            ft.Button(
                                "Pick Directory",
                                icon=ft.Icons.FOLDER_OPEN,
                                on_click=pick_dir,
                                style=ft.ButtonStyle(
                                    color=ft.Colors.WHITE,
                                    bgcolor=ft.Colors.GREEN_700,
                                )
                            ),
                            ft.Button(
                                "Save File",
                                icon=ft.Icons.SAVE,
                                on_click=save_file,
                                style=ft.ButtonStyle(
                                    color=ft.Colors.WHITE,
                                    bgcolor=ft.Colors.ORANGE_700,
                                )
                            ),
                        ],
                        wrap=True,
                        spacing=10
                    ),
                    ft.Container(height=20),
                    ft.Divider(height=1, color=ft.Colors.GREY_300),
                    ft.Container(height=10),
                    status_text,
                    ft.Container(height=10),
                    ft.Container(
                        content=result_text,
                        bgcolor=ft.Colors.GREY_100,
                        border=ft.Border.all(1, ft.Colors.GREY_300),
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
    ft.run(main)
