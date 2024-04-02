from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy

from core.keys import keys, mod


groups: list[Group] = []

for key, label, matches in [
    ("1", "", Match(wm_class="code")),
    ("2", "", Match(wm_class="Alacritty")),
    ("3", "󰈹", Match(wm_class=["google-chrome", "firefox"])),
    ("w", "󰇮", Match(wm_class=["discord", "telegram-desktop"])),
    ("e", "", Match(wm_class="spotify")),
]:
    groups.append(Group(key, matches, label=label))

    keys.extend([
        Key([mod], key, lazy.group[key].toscreen(toggle=True), desc=f"Switch to group {groups[-1].name}"),
        Key([mod, "shift"], key, lazy.window.togroup(key), desc=f"Switch to & move focused window to group {groups[-1].name}"),
    ]) 
