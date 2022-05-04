import requests
import json

headers1 = {"Authorization": "Bearer (authkey)",
            "Content-Type": "application/json"
            }
data1 = {
    "from": "447520651783",
    "to": ["918882474233"],
    "body": "undefined",
        }
url1 = "https://sms.api.sinch.com/xms/v1/17705719db0e49a78b86164b0c0bdb89/batches"
requests.post(url=url1, data=json.dumps(data1),headers=headers1)
