import flet as ft

# Check FilePicker attributes
fp = ft.FilePicker()
print("FilePicker attributes with 'result' or 'on':")
attrs = [a for a in dir(fp) if 'result' in a.lower() or (a.startswith('on_') and not a.startswith('_'))]
print(attrs)

# Check all on_ attributes
print("\nAll 'on_' attributes:")
on_attrs = [a for a in dir(fp) if a.startswith('on_')]
print(on_attrs)

print("\nFilePicker __init__ signature:")
import inspect
print(inspect.signature(ft.FilePicker.__init__))
