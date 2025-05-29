source $HOME/dev/xkb/add-to-rc-file
while true; do
    xsetroot -name "$(date)"
    sleep 2
done &
exec dwm
