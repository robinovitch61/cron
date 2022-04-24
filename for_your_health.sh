#0 8-17 * * 1-5 /bin/zsh -lc ~/projects/cron/for_your_health.sh > /tmp/health.txt 2>&1
BASEDIR=$(dirname "$0")

export $(/Users/leo/go/bin/vault-vals prod slack.SLACK_API_TOKEN)
$BASEDIR/for_your_health.py
