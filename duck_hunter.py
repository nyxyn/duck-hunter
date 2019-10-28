import hexchat
import threading
import time
import random

TEXT_EVENT = 'Channel Message'
DUCK_BOT = 'gonzobot'
KEYWORD_1 = ' quack!'
KEYWORD_2 = ' flap!'
CHANNEL_KEY = 'channel'

__module_name__ = 'duck_hunter'
__module_version__ = '1.0'
__module_description__ = 'Befriend that pesky duck'


def say(channel):
    channel_context = hexchat.find_context(channel=channel)

    sleep_delay = random.randint(4, 15)
    time.sleep(sleep_delay)

    command = 'msg {} .bef'.format(channel)
    channel_context.command(command)


def print_callback(words, eol, userdata):
    nick = words[0]
    message = words[1].replace(u'\u200b', '').lower()
    channel = hexchat.get_info(CHANNEL_KEY)

    if DUCK_BOT in nick and (KEYWORD_1 in message or KEYWORD_2 in message):
        thread = threading.Thread(target=say, args=(channel,))
        thread.start()

    return hexchat.EAT_NONE


hexchat.prnt('Setting hook for duck hunter...')
hexchat.hook_print(TEXT_EVENT, print_callback)
hexchat.prnt('Hook set')

