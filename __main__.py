import subprocess
import sys

try:

    import requests, colorama, tqdm, socks
except:
    subprocess.check_call([sys.executable,'-m','pip', 'install', 'requests', 'colorama', 'tqdm', 'pysocks'])
import os.path

import zipfile
from time import sleep

import requests
from tqdm import tqdm

import XeoN


def download(url, filename):
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        length = int(r.headers.get('content-length'))
        for c in tqdm(r.iter_content(chunk_size=1024), total=int((length / 1024) + 1), desc=f'Downloading {filename}',
                      unit='KB'):
            if c:
                f.write(c)


if not os.path.exists('redis'):
    try:
        print('Trying to download from github...')
        download('https://github.com/tporadowski/redis/releases/download/v5.0.14.1/Redis-x64-5.0.14.1.zip',
                 'Redis-x64-5.0.14.1.zip')
    except:
        try:
            print('Trying to download from hsn mirror...')
            download('http://download.zh314.xyz/mirror/redis/Redis-x64-5.0.14.1.zip',
                     'Redis-x64-5.0.14.1.zip')
        except:
            try:
                print('Trying to download from hsn-cf mirror...')
                download('http://download-cf.zh314.xyz/mirror/redis/Redis-x64-5.0.14.1.zip',
                         'Redis-x64-5.0.14.1.zip')
            except:
                raise ConnectionError()

    os.makedirs('redis')
    with zipfile.ZipFile('Redis-x64-5.0.14.1.zip') as f:
        f.extractall('redis')

if not os.path.exists('proxy_pool'):
    subprocess.check_call(['git', 'clone', 'https://github.com/hsn8086/proxy_pool.git'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'],
                          cwd='proxy_pool')

subprocess.Popen(['redis\\redis-server.exe', 'redis.windows.conf'], cwd='redis')
subprocess.Popen([sys.executable, 'proxyPool.py', 'schedule'], cwd='proxy_pool')
subprocess.Popen([sys.executable, 'proxyPool.py', 'server'], cwd='proxy_pool')
sleep(16)
XeoN.get_proxy()
XeoN.main()
