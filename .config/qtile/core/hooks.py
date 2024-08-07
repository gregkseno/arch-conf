import os
import subprocess

from libqtile import hook


@hook.subscribe.startup_once
def autostart():  
    autostart_path = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([autostart_path])