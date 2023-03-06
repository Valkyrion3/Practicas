import urllib.request, urllib.parse, urllib.error
def main():
    print("Browser 2")
    fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
    count = dict()
    for line in fhand:
        words = line.decode().split()
        for w in words:
            count[w]= count.get(w,0)+1
    print(count)
    
if __name__ == "__main__":
    main()