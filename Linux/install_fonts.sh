# introduce the program
# This script installs TrueType fonts from a specified directory to the system fonts directory on Linux.
# The script assumes that the TrueType fonts are stored in a directory named "fonts" in the same directory as the script.
# The script will copy all TrueType font files with a ".ttf" extension from the "fonts" directory to the system fonts directory (/usr/share/fonts/truetype/).
# The script will then update the font cache to make the new fonts available to the system.
# The script requires sudo privileges to copy files to the system fonts directory and update the font cache.
# The script should be run from the same directory as the "fonts" directory containing the TrueType font files.
# The script can be run by executing the following command in the terminal: bash install_fonts.sh
# The script can be modified to specify a different directory for the TrueType fonts by changing the "fonts_dir" variable.

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
