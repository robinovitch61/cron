#!/Users/leo/.pyenv/versions/voltus/bin/python

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import random

client = WebClient(token=os.getenv("SLACK_API_TOKEN"))

messages = (
    "Stand up! π§ββοΈ",
    "Big stretch time! πββοΈ",
    "Time for a glass of water! π§",
    "Look away from your screen a while! π",
    "Reach for your toes for 30s! π€ΈββοΈ",
    "Go for a little pace around the room! πΆββοΈ",
    "Hey you! You're doing great! β€οΈ",
)

client.chat_postMessage(channel='#for-your-health', text="<!here> " + random.choice(messages) + " For your health!")
