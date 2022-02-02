@ECHO OFF 
ECHO ==========================
20:14 24-01-2022
mkdir continers
cd containers
xcopy \\wsl$\docker-desktop-data\version-pack-data\community\docker\containers . /E/H/C/I

PAUSE