if [ -d "$HOME/.local/share/WallChanger" ]; then
    rm -r $HOME/.local/share/WallChanger
    rm $HOME/.local/share/applications/WallChanger.desktop
    rm $HOME/.config/autostart/wcautostart.desktop
fi


cp -r WallChanger $HOME/.local/share
cp WallChanger.desktop $HOME/.local/share/applications
cp wcautostart.desktop $HOME/.config/autostart

echo Path=$HOME/.local/share/WallChanger >> $HOME/.local/share/applications/WallChanger.desktop
echo Path=$HOME/.local/share/WallChanger >> $HOME/.config/autostart/wcautostart.desktop
