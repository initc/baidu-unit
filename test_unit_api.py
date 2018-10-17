# encoding:utf-8
import urllib2
# 24.288511166507b705f4575236881f058a.2592000.1541656888.282335-14375606
# 24.6ac1f5dca5685adccf0b678de5df2fe3.2592000.1541656902.282335-14375606
access_token = '24.d809d8600bdaa0f67888835623e54a4f.2592000.1541654665.282335-14375606'
url = 'https://aip.baidubce.com/rpc/2.0/unit/bot/chat?access_token=' + access_token
post_data = "{\"bot_session\":\"\",\"log_id\":\"7758521\",\"request\":{\"bernard_level\":1,\"client_session\":\"{\\\"client_results\\\":\\\"\\\", \\\"candidate_options\\\":[]}\",\"query\":\"今天网上去济南的火车？\",\"query_info\":{\"asr_candidates\":[],\"source\":\"KEYBOARD\",\"type\":\"TEXT\"},\"updates\":\"\",\"user_id\":\"88888\"},\"bot_id\":\"12088\",\"version\":\"2.0\"}"
request = urllib2.Request(url, post_data)
request.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(request)
content = response.read()
if content:
    print content