import os, re, json
from pyquery import PyQuery as pq


url = 'https://passthepopcorn.me/torrents.php?page=1&action=advanced&grouping=0&scene=2&order_by=gptime'

site = 'https://passthepopcorn.me/'
cookie_file = '/home/mike/cookies.txt'  ##path to cookie file with PTP logged in cookies
watchdir = '/home/mike/dwatch/'  ##path to rtorrent watch directory

gp_html = os.popen('curl -s -b ' + cookie_file + '  "' + url + '"').read()

goldenpage = pq(gp_html)


regex = r"{(.*)}"
movies = json.loads(re.search(regex,goldenpage('script:contains("SetViewMode")').html(),re.MULTILINE).group(0))


for movie in movies['Movies']:
    try:
        if(movie['GroupingQualities'][0]['Torrents'][0]['Freeleech']):
            #print movie['Title'] + " IS FREELEECH!"
            possible_torrent = pq(movie['GroupingQualities'][0]['Torrents'][0]['Title'])
            if(possible_torrent('a.torrent-info-link--user-downloaded')):
                #print "** already downloaded!"
                continue
            if(possible_torrent('a.torrent-info-link--user-seeding')):
                #print "** already seeding!"
                continue

            print "** Grabbing " + movie['Title'] + " - " + possible_torrent('a.torrent-info-link').text()
            torrent_id = movie['GroupingQualities'][0]['Torrents'][0]['TorrentId']
            auth_key = movies['AuthKey']
            torrent_pass = movies['TorrentPass']
            dl_url = site + "torrents.php?action=download&id="+str(torrent_id)+"&authkey="+auth_key+"&torrent_pass="+torrent_pass
            print "** Download link: " + dl_url
            os.system('cd ' + watchdir + ' ; curl -s -b ' + cookie_file + ' -O -J ' + '"'+dl_url+'"')
    except KeyError:
        continue











	
