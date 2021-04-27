if [ -d "$HOME/.local/share/WallChanger" ]; then
    rm -r $HOME/.local/share/WallChanger && rm $HOME/.local/share/applications/WallChanger.desktop
fi

echo Path=$HOME/.local/share/WallChanger >> WallChanger.desktop

cp -r WallChanger $HOME/.local/share && cp WallChanger.desktop $HOME/.local/share/applications

