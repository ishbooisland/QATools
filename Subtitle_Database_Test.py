import os
import hashlib
import requests


def get_hash(name):
    readsize = 64 * 1024
    with open(name, 'rb') as f:
        size = os.path.getsize(name)
        data = f.read(readsize)
        f.seek(-readsize, os.SEEK_END)
        data += f.read(readsize)
    return hashlib.md5(data).hexdigest()


MovieHash = get_hash(
    'C:\Users\Darrin\Documents\Downloads\Deadpool.2016.1080p.HDRip.KORSUB.x264.AAC2.0-STUTTERSHIT\DeadPool.mkv')
user_agent = {'User-agent': 'SubDB/1.0 (getSubs/0.1; http://github.com/)'}

s = requests.get('http://api.thesubdb.com/?action=search&hash=' + MovieHash, headers=user_agent)
s = requests.get('http://api.thesubdb.com/?action=download&hash=' + MovieHash + '&language=en', headers=user_agent)
print s.text
