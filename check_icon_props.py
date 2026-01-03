import flet as ft

# Check Page properties
page_attrs = [a for a in dir(ft.Page) if 'icon' in a.lower() or 'window' in a.lower()]
print("Page attributes with 'icon' or 'window':")
for attr in page_attrs:
    print(f"  {attr}")

# Check if there's a specific icon property
print("\n\nChecking ft namespace for icon/window related:")
ft_attrs = [a for a in dir(ft) if 'icon' in a.lower() or 'window' in a.lower()]
for attr in ft_attrs[:20]:
    print(f"  {attr}")
