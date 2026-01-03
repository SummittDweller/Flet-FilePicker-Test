#!/bin/bash
# Create macOS ICNS icon from PNG

# Create iconset directory
mkdir -p app_icon.iconset

# Copy and resize the icon to all required sizes
sips -z 16 16     app_icon.png --out app_icon.iconset/icon_16x16.png
sips -z 32 32     app_icon.png --out app_icon.iconset/icon_16x16@2x.png
sips -z 32 32     app_icon.png --out app_icon.iconset/icon_32x32.png
sips -z 64 64     app_icon.png --out app_icon.iconset/icon_32x32@2x.png
sips -z 128 128   app_icon.png --out app_icon.iconset/icon_128x128.png
sips -z 256 256   app_icon.png --out app_icon.iconset/icon_128x128@2x.png
sips -z 256 256   app_icon.png --out app_icon.iconset/icon_256x256.png
sips -z 512 512   app_icon.png --out app_icon.iconset/icon_256x256@2x.png
sips -z 512 512   app_icon.png --out app_icon.iconset/icon_512x512.png
cp app_icon.png app_icon.iconset/icon_512x512@2x.png

# Convert to ICNS
iconutil -c icns app_icon.iconset -o app_icon.icns

# Clean up
rm -rf app_icon.iconset

echo "ICNS icon created: app_icon.icns"
