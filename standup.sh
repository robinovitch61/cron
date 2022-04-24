#!/usr/bin/env sh

#0 8-17 * * 1-5 ~/projects/cron/standup.sh > /tmp/standup.txt 2>&1
say -v Zarvox 'Get up! Stand up! Stretch! Drink water!' & \
osascript -e 'display alert "Stand up and stretch!"'

