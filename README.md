# crypto-twitter-bot

Simple Twitter bot that tweets cryptocurrency USD prices every hour.

# Usage

1. Modify bot.py, add your consumer/access key/secrets.
```python
twitter.Api(consumer_key="YOUR_CONSUMER_KEY_HERE",
        consumer_secret="YOUR_CONSUMER_SECRET_HERE",
        access_token_key="YOUR_ACCESS_TOKEN_KEY_HERE",
        access_token_secret="YOUR_ACCESS_TOKEN_SECRET_HERE")
```

2. Create a cronjob:
```bash
$ crontab -e
```

3. Add the following line, adjust based on your script path and desired frequency:
```
0 * * * * python3 /path/to/bot.py > /dev/null 2>&1
```