xrandr --output DP-0 --mode 3440x1440 --rate 144

xset -dpms
xset s off

xsetroot -solid "#eff1f5"
source $HOME/personal/dev/xkb/add-to-rc-file
while true; do
    xsetroot -name "$(date)"
    sleep 2
done &
exec dwm
