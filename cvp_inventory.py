import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEADERS = {'Accept': 'application/json', 'Content-Type': 'application/json'}
REQUEST_TIMEOUT = 10

def _cvp_inventory(cvp, token):
    inventory = {}
    HEADERS["Authorization"] = f'Bearer {token}'
    session = requests.Session()
    url_prefix = f'https://{cvp}/cvpservice/inventory/devices'
    print('INFO: Collecting switch inventory information from CVP', cvp)
    response = session.get(url_prefix, headers=HEADERS, timeout=REQUEST_TIMEOUT, verify=False)

    print("response: ", response)

    print(response.json())

def main():
    cvp = "www.cv-prod-us-central1-c.arista.io"
    token = "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJkaWQiOjc0ODY1NTI2NjE4MTk0MzQ4OTIsImRzdCI6ImFjY291bnQiLCJleHAiOjE3OTg2NzUxOTksImlhdCI6MTc2ODM5MjYzNCwibGJhYyI6eyJzdWJuZXRzIjpbIjAuMC4wLjAvMCIsIjo6LzAiXX0sIm9naSI6NzQ4NjU1MjY2MTgxOTQwNzA2Miwib2duIjoiaGlnaHBvaW50LWRlbW8tdXMiLCJzaWQiOiI5MzZjMjk1MDYwYjUyZjg1OGJjNjc3YmM4ODAyOWE3YTFhOTAyNjlkMTliMjkzOGVhNTk3NzQwODlhYzUxN2JiLVJpUDFHRTRXWmZHbUlhaWsyV1hNSmxrVTJpV21SQ0VnLXNheXU1N0YifQ.3bGohdyFi9pF8CLu9fLX4iwX5CVc4pxXLOg7RXxWR-3ZxA6MqRj5k-HE6cXur3gvEWSbTn3CyeF5QBz3kkIF8A"
    _cvp_inventory(cvp, token)
    #print(result)

if __name__ == "__main__":
    main()