import requests

access_token = '24.d809d8600bdaa0f67888835623e54a4f.2592000.1541654665.282335-14375606'
url = 'https://aip.baidubce.com/rpc/2.0/unit/bot/chat?access_token=' + access_token

payload = {'bot_session': '', 'log_id': '7758521', 'request': {'bernard_level': 1, 'client_session': '{"client_results":"", "candidate_options":[]}', 'query': '今天网上去济南的火车？', 'query_info': {'asr_candidates': [], 'source': 'KEYBOARD', 'type': 'TEXT'}, 'updates': '', 'user_id': '88888'}, 'bot_id': '12088', 'version': '2.0'}

headers = {'Content-Type', 'application/json'}

def getChat(text):
	payload["query"] = text
	r = requests.post(url, json=payload)
	return r