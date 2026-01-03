#!/usr/bin/env python3
import flet as ft

def main(page: ft.Page):
    page.title = "Flet FilePicker Test"
    
    result_text = ft.Text("No file selected yet")
    
    def pick_files_result(e):
        if e.files:
            selected_files = "\n".join([f.path for f in e.files])
            result_text.value = f"Selected file(s):\n{selected_files}"
        else:
            result_text.value = "No file selected (cancelled)"
        page.update()
    
    file_picker = ft.FilePicker()
    file_picker.on_result = pick_files_result
    page.overlay.append(file_picker)
    
    def pick_single_file(e):
        file_picker.pick_files()
    
    page.add(
        ft.Column([
            ft.Text("Flet FilePicker Test", size=24),
            ft.Button("Pick File", on_click=pick_single_file),
            result_text
        ])
    )

ft.run(main)
