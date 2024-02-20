# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import extension
from libqtile.log_utils import logger

import pywal
from toml import load as load_toml
from toml import dump as write_toml

wallpapers_path = '/home/greg/Pictures/Wallpapers/anime-face.png'
alacritty_config = "/home/greg/.config/alacritty/alacritty.toml" 

def load_colors(wallpapers_path): 
    image = pywal.image.get(wallpapers_path)
    colors_dict = pywal.colors.get(image, backend="colorz", sat="0.3")
    wallpaper_path = colors_dict['wallpaper']
    colors = list(colors_dict['colors'].values())

    with open(alacritty_config, "r") as file:
        alacritty_toml = load_toml(file)

    for i, color in enumerate(alacritty_toml['colors']['normal'].keys()):
        alacritty_toml['colors']['normal'][color] = colors[:8][i]
        alacritty_toml['colors']['bright'][color] = colors[8:][i]
   
    with open(alacritty_config, "w") as file:
        write_toml(alacritty_toml, file)
    lazy.spawn('~/.config/qtile/alacritty_colors.sh ~/.config/alacritty/alacritty.toml')
    return wallpaper_path, colors[:8], colors[:8] 

@hook.subscribe.startup_once
def autostart():  
    autostart_path = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([autostart_path])

wallpaper_path, colors, _ = load_colors(wallpapers_path)
mod = "mod4"
terminal = guess_terminal()

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "x", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "q", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "d", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod, "shift"], "s", lazy.spawn("scrot /home/greg/Pictures/Screenshots/%Y-%m-%d-%T-screenshot.png --select"), desc="Takes screenshot"),
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle floating"),
]

groups = [Group("main"),
          Group("term"),
          Group("web", matches=[Match(wm_class="firefox")])]

for i, group in enumerate(groups):
    keys.extend(
[
            Key(
                [mod],
                str(i + 1),
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            Key(
                [mod, "shift"],
                str(i + 1),
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            )
            ]
    )

layout_theme = {
    "margin": 5,
    "border_focus": colors[3],
    "border_normal": colors[0],
    "font": "Source Code Pro Semibold",
    "grow_amount": 2,
}
layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
]

widget_defaults = dict(
    font="Source Code Pro Semibold",
    fontsize=16,
    padding=4,
    background=colors[0],
    foreground=colors[7]
)

extension_defaults = widget_defaults.copy()

group_box_settings = {
    "active": colors[1],
    "inactive": colors[1],
    "disable_drag": True,
    "rounded": True,
    "highlight_method": "text",
    "this_current_screen_border": colors[7],
    "this_screen_border": colors [7],
    "other_current_screen_border": colors[1],
    "other_screen_border": colors[1],
    "urgent_alert_method": "line",
    "urgent_border": colors[1]
}
sep_settings = {
    "linewidth": 2,
    "size_percent": 45,
    "padding": 10,
    "foreground": colors[3]
}
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(**group_box_settings),
                widget.Prompt(),
                widget.Spacer(),
                widget.Clock(format="%d.%m.%Y %H:%M"),
                widget.Spacer(),
                widget.CheckUpdates(dsitro='Arch', colour_have_updates=colors[2], no_update_string='No updates', colour_no_updates=colors[1]),
                # widget.Sep(linewidth=2, size_percent=45, padding=10),
                # widget.Wlan(format="{essid} {percent:2.0%}", update_interval=5),
                widget.Sep(**sep_settings),
                widget.Volume(fmt="Volume: {}"),
                widget.Sep(**sep_settings),
                # widget.Battery(format="🔋 {percent:2.0%} ", update_interval=5),
                widget.WidgetBox(widgets=[
    		widget.LaunchBar(_progs=[('󰤄 ', 'systemctl suspend'), (' ', 'systemctl reboot'), (' ', 'systemctl poweroff')])
                    ],
                    close_button_location='right', text_open='   ', text_closed='   ',
                )
            ],
            36,
            opacity=0.85,
            margin=[5, 5, 0, 5],
            # background=colors[7],
            # border_color=colors[7]
        ),
        wallpaper=wallpaper_path,
        wallpaper_mode='stretch',
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    **layout_theme
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "Qtile"
