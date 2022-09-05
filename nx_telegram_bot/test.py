import json

string = b"{'days_since_first_meet': 134}"
body = string.replace(b"'", b'"')
body = json.loads(body)
print (body['days_since_first_meet'])