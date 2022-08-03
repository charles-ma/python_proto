import urllib2 as url

def call_web_service():
    x = url.urlopen('http://127.0.0.1:8080')
    print(x)

if __name__ == '__main__':
    call_web_service()
