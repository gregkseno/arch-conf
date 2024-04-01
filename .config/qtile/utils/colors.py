from dataclasses import dataclass


def to_alacrtty():
    """Applies color palette to alacrtty config"""
    from toml import load as load_toml
    from toml import dump as write_toml
    from utils.config import alacritty_path
    
    with open(alacritty_path, "w") as file:
        alacritty_toml = load_toml(file)

        alacritty_toml['colors']['normal']['background'] = BiscuitDark.background
        alacritty_toml['colors']['normal']['foreground'] = BiscuitDark.foreground
        alacritty_toml['colors']['normal']['black'] =  BiscuitDark.black
        alacritty_toml['colors']['normal']['red'] = BiscuitDark.red
        alacritty_toml['colors']['normal']['green'] = BiscuitDark.green
        alacritty_toml['colors']['normal']['yellow'] = BiscuitDark.yellow
        alacritty_toml['colors']['normal']['blue'] = BiscuitDark.blue
        alacritty_toml['colors']['normal']['magenta'] = BiscuitDark.magenta
        alacritty_toml['colors']['normal']['cyan'] = BiscuitDark.cyan
        alacritty_toml['colors']['normal']['white'] = BiscuitDark.white

        alacritty_toml['colors']['bright']['background'] = BiscuitLight.background
        alacritty_toml['colors']['bright']['foreground'] = BiscuitLight.foreground
        alacritty_toml['colors']['bright']['black'] = BiscuitLight.black
        alacritty_toml['colors']['bright']['red'] = BiscuitLight.red
        alacritty_toml['colors']['bright']['green'] = BiscuitLight.green
        alacritty_toml['colors']['bright']['yellow'] = BiscuitLight.yellow
        alacritty_toml['colors']['bright']['blue'] = BiscuitLight.blue
        alacritty_toml['colors']['bright']['magenta'] = BiscuitLight.magenta
        alacritty_toml['colors']['bright']['cyan'] = BiscuitLight.cyan
        alacritty_toml['colors']['bright']['white'] = BiscuitLight.white
   
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
    background = "#1A1515"
    foreground = "#DCC9BC"

    black = "#2D2424"
    red = "#CF223E"
    green = "#959A6B"
    yellow = "#E39C45"
    blue = "#614F76"
    magenta = "#AE3F82"
    cyan = "#756D94"
    white = "#FFE9C7"

@dataclass(frozen=True)
class BiscuitLight:
    background = "#A38A8A"
    foreground = "#483939"

    black = "#C1AEAE"
    red = "#AE4750"
    green = "#97916F"
    yellow = "#CD9165"
    blue = "#83546B"
    magenta = "#A05A78"
    cyan = "#79657A "
    white = "#2D2424"


colors = Biscuit()
