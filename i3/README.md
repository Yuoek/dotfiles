# i3-config

## package
```bash
yay -Sy tigervnc xorg i3-wm dbus
```
```
sudo pacman -S xorg lightdm lightdm-gtk-greeter i3-wm i3lock i3status i3blocks dmenu xfce4-terminal
yay -S feh
```

## .xinitrc
```makrdown
#!/bin/bash

# 关键：强制指定 DISPLAY
export DISPLAY=:2

unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS

xsetroot -solid grey
vncconfig -nowin &

# 一定要加 dbus-launch
exec dbus-launch --exit-with-session i3

```

## .vnc/config
```markdown
#!/bin/bash
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
exec dbus-launch --exit-with-session i3
```
