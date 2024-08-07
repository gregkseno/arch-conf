from libqtile import bar as qtile_bar
from libqtile import widget

from utils.colors import colors

group_box_widget = widget.GroupBox(
    active=colors.white,
    inactive=colors.white,
    disable_drag=True,
    rounded=True,
    highlight_method="text",
    this_current_screen_border=colors.black,
    this_screen_border=colors.black,
    other_current_screen_border=colors.white,
    other_screen_border=colors.white,
    urgent_alert_method="line",
    urgent_border=colors.red
)

sep_widget = widget.Sep(
    linewidth=2,
    size_percent=45,
    padding=10,
    foreground=colors.foreground
)

# kbd_widget = widget.KeyboardKbdd(
#     configured_keyboards=['us', 'ru'],
# )

upd_widget = widget.CheckUpdates(
    dsitro='Arch_checkupdates',
    colour_have_updates=colors.red,
    no_update_string='No updates',
    colour_no_updates=colors.white
)

vol_widget = widget.Volume(
    fmt="Volume: {}",
    scroll_delay=0
)

power_widget = widget.WidgetBox(
    widgets=[
        widget.LaunchBar(_progs=[
            ('󰤄 ', 'systemctl suspend'),
            (' ', 'systemctl reboot'),
            (' ', 'systemctl poweroff')
        ])
    ],
    close_button_location='right',
    text_open='   ',
    text_closed='   ',
)


widgets = [
    group_box_widget,
    widget.Prompt(),
    widget.Spacer(),
    widget.Clock(format="%d.%m.%Y %H:%M"),
    widget.Spacer(),
    widget.Systray(),
    sep_widget,
    upd_widget,
    sep_widget,
    # kbd_widget,
    # widget.Wlan(format="{essid} {percent:2.0%}", update_interval=5),
    sep_widget,
    vol_widget,
    sep_widget,
    # widget.Battery(format="🔋 {percent:2.0%} ", update_interval=5),
    power_widget
]

bar = qtile_bar.Bar(widgets, 36, opacity=0.85, margin=[5, 5, 0, 5])
