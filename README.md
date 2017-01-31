# ptp-grabrecs
Simple script to automatically grab user recommendations from PTP


## Installation
0. clone/download this repo on your server

1. Install pyquery 
  ```sh
  	pip install pyquery
  ```
2. Download cookies.txt chrome extension

3. Login to PTP in chrome and download the cookies.txt file

4. scp cookies.txt file up to your server

5. modify ptp_grabrecs.py to change the following config variables
  ```python
    cookie_file = '/home/mike/cookies.txt'  ##path to cookie file with PTP logged in cookies
    searchstring = 'x264 / MKV'  ## string to search on the torrent page
    watchdir = '/home/mike/rwatch/'  ##path to rtorrent watch directory
  ```
6. run the script:
  ```sh
  	python ptp-grabrecs/ptp_grabrecs.py
  ```
  
7. if it looks good, you can add it to crontab
