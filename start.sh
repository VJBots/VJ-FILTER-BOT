if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/TeamHMT/Auto-search-tamil-bot.git /Auto-search-tamil-bot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Auto-search-tamil-bot
fi
cd /Auto-search-tamil-bot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
