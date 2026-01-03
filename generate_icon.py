#!/usr/bin/env python3
"""
Generate a simple rocket icon for the Flet app
"""
from PIL import Image, ImageDraw, ImageFont
import os

# Create a 512x512 image with transparent background
size = 512
img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Draw a simple rocket shape
# Background circle
circle_color = (41, 98, 255, 255)  # Blue
draw.ellipse([50, 50, size-50, size-50], fill=circle_color)

# Rocket body (white)
rocket_points = [
    (size//2, 100),  # Top point
    (size//2 - 60, 400),  # Bottom left
    (size//2 + 60, 400),  # Bottom right
]
draw.polygon(rocket_points, fill=(255, 255, 255, 255))

# Rocket fins
left_fin = [(size//2 - 60, 400), (size//2 - 120, 450), (size//2 - 60, 350)]
right_fin = [(size//2 + 60, 400), (size//2 + 120, 450), (size//2 + 60, 350)]
draw.polygon(left_fin, fill=(255, 200, 0, 255))  # Orange
draw.polygon(right_fin, fill=(255, 200, 0, 255))

# Window (circle)
window_center = (size//2, 220)
window_radius = 30
draw.ellipse([
    window_center[0] - window_radius,
    window_center[1] - window_radius,
    window_center[0] + window_radius,
    window_center[1] + window_radius
], fill=(100, 200, 255, 255))  # Light blue

# Flame (bottom)
flame_points = [
    (size//2, 450),  # Bottom point
    (size//2 - 40, 400),
    (size//2, 420),
    (size//2 + 40, 400),
]
draw.polygon(flame_points, fill=(255, 100, 0, 255))  # Red-orange

# Save as PNG
script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, 'app_icon.png')
img.save(icon_path)
print(f"Icon saved to: {icon_path}")

# Also save smaller sizes for various uses
for size_px in [256, 128, 64, 32]:
    small_img = img.resize((size_px, size_px), Image.Resampling.LANCZOS)
    small_path = os.path.join(script_dir, f'app_icon_{size_px}.png')
    small_img.save(small_path)
    print(f"Icon saved to: {small_path}")
