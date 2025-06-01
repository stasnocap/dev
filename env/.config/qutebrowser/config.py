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
config.bind('X', 'undo')

config.bind('k', 'search-next')
config.bind('K', 'search-pre')

config.unbind('<Ctrl-V>')

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
