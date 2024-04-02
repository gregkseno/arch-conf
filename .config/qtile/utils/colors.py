from dataclasses import dataclass


def to_alacrtty():
    """Applies color palette to alacrtty config"""
    from toml import load as load_toml
    from toml import dump as write_toml
    from utils.config import alacritty_path
    
    with open(alacritty_path, "r") as file:
        alacritty_toml = load_toml(file)

    alacritty_toml['colors']['normal']['black'] =  BiscuitDark.black
    alacritty_toml['colors']['normal']['red'] = BiscuitDark.red
    alacritty_toml['colors']['normal']['green'] = BiscuitDark.green
    alacritty_toml['colors']['normal']['yellow'] = BiscuitDark.yellow
    alacritty_toml['colors']['normal']['blue'] = BiscuitDark.blue
    alacritty_toml['colors']['normal']['magenta'] = BiscuitDark.magenta
    alacritty_toml['colors']['normal']['cyan'] = BiscuitDark.cyan
    alacritty_toml['colors']['normal']['white'] = BiscuitDark.white

    alacritty_toml['colors']['bright']['black'] = BiscuitLight.black
    alacritty_toml['colors']['bright']['red'] = BiscuitLight.red
    alacritty_toml['colors']['bright']['green'] = BiscuitLight.green
    alacritty_toml['colors']['bright']['yellow'] = BiscuitLight.yellow
    alacritty_toml['colors']['bright']['blue'] = BiscuitLight.blue
    alacritty_toml['colors']['bright']['magenta'] = BiscuitLight.magenta
    alacritty_toml['colors']['bright']['cyan'] = BiscuitLight.cyan
    alacritty_toml['colors']['bright']['white'] = BiscuitLight.white
             
    with open(alacritty_path, "w") as file:
        write_toml(alacritty_toml, file)



# https://github.com/catppuccin/catppuccin#-palette
# Mocha
@dataclass(frozen=True)
class Catppuccin:
    rosewater = "#f5e0dc"
    flamingo  = "#f2cdcd"
    pink      = "#f5c2e7"
    mauve     = "#cba6f7"
    red       = "#f38ba8"
    maroon    = "#eba0ac"
    peach     = "#fab387"
    yellow    = "#f9e2af"
    green     = "#a6e3a1"
    teal      = "#94e2d5"
    sky       = "#89dceb"
    sapphire  = "#74c7ec"
    blue      = "#89b4fa"
    lavender  = "#b4befe"
    text      = "#cdd6f4"
    subtext1  = "#bac2de"
    subtext0  = "#a6adc8"
    overlay2  = "#9399b2"
    overlay1  = "#7f849c"
    overlay0  = "#6c7086"
    surface2  = "#585b70"
    surface1  = "#45475a"
    surface0  = "#313244"
    base      = "#1e1e2e"
    mantle    = "#181825"
    crust     = "#11111b"

# https://github.com/Biscuit-Colorscheme/biscuit?tab=readme-ov-file#-colors
@dataclass(frozen=True)
class BiscuitDark:
    background = "#1a1515"
    foreground = "#dcc9bc"

    black = "#2d2424"
    red = "#cf223e"
    green = "#959a6b"
    yellow = "#e39c45"
    blue = "#614f76"
    magenta = "#ae3f82"
    cyan = "#756d94"
    white = "#ffe9c7"

@dataclass(frozen=True)
class BiscuitLight:
    background = "#a38a8a"
    foreground = "#483939"

    black = "#c1aeae"
    red = "#ae4750"
    green = "#97916f"
    yellow = "#cd9165"
    blue = "#83546b"
    magenta = "#a05a78"
    cyan = "#79657a"
    white = "#2d2424"


colors = BiscuitDark()
