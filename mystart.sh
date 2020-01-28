apt-get update -y
apt-get install -y python3-rtree
pip install -r /home/site/wwwroot/requirements.txt
gunicorn --bind=0.0.0.0:$PORT app:app
