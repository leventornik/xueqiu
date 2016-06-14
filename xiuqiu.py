import urllib2,json
url="http://xueqiu.com/p/ZH488118"
send_headers = {
    'Referer': 'http://xueqiu.com/p/ZH488118',
    'User-Agent': 'MMozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Host': 'xueqiu.com'

}
req=urllib2.Request(url,headers=send_headers)
r=urllib2.urlopen(req)
html=r.read()
r.close

pos_start = html.find('SNB.cubeInfo = ') + len('SNB.cubeInfo = ') 
pos_end = html.find('SNB.cubePieData') 
data = html[pos_start:pos_end] 
dic = json.loads(data)
print dic

