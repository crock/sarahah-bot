import requests

good_proxies = []
bad_proxies = []

def get_proxy_list():
    fx = open('proxies.txt', 'r')
    proxies = fx.read().split('\n')
    fx.close()

    return proxies

def set_proxy(session, proxy):
    if proxy != 'none':
        session.proxies.update({
            'http:' : 'http://' + proxy,
            'https:' : 'https://' + proxy
        })
    return session

def check_proxy(proxy):
    ps = requests.Session()
    try:
        session = set_proxy(ps, proxy)
        r = session.get('https://google.com', timeout=4)
        if r.status_code is 200:
            good_proxies.append(proxy)
            return True
    except r.raise_for_status():
        bad_proxies.append(proxy)
        return False
