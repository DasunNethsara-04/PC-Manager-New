#!/bin/bash

# Path to the fonts directory
fonts_dir="./fonts"

# Check if the fonts directory exists
if [ ! -d "$fonts_dir" ]; then
    echo "Fonts directory not found."
    exit 1
fi

# Loop through each file in the fonts directory
for file in "$fonts_dir"/*.ttf; do
    # Check if the file is a TrueType font
    if [ "${file: -4}" == ".ttf" ]; then
        # Copy the font file to the system fonts directory
        sudo cp "$file" "/usr/share/fonts/truetype/"
    fi
done

# Update font cache
sudo fc-cache -f -v
