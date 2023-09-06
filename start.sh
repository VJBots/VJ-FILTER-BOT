if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/wishvishnu179/ADVFILTERBOT.git /ADVFILTERBOT 
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /ADVFILTERBOT 
fi
cd /ADVFILTERBOT
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
