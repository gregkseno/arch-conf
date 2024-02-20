# Arch Linux configuration
My personal Arch Linux configuration

## LightDM
To move `.Xauthority` file from `$HOME` change `$XAUTHORITY` env variable.

Add `XAUTHORITY=~/.config/Xauthority` to `/etc/environment`

## I/O configuration
### Keyboard configuration
Add to `/etc/X11/xorg.conf.d/` file `00-keyboard.conf`
```
Section "InputClass"
	Identifier "system-keyboard"
	MatchIsKeyboard "on"
	Option "XkbLayout" "us,ru"
	Option "XkbOptions" "grp:win_space_toggle"
EndSection
```
### Mouse configuration
Add to `/etc/X11/xorg.conf.d/` file `10-mouse.conf`
```
Section "InputClass"
	Identifier "My Mouse"
	MatchIsPointer "yes"
	Option "AccelerationNumerator" "1"
	Option "AccelerationDenominator" "1"
	Option "AccelerationThreshold" "0"
EndSection
```

## Emoji fix
To fix squares instead of emoji/symbols install font listed [here](https://wiki.archlinux.org/title/Fonts#Emoji_and_symbols)

## Dependencies
1. pywal -- for auto coloring WM
2. toml -- configuration of alacritty (to change colors in config)
