import requests
from itertools import cycle

proxy_list = [
    'http://119.18.156.245:8080',
    'http://168.126.74.132:80',
    'http://50.144.166.226:80',
    'http://51.81.187.228:3128'
]

proxy_pool = cycle(proxy_list)

MAX_REQUESTS_PER_PROXY = 10

request_counter = {}

total_requests = 50

url = 'https://jsonplaceholder.typicode.com/posts'

def make_requests():
    for _ in range(total_requests):
        proxy = next(proxy_pool)
        
        if proxy not in request_counter:
            request_counter[proxy] = 0
        
        while request_counter[proxy] >= MAX_REQUESTS_PER_PROXY:
            proxy = next(proxy_pool)
            if proxy not in request_counter:
                request_counter[proxy] = 0

        request_counter[proxy] += 1
        
        proxies = {
            'http': proxy,
            'https': proxy,
        }

        try:
            response = requests.get(url, proxies=proxies, timeout=5)
            data = response.json()
            print('data', data)
            if response.status_code == 200:
                print(f"Request successful with proxy {proxy}")
            else:
                print(f"Request failed with proxy {proxy}, status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error with proxy {proxy}: {e}")

make_requests()
