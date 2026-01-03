import flet as ft
import inspect

# Check FilePicker methods without creating a page
fp_class = ft.FilePicker

print("pick_files signature:")
sig = inspect.signature(fp_class.pick_files)
print(f"  {sig}")
print(f"  Return annotation: {sig.return_annotation}")

print("\nget_directory_path signature:")
sig2 = inspect.signature(fp_class.get_directory_path)
print(f"  {sig2}")
print(f"  Return annotation: {sig2.return_annotation}")

print("\nsave_file signature:")
sig3 = inspect.signature(fp_class.save_file)
print(f"  {sig3}")
print(f"  Return annotation: {sig3.return_annotation}")
