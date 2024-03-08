.. sectnum::

Arch Linux configuration
========================

.. contents:: Table of Contents

My personal Arch Linux configuration


I/O configuration
-----------------

Keyboard configuration
~~~~~~~~~~~~~~~~~~~~~~

Add to ``/etc/X11/xorg.conf.d/`` file ``00-keyboard.conf``

::

   Section "InputClass"
       Identifier "system-keyboard"
       MatchIsKeyboard "on"
       Option "XkbLayout" "us,ru"
       Option "XkbOptions" "grp:win_space_toggle"
   EndSection

Mouse configuration
~~~~~~~~~~~~~~~~~~~

Add to ``/etc/X11/xorg.conf.d/`` file ``10-mouse.conf``

::

   Section "InputClass"
       Identifier "My Mouse"
       MatchIsPointer "yes"
       Option "AccelerationNumerator" "1"
       Option "AccelerationDenominator" "1"
       Option "AccelerationThreshold" "0"
   EndSection

Emoji fix
---------

To fix squares instead of emoji/symbols install font listed
`here <https://wiki.archlinux.org/title/Fonts#Emoji_and_symbols>`__

Dependencies
------------

1. pywal -- for auto coloring WM
2. toml -- configuration of alacritty (to change colors in config)

Intstallation Guide
-------------------

Additionally check `official Arch installation
guide <https://wiki.archlinux.org/title/installation_guide>`__

Connect to the Internet
~~~~~~~~~~~~~~~~~~~~~~~

To set up a network connection in the live environment, firstly ensure your network interface is listed and enabled, for example with ``ip link``. 
Then follow desired connection type `Wi-Fi`_ or `Ethernet`_.

Ethernet
^^^^^^^^

Plug in the Ethernet cable.

Wi-Fi
^^^^^

Authenticate to the wireless network using ``iwctl``:

-  check device name, list all Wi-Fi devices

   .. code::

      [iwd]# device list

-  if the device or its corresponding adapter is turned off, turn it on

   .. raw:: html

      <div><pre>[iwd]# device <i>device</i> set-property Powered on
      [iwd]# adapter <i>adapter</i> set-property Powered on<pre><div>

-  scan for networks and list all available

   .. raw:: html

      <div><pre>[iwd]# station <i>device</i> scan
      [iwd]# station <i>device</i> get-networks<pre><div>

   .. note::

      If networks list is empty, turn off then on the *adapter* and *device*

-  connect to a network
  
   .. raw:: html

      <div><pre>[iwd]# station <i>device</i> connect <i>SSID</i><pre><div>

System clock
~~~~~~~~~~~~
Use ``timedatectl`` to ensure the system clock is accurate.

Disk partitioning
~~~~~~~~~~~~~~~~~

Check disred *disk* name using ``lsblk``

To make partitioning:
- run ``cfdisk``
- free space on disidred *disk* 
- modify partition tables according to the table (UEFI with GPT)
- format newly created partitions according to the table (UEFI with GPT) 

+---------------------+---------------+-------------------------+------------------------------+
|| Mount point on the || Partition    || Size                   || Format                      |
|| installed system   ||              ||                        ||                             |
+=====================+===============+=========================+==============================+
| ``/boot``           | ``/dev/sda1`` | 1 GiB                   | ``mkfs.fat -F 32 /dev/sda1`` |
+---------------------+---------------+-------------------------+------------------------------+
| ``[SWAP]``          | ``/dev/sda2`` | 4-8 GiB                 | ``mkswap /dev/sda2``         |
+---------------------+---------------+-------------------------+------------------------------+
| ``/``               | ``/dev/sda3`` | Remainder of the device | ``mkfs.ext4 /dev/sda3``      |
+---------------------+---------------+-------------------------+------------------------------+


Mount the file systems
~~~~~~~~~~~~~~~~~~~~~~

Mount the root volume to ``/mnt``

.. code::

   # mount /dev/sda3 /mnt

Mount the EFI system partition

.. code::

   # mount --mkdir /dev/sda1 /mnt/boot

Enable swap with

.. code::

   # swapon /dev/sda2

Install main packages
~~~~~~~~~~~~~~~~~~~~~

Before installing packages check add new suitable mirrors to ``/etc/pacman.d/mirrorlist``

.. code::

   # cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.backup
   # curl -s "https://archlinux.org/mirrorlist/?country=RU&protocol=https&use_mirror_status=off" | sed -e 's/^#Server/Server/' -e '/^#/d' > /etc/pacman.d/mirrorlist

Install packages

.. code::

   # pacstrap -K /mnt base linux linux-firmware base-devel grub efibootmgr neovim networkmanager sof-firmware man-db zsh stow git

Configure the system
~~~~~~~~~~~~~~~~~~~~

-  generate an fstab file

   .. code::

      # genfstab -U /mnt > /mnt/etc/fstab

-  change root into the new system

   .. code::

      # arch-chroot /mnt

-  set up time:

   -  select time zone from ``timedatectl list-timezones`` and set it

      .. raw:: html

         <div><pre># ln -sf /usr/share/zoneinfo/<i>Region</i>/<i>City</i> /etc/localtime</pre></div>

   -  generate ``/etc/adjtime``

      .. code::

         # hwclock --systohc

-  set up localization:
  
   -  edit ``/etc/locale.gen`` and uncomment ``en_US.UTF-8 UTF-8`` and other needed UTF-8 locales
   -  generate the locales

      .. code::

         # locale-gen
   
   -  create the ``/etc/locale.conf`` file, and set the ``LANG`` variable accordingly

      .. code::

         LANG=en_US.UTF-8

-  set up network configuration by creating the hostname file ``/etc/hostname`` and adding *yourhostname*
-  set ``root`` password by running ``passwd``
-  add user and it's password

   .. code::

      useradd -m -G wheel -s /bin/zsh greg
      passwd greg

-  install GRUB 

   .. code::

      grub-install --efi-directory=/boot --bootloader-id=grub
      grub-mkconfig -o /boot/grub/grub.cfg

-  enable services/deamons

   .. code::

      systemctl enable NetworkManager

Post-installation
~~~~~~~~~~~~~~~~~

ZSH
^^^

Download oh-my-zsh:

.. code:: 

   ~$ sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
   ~$ rm .zshrc .zshrc.pre-oh-my-zsh

Instal plugins:

.. code:: 

   ~# pacman -S zsh-syntax-highlighting zsh-autosuggestions zsh-theme-powerlevel10k
   ~$ git clone https://github.com/jeffreytse/zsh-vi-mode $ZSH_CUSTOM/plugins/zsh-vi-mode

LightDM
^^^^^^^

Install LightDM:

.. code:: 

   ~# pacman -S lightdm lightdm-gtk-greeter
   ~# systemctl enable lightdm

To move ``.Xauthority`` file from ``$HOME`` change ``$XAUTHORITY`` env
variable.

Add ``XAUTHORITY=~/.config/Xauthority`` to ``/etc/environment``

Qtile
^^^^^

Firstly, install Xorg:

.. code:: 

   ~# pacman -S xorg

Install Qtile:

.. code:: 

   ~# pacman -S qtile python-pywal python-toml picom

Add wallpaper to ~/Pictures/Wallpaper

Configuration install
^^^^^^^^^^^^^^^^^^^^^

To import my config files follow the steps:

.. code::

   ~$ mkdir .dotfiles
   ~$ cd .dotfiles
   ~$ git clone https://github.com/gregkseno/arch-conf.git
   ~$ mv -f arch-conf/{.,}* .
   ~$ rmdir arch-conf
   ~$ stow .









ntfs-3g