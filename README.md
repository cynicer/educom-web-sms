# Educom Web SMS
Send SMS via the Educom web interface with a little Python script.

## Usage
```
EducomWebSms.py [-h] username password prefix number message

Send a SMS via your Educom Web SMS account.

positional arguments:
  username    Username (mail or phone number).
  password    Account password.
  prefix      Prefix of your target network (e.g. 0043699). The EXACT format is important!
  number      Phone number to send the SMS to without the prefix (e.g. 12345678).
  message     Message to send via SMS.

optional arguments:
  -h, --help  show this help message and exit
```