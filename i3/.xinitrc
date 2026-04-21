
#!/bin/bash

# 关键：强制指定 DISPLAY
export DISPLAY=:2

unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS

xsetroot -solid grey
vncconfig -nowin &

# 一定要加 dbus-launch
exec dbus-launch --exit-with-session i3
