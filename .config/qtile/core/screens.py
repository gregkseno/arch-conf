from libqtile.config import Screen

from core.bar import bar
from utils.config import wallpapers_path

screens = [
    Screen(
        top=bar,
        wallpaper=wallpapers_path,
        wallpaper_mode='stretch',
    ),
]