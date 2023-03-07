import urllib.request, urllib.parse, urllib.error
import json

def main():
    print("API")
    serviceurl = "http://py4e-data.dr-chuck.net/geojson?"
    while True:
        address = input("Enter location: ")
        if len(address)<1:
            break
        url = serviceurl + urllib.parse.urlencode({"address":address})
        print("Retrieving",url)
        uh = urllib.request.urlopen(url)
        data = uh.read().decode()
        print("Retrieved",len(data),"characters")
        try:
            js = json.loads(data)
        except:
            js = None
        if not js or "status" not in js or js["status"] != "OK":
            print("===Failure to retrieve===")
            print(data)
            continue
        print(json.dumps(js,indent=4))
        lat = js["results"][0]["geometry"]["location"]["lat"]
        lng = js["results"][0]["geometry"]["location"]["lng"]
        print("Lat:",lat,", Lng",lng)
        location = js["results"][0]["formatted_address"]
        print("Location:",location)
    
if __name__ == "__main__":
    main()