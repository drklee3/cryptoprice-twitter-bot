# crypto-twitter-bot

Simple Twitter bot that tweets cryptocurrency USD prices every hour.

# Usage

Create a cronjob:
```bash
$ crontab -e
```

Add the following line, adjust to your desired frequency:
```
0 * * * * python3 /path/to/bot.py > /dev/null 2>&1
```