import requests

BASE = "http://127.0.0.1:5000"

def get_ips():
    # First response
    resp1 = requests.get(BASE + "/ips")
    try:
        print(resp1.json())
    except requests.exceptions.JSONDecodeError:
        print("Response is an error")
        print(resp1)
    else:
        print("Some other error: ", resp1)

def post_recommendations(data):
    resp1 = requests.post(data)
    print(resp1)


if __name__ == "__main__":
    get_ips()
    post_recommendations({"comb1":{"CPU":5.1, "RAM":128}})