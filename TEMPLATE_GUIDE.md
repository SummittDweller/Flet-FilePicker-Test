# Flet FilePicker Template Guide

## 🎯 Purpose

This project serves as a **reference template** for implementing FilePicker functionality in **Flet 0.80+**. The API changed significantly in version 0.80, and this template demonstrates the correct modern approach.

---

## 🔑 Critical API Changes in Flet 0.80+

### 1. FilePicker is a Service, Not a Control

```python
# ❌ OLD WAY (doesn't work in 0.80+)
page.overlay.append(file_picker)

# ✅ NEW WAY (correct)
page.services.append(file_picker)
```

**Why:** FilePicker changed from a Control to a Service in Flet 0.80. Services must be added to `page.services`, not `page.overlay`.

---

### 2. No More Callbacks - Methods Return Values

```python
# ❌ OLD WAY (callback-based, doesn't work)
def on_result(e: ft.FilePickerResultEvent):
    if e.files:
        print(e.files)

file_picker = ft.FilePicker(on_result=on_result)
file_picker.pick_files()

# ✅ NEW WAY (return-value based)
file_picker = ft.FilePicker()
files = await file_picker.pick_files()  # Returns list directly
if files:
    for file in files:
        print(file.path, file.name, file.size)
```

**Why:** The API changed from event-driven callbacks to direct return values for cleaner async/await patterns.

---

### 3. All Methods Are Async

```python
# ✅ Handler must be async and use await
async def pick_file_handler(e):
    files = await file_picker.pick_files()
    if files:
        # Process files
        pass
```

**Why:** FilePicker methods now return coroutines and must be awaited.

---

### 4. Return Types Reference

| Method | Returns | On Cancel |
|--------|---------|-----------|
| `pick_files()` | `list[FilePickerFile]` | Empty list `[]` |
| `get_directory_path()` | `str \| None` | `None` |
| `save_file()` | `str \| None` | `None` |

#### FilePickerFile Properties
```python
file.path   # Full path to file
file.name   # Filename only
file.size   # Size in bytes
```

---

### 5. Naming Convention Updates

```python
# ❌ OLD (lowercase)
ft.colors.BLUE_400
ft.icons.FILE_OPEN
ft.border.all()

# ✅ NEW (capitalized)
ft.Colors.BLUE_400
ft.Icons.FILE_OPEN
ft.Border.all()
```

---

### 6. Deprecated Components

```python
# ❌ Deprecated
ft.ElevatedButton()
ft.app(target=main)
ft.FilePickerResultEvent

# ✅ Modern replacements
ft.Button()
ft.run(main)
# No event - use return values
```

---

## 📋 Complete Implementation Template

### Basic Single File Picker

```python
import flet as ft

def main(page: ft.Page):
    page.title = "File Picker Example"
    
    result_text = ft.Text("No file selected")
    
    async def pick_file_clicked(e):
        files = await file_picker.pick_files(
            allowed_extensions=["txt", "pdf", "png", "jpg"],
            dialog_title="Pick a file"
        )
        
        if files:
            file = files[0]
            result_text.value = f"Selected: {file.name}\nPath: {file.path}"
        else:
            result_text.value = "Selection cancelled"
        page.update()
    
    # Create FilePicker
    file_picker = ft.FilePicker()
    
    # Add to services (IMPORTANT!)
    page.services.append(file_picker)
    
    # Build UI
    page.add(
        ft.Button("Pick File", on_click=pick_file_clicked),
        result_text
    )

ft.run(main)
```

---

### Multiple File Selection

```python
async def pick_multiple_files(e):
    files = await file_picker.pick_files(
        allow_multiple=True,
        dialog_title="Pick multiple files"
    )
    
    if files:
        result = f"Selected {len(files)} files:\n"
        for file in files:
            result += f"  • {file.name} ({file.size} bytes)\n"
        result_text.value = result
    else:
        result_text.value = "No files selected"
    page.update()
```

---

### Directory Selection

