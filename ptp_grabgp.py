import os, re, json
from pyquery import PyQuery as pq


url = 'https://passthepopcorn.me/torrents.php?page=1&action=advanced&grouping=0&scene=2&order_by=gptime'

site = 'https://passthepopcorn.me/'
cookie_file = '/home/mike/cookies.txt'  ##path to cookie file with PTP logged in cookies
watchdir = '/home/mike/rwatch/'  ##path to rtorrent watch directory

os.system('curl -s -b ' + cookie_file + ' -o ptp_gp.html "' + url + '"')

goldenpage = pq(filename='ptp_gp.html')


regex = r"{(.*)}"
#moviesJson = json.loads(re.search(regex,goldenpage('script:contains("SetViewMode")').html(),re.MULTILINE).group(0))
moviesJson = re.search(regex,goldenpage('script:contains("SetViewMode")').html(),re.MULTILINE).group(0)
print moviesJson;


for possible_torrent in goldenpage('a.torrent-info-link'):
    print 'here'
    dl_link = site + possible_torrent.attrib['href']
    print "possible freeleach torrent link: " +  dl_link

    # if(possible_torrent):
    #
    #     if(not possible_torrent('a.torrent-info-link span.torrent-info__download-modifier--free')):
    #         continue
    #     if(possible_torrent('a.torrent-info-link--user-downloaded')):
    #         continue
    #     if(possible_torrent('a.torrent-info-link--user-seeding')):
    #         continue
    #
    #     print "** Grabbing " + possible_torrent('a.torrent-info-link').text()
    #     dl_link = possible_torrent('span.basic-movie-list__torrent__action a[title="Download"]')[0].attrib['href']
    #     print "** Download link: " + dl_link
    #     dl_url = url + dl_link
    #     os.system('cd ' + watchdir + ' ; curl -s -b ' + cookie_file + ' -O -J ' + '"'+dl_url+'"')




	
