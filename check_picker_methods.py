import flet as ft
import asyncio

async def test_picker():
    page = ft.Page()
    
    fp = ft.FilePicker()
    
    # Check what pick_files returns
    print("Testing pick_files return value...")
    import inspect
    sig = inspect.signature(fp.pick_files)
    print(f"pick_files signature: {sig}")
    print(f"pick_files is coroutine function: {inspect.iscoroutinefunction(fp.pick_files)}")
    
    # Check get_directory_path
    sig2 = inspect.signature(fp.get_directory_path)
    print(f"\nget_directory_path signature: {sig2}")
    
    # Check save_file
    sig3 = inspect.signature(fp.save_file)
    print(f"\nsave_file signature: {sig3}")

asyncio.run(test_picker())