```python
async def pick_directory(e):
    path = await directory_picker.get_directory_path(
        dialog_title="Choose a folder"
    )
    
    if path:
        result_text.value = f"Selected directory:\n{path}"
    else:
        result_text.value = "No directory selected"
    page.update()
```

---

### File Saving

```python
async def save_file(e):
    path = await save_picker.save_file(
        dialog_title="Save file as...",
        file_name="output.txt",
        allowed_extensions=["txt", "log", "md"]
    )
    
    if path:
        try:
            with open(path, 'w') as f:
                f.write("Your content here")
            result_text.value = f"File saved to:\n{path}"
        except Exception as ex:
            result_text.value = f"Error: {ex}"
    else:
        result_text.value = "Save cancelled"
    page.update()
```

---

## 🏗️ Project Structure Template

```
your-project/
├── main.py              # Main application
├── requirements.txt     # flet>=0.80.0
├── setup.sh            # Venv setup script
├── run.sh              # Launch script
└── README.md           # Documentation
```

### requirements.txt
```txt
flet>=0.80.0
```

### setup.sh
```bash
#!/bin/bash
python3 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r requirements.txt
echo "Setup complete!"
```

### run.sh
```bash
#!/bin/bash
.venv/bin/python main.py
```

---

## 🐛 Troubleshooting Guide

### Error: "Unknown control: FilePicker"

**Cause:** FilePicker added to overlay instead of services  
**Solution:**
```python
# Change this:
page.overlay.append(file_picker)

# To this:
page.services.append(file_picker)
```

---

### Error: "coroutine 'FilePicker.pick_files' was never awaited"

**Cause:** Forgot to use async/await  
**Solution:**
```python
# Change this:
def handler(e):
    file_picker.pick_files()

# To this:
async def handler(e):
    files = await file_picker.pick_files()
```

---

### Error: "module 'flet' has no attribute 'colors'"

**Cause:** Using old lowercase naming convention  
**Solution:**
```python
# Change this:
ft.colors.BLUE_400

# To this:
ft.Colors.BLUE_400
```

---

### Error: "FilePicker.__init__() got unexpected keyword argument 'on_result'"

**Cause:** Using old callback-based API  
**Solution:** Remove callbacks, use return values:
```python
# Change this:
file_picker = ft.FilePicker(on_result=handler)
file_picker.pick_files()

# To this:
file_picker = ft.FilePicker()
files = await file_picker.pick_files()
```

---

### Handler Not Being Called

**Cause:** Results now returned directly, not via callbacks  
**Solution:** Get return value and process it in the same handler:
```python
async def handler(e):
    files = await file_picker.pick_files()
    if files:
        # Process files here
        pass
```

---

## ✅ Best Practices

### 1. One FilePicker Per Operation Type
```python
file_picker = ft.FilePicker()        # For picking files
directory_picker = ft.FilePicker()    # For picking directories
save_picker = ft.FilePicker()         # For saving files
```

### 2. Always Check Return Values
```python
files = await file_picker.pick_files()
if files:  # User selected files
    # Process
else:  # User cancelled
    # Handle cancellation
```

### 3. Add FilePickers Before Building UI
```python
# Add to services first
page.services.append(file_picker)

# Then build UI
page.add(...)
```

### 4. Use Try-Except for File Operations
```python
try:
    with open(path, 'w') as f:
        f.write(content)
except Exception as ex:
    print(f"Error: {ex}")
```

---

## 📚 Complete Working Example

See `main.py` in this project for a complete, production-ready implementation featuring:
- ✅ Single and multiple file selection
- ✅ Directory selection
- ✅ File saving with content
- ✅ Timestamped logging
- ✅ Error handling
- ✅ Status updates
- ✅ Modern Flet 0.80+ API

---

## 🔗 Resources

- **Flet Docs:** https://flet.dev
- **Flet GitHub:** https://github.com/flet-dev/flet
- **Flet Discord:** https://discord.gg/dzWXP8SHG8
- **This Template:** Use as reference for any Flet FilePicker implementation

---

**Template Version:** 1.0  
**Flet Version:** 0.80.1  
**Last Updated:** January 2026  
**Status:** ✅ Tested and Working
