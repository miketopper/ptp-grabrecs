import os
from pyquery import PyQuery as pq

cookie_file = '/home/mike/cookies.txt'
url = 'https://passthepopcorn.me/'
searchstring = 'x264 / MKV'
watchdir = '/home/mike/rwatch/'

os.system('curl -s -b ' + cookie_file + ' -o ptp_homepage.html ' + url)

homepage = pq(filename='ptp_homepage.html')

for userrec in homepage('div.user-recommendation a.l_movie'):

    rec_page = url + userrec.attrib['href']
    print "Downloading torrent page: " +  rec_page
    os.system('curl -s -b ' + cookie_file + ' -o recpage.html ' + rec_page)
	
    recpage_html = pq(filename='recpage.html')

    ## remove the pass line and the if line if you want to download multiple of the same thing
    for possible_torrent in recpage_html('tr.group_torrent td:contains("'+searchstring+'")').items():
        pass
	
    if(possible_torrent):
        print "** Grabbing " + possible_torrent('a.torrent-info-link').text()

        if(not possible_torrent('a.torrent-info-link span.torrent-info__download-modifier--free')):
            continue
        if(possible_torrent('a.torrent-info-link--user-downloaded')):
            continue
        if(possible_torrent('a.torrent-info-link--user-seeding')):
            continue

        print "** Grabbing " + possible_torrent('a.torrent-info-link').text()
        dl_link = possible_torrent('span.basic-movie-list__torrent__action a[title="Download"]')[0].attrib['href']
        print "** Download link: " + dl_link
        dl_url = url + dl_link
        os.system('cd ' + watchdir + ' ; curl -s -b ' + cookie_file + ' -O -J ' + '"'+dl_url+'"')




	
