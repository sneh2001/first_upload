import urllib.request
webUrl = \
    urllib.request.urlopen('http://wordpress.org/plugins/about/readme.txt'
                           )
print 'Result code: ' + str(webUrl.getcode())

data = webUrl.read()
print data
