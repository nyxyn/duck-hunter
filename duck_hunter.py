import hexchat
import threading
import time

TEXT_EVENT = 'Channel Message'
DUCK_BOT = 'gonzobot'
KEYWORD_1 = ' quack!'
KEYWORD_2 = ' flap!'

__module_name__ = 'duck_hunter'
__module_version__ = '1.0'
__module_description__ = 'Befriend that pesky duck'


def say():
    time.sleep(2)
    hexchat.command('say .bef')


def print_callback(words, eol, userdata):
    nick = words[0]
    message = words[1].replace(u'\u200b', '').lower()
    
    if DUCK_BOT in nick and (KEYWORD_1 in message or KEYWORD_2 in message):
        thread = threading.Thread(target=say)
        thread.start()

    return hexchat.EAT_NONE


hexchat.prnt('Setting hook for duck hunter...')
hexchat.hook_print(TEXT_EVENT, print_callback)
hexchat.prnt('Hook set')

