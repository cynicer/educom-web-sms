import requests

common_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Referer': 'https://educom.kontomanager.at/',
    'Origin': 'https://educom.kontomanager.at/'
}


def generate_session_id():
    response = requests.post('https://educom.kontomanager.at/', headers=common_headers)

    if 'PHPSESSID' not in response.headers['Set-Cookie']:
        return ""

    for header in response.headers['Set-Cookie'].split(';'):
        if 'PHPSESSID' in header:
            return header.split('=')[1]


def generate_session(username, password):
    session_id = generate_session_id()

    headers = common_headers.copy()
    headers['Content-Type'] = 'application/x-www-form-urlencoded'
    headers['Cookie'] = 'PHPSESSID=' + session_id
    data = {
        'login_rufnummer': username,
        'login_passwort': password
    }
    response = requests.post('https://educom.kontomanager.at/index.php', headers=headers, data=data)

    # contains alert if no successful login -> no header change
    if 'alert-warning' in str(response.content):
        raise ConnectionError("Login failed.")

    headers = common_headers.copy()
    headers['Cookie'] = 'PHPSESSID=' + session_id
    requests.post('https://educom.kontomanager.at/kundendaten.php', headers=headers)

    return session_id


def send_sms(session_id, target_network, target_number, text):
    headers = common_headers.copy()
    headers['Content-Type'] = 'application/x-www-form-urlencoded'
    headers['Cookie'] = 'PHPSESSID=' + session_id
    data = {
        'telefonbuch': '-',
        'to_netz': target_network,
        'to_nummer': target_number,
        'nachricht': text
    }
    requests.post('https://educom.kontomanager.at/websms_send.php', headers=headers, data=data)


session = generate_session("e@mail.com", "password")
send_sms(session, "0043699", "12345678", "Hello World!")



