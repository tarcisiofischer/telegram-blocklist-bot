Telegram Blocklist Bot
===

A very simple blocklist bot for telegram. It will check if a user is in a blocklist. In case he/she is, they'll be banned from the group
(Even if the user never entered before). 

### How to install

1. Create a bot in `BotFather` in instagram (Say `/newbot` and follow instructions). Save the access `TOKEN` it'll provide.
2. In `BotFather`, set `/setprivacy` to `Disable`.
3. Run `python run_bot.py [TOKEN]`.

**NOTE**: You may need to install `python-telegram-bot`. e.g.: `pip install python-telegram-bot`.

### How to block other users

1. Stop running the script.
2. Edit the source code and add an entry in the `BAN_LIST`.
3. Run the script again.
