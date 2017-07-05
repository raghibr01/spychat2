#self function info
import request
from constant import APP_ACCESS_TOKEN, BASE_URL
url= (BASE_URL + '/user/self/?access_tokens' ) % APP_ACCESS_TOKEN
requests.get(url)
print requests.get(url).json()['data']['username']
print requests.get(url).json()['data']['id']
response = requests.get(url).json()
print response['data']['username']
print response['date']['id']

