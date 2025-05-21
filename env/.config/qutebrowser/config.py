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

c.hints.chars = 'arstgmneio'

c.content.blocking.enabled = True
