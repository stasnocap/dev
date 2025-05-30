xrandr --output DP-0 --mode 3440x1440 --rate 144
source $HOME/dev/xkb/add-to-rc-file
while true; do
    xsetroot -name "$(date)"
    sleep 2
done &
exec dwm
