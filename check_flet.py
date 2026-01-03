import flet as ft

# Check for FilePicker
print("FilePicker exists:", hasattr(ft, 'FilePicker'))

# Check for file-related attributes
file_attrs = [attr for attr in dir(ft) if 'file' in attr.lower()]
print("\nFile-related attributes:", file_attrs)

# Check for picker-related attributes  
pick_attrs = [attr for attr in dir(ft) if 'pick' in attr.lower()]
print("\nPicker-related attributes:", pick_attrs)

# Check version
print("\nFlet version:", ft.__version__ if hasattr(ft, '__version__') else "Unknown")
