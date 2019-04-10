import urllib.request

allType = ["(BalFlowMainNet10)","(BalFlowMainRate10)","(AmtOfUNet10)","(AmtOfURate10)","(AmtOfBNet10)","(AmtOfBRate10)",
            "(AmtOfMNet10)","(AmtOfMRate10)","(AmtOfSNet10)","(AmtOfSRate10)"]

def geturl(page,type='(AmtOfUNet10)'):
    url='http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=ct&'
    url+='sty=DCFFITA&'
    url+='sortType='+type+'&'
    url+='sortRule=-1&'
    url+='page='+str(page)+'&'
    url+='pageSize=50&'
    url+='js=var%20quote_123={pages:(pc),data:[(x)]}&'
    url+='token=894050c76af8597a853f5b408b759f5d&'
    url+='cmd=C._AB&'
    url+='jsName=quote_123'
    return url

def gethtml(url):
    html = urllib.request.urlopen(url).read()
    html = html.decode('UTF8')
    return html

print(gethtml(geturl(1)))
