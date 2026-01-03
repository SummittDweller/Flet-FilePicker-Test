# Flet 0.80+ FilePicker - Quick Reference Card

## 🚀 Essential Setup

```python
import flet as ft

def main(page: ft.Page):
    # Create FilePicker
    file_picker = ft.FilePicker()
    
    # Add to services (NOT overlay!)
    page.services.append(file_picker)
    
    # Handler must be async
    async def pick_file(e):
        files = await file_picker.pick_files()
        if files:
            print(files[0].path)
    
    page.add(ft.Button("Pick", on_click=pick_file))

ft.run(main)
```

---

## 📖 Method Signatures

### Pick Files
```python
files = await file_picker.pick_files(
    dialog_title="Pick files",              # Optional
    initial_directory="/path/to/start",     # Optional
    allowed_extensions=["txt", "pdf"],      # Optional
    allow_multiple=True                      # Default: False
)
# Returns: list[FilePickerFile] (empty list if cancelled)
```

### Get Directory
```python
path = await picker.get_directory_path(
    dialog_title="Choose folder",           # Optional
    initial_directory="/path/to/start"      # Optional
)
# Returns: str | None (None if cancelled)
```

### Save File
```python
path = await picker.save_file(
    dialog_title="Save as...",              # Optional
    file_name="output.txt",                 # Optional
    initial_directory="/path/to/start",     # Optional
    allowed_extensions=["txt", "log"]       # Optional
)
# Returns: str | None (None if cancelled)
```

---

## 📦 FilePickerFile Properties

```python
file.path   # "/full/path/to/file.txt"
file.name   # "file.txt"
file.size   # 1024 (bytes)
```

---

## ⚡ Common Patterns

### Single File
```python
async def handler(e):
    files = await picker.pick_files()
    if files:
        print(files[0].path)
```

### Multiple Files
```python
async def handler(e):
    files = await picker.pick_files(allow_multiple=True)
    for file in files:
        print(file.name)
```

### With Extensions
```python
files = await picker.pick_files(
    allowed_extensions=["jpg", "png", "gif"]
)
```

### Save & Write
```python
path = await picker.save_file(file_name="output.txt")
if path:
    with open(path, 'w') as f:
        f.write("content")
```

---

## ❌ Common Mistakes

| Wrong | Right |
|-------|-------|
| `page.overlay.append(picker)` | `page.services.append(picker)` |
| `def handler(e):` | `async def handler(e):` |
| `picker.pick_files()` | `await picker.pick_files()` |
| `ft.colors.BLUE` | `ft.Colors.BLUE` |
| `ft.ElevatedButton` | `ft.Button` |
| `ft.app(target=main)` | `ft.run(main)` |

---

## 🔍 Key Differences from Old API

| Flet <0.80 | Flet 0.80+ |
|------------|------------|
| Callback-based | Return-value based |
| `on_result` parameter | Direct `await` return |
| `FilePickerResultEvent` | `list[FilePickerFile]` or `str` |
| Control (overlay) | Service (services) |
| Sync methods | Async methods |

---

**Remember:** 
- ✅ Use `page.services`
- ✅ Make handlers `async`
- ✅ Use `await` on methods
- ✅ Check return values
- ✅ Capitalize: `Colors`, `Icons`, `Border`
