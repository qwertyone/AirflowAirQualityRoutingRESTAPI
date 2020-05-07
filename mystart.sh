##this file is critical to the service through Azure. The majority of my time was spent trying to address Azure machine problems with the python modules.

apt-get update -y
pip install --upgrade pip
apt-get install -y python3-rtree
pip install -r /home/site/wwwroot/requirements.txt
gunicorn --bind=0.0.0.0:$PORT app:app
