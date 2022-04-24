#!/Users/leo/.pyenv/versions/voltus/bin/python

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import random

client = WebClient(token=os.getenv("SLACK_API_TOKEN"))

messages = (
    "Stand up! 🧍‍♂️",
    "Big stretch time! 🙆‍♀️",
    "Time for a glass of water! 💧",
    "Look away from your screen a while! 👀",
    "Reach for your toes for 30s! 🤸‍♀️",
    "Go for a little pace around the room! 🚶‍♂️",
    "Hey you! You're doing great! ❤️",
)

client.chat_postMessage(channel='#for-your-health', text="<!here> " + random.choice(messages) + " For your health!")
