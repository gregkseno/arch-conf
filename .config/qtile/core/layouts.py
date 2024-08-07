from libqtile import layout
from libqtile.config import Match
from utils.colors import colors

layout_theme = {
    "margin": 5,
    "border_focus": colors.foreground,
    "border_normal": colors.background,
    "font": "Source Code Pro Semibold",
    "grow_amount": 2,
}

layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
]

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
