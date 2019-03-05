"""
    instabot example

    Workflow:
        shows self DM.
"""

import argparse
import os
import sys

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-proxy', type=str, help="proxy")
args = parser.parse_args()

bot = Bot()
bot.login(username=args.u, password=args.p,
          proxy=args.proxy)

print(bot.api.getv2Inbox())
data = bot.last_json['inbox']['threads']
for item in data:
    print(item['inviter']['username'])
    last_item = item['last_permanent_item']
    item_type = last_item['item_type']
    if item_type == 'text':
        print(last_item['text'])
    else:
        print(item_type)
