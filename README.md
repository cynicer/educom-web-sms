# Educom/XOXO Web SMS
Send SMS via the ~~Educom~~ XOXO web interface with a little Python script.

## Usage
```
EducomWebSms.py [-h] username password prefix number message

Send a SMS via your XOXO Web SMS account.

positional arguments:
  username    Username (mail or phone number).
  password    Account password.
  prefix      Prefix of your target network (e.g. 0043699). The EXACT format is important!
  number      Phone number to send the SMS to without the prefix (e.g. 12345678).
  message     Message to send via SMS.

optional arguments:
  -h, --help  show this help message and exit
```

**Important**: This works for Educom customers who signed up 2021 and earlier. All 2022 and later Educom constracts do not work.
