if [ -d "/usr/share/WallChanger" ]; then
    rm -r /usr/share/WallChanger && rm /usr/share/applications/WallChanger.desktop
fi
cp -r WallChanger /usr/share && cp WallChanger.desktop /usr/share/applications

