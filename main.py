import requests

def check_domain(domain):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {
        'domainname': domain,
    }
    response = requests.post('https://www.turkticaret.net/siberhosting/whoisAjax.php', headers=headers, data=data)
    if response.text.__contains__('whois'):
        return False
    return True

domains = [
    'domain1.com', 'domain2.com', 'domain3.com'
]
