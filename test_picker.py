#!/usr/bin/env python3
import flet as ft

def main(page: ft.Page):
    page.title = "Test"
    
    def on_result(e):
        print(f"Result: {e}, type: {type(e)}")
        if hasattr(e, 'files'):
            print(f"Files: {e.files}")
        if hasattr(e, 'path'):
            print(f"Path: {e.path}")
    
    picker = ft.FilePicker()
    picker.on_result = on_result
    page.overlay.append(picker)
    
    def pick_click(e):
        picker.pick_files()
    
    page.add(
        ft.Button("Pick", on_click=pick_click)
    )

ft.run(main)
