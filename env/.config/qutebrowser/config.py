from qutebrowser.config.configfiles import ConfigAPI
from qutebrowser.config.config import ConfigContainer
config: ConfigAPI = config # pyright: ignore[reportUndefinedVariable]
c: ConfigContainer = c # pyright: ignore[reportUndefinedVariable]

config.load_autoconfig()

config.bind('n', 'scroll left')
config.bind('e', 'scroll down')
config.bind('u', 'scroll up')
config.bind('i', 'scroll right')

config.bind('N', 'back')
config.bind('E', 'tab-next')
config.bind('U', 'tab-prev')
config.bind('I', 'forward')

config.bind('j', 'scroll-page 0 -0.5')
config.bind('m', 'scroll-page 0 0.5')

config.bind('x', 'tab-close')
config.bind('z', 'undo')

config.bind('k', 'search-next')
config.bind('K', 'search-prev')

config.bind('cD', 'yank domain -s')
config.bind('cM', 'yank inline [{title}]({url:yank}) -s')
config.bind('cP', 'yank pretty-url -s')
config.bind('cT', 'yank title -s')
config.bind('cC', 'yank -s')
config.bind('cd', 'yank domain')
config.bind('cm', 'yank inline [{title}]({url:yank})')
config.bind('cp', 'yank pretty-url')
config.bind('ct', 'yank title')
config.bind('cc', 'yank')
config.bind(';C', 'hint links yank-primary')
config.bind(';c', 'hint links yank')

config.bind('w', 'hint links spawn mpv --force-window=immediate --input-ipc-server=/tmp/mpv-socket --ytdl-format="bestvideo[height<=?2160]+bestaudio/best" {hint-url}')
config.bind('a', 'hint links spawn bash -c "echo \'loadfile {hint-url} append\' | socat - /tmp/mpv-socket"')
config.bind('W', 'hint links spawn mpv --force-window=immediate --input-ipc-server=/tmp/mpv-socket --ytdl-raw-options="yes-playlist=,format=bestvideo[height<=?2160]+bestaudio/best" {hint-url}')

config.unbind('<Ctrl-V>')
config.unbind('v')
config.unbind('V')
config.bind('VV', 'open -t -- {primary}')
config.bind('Vv', 'open -t -- {clipboard}')
config.bind('vV', 'open -- {primary}')
config.bind('vv', 'open -- {clipboard}')

c.hints.chars = 'arstgmneio'

c.content.blocking.enabled = True

# catpuccin
import os
from urllib.request import urlopen

if not os.path.exists(config.configdir / "theme.py"):
    theme = "https://raw.githubusercontent.com/catppuccin/qutebrowser/main/setup.py"
    with urlopen(theme) as themehtml:
        with open(config.configdir / "theme.py", "a") as file:
            file.writelines(themehtml.read().decode("utf-8"))

if os.path.exists(config.configdir / "theme.py"):
    import theme
    theme.setup(c, 'latte', True)
