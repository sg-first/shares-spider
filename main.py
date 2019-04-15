import spider
import json
import csvIO

strData=[]
for i in range(1,76):
    a=spider.gethtml(spider.geturl(i))
    strData.append(a)

def to2DList(x):
    x=x[14:]
    x=x.replace('data','"data"')
    x = x.replace('pages', '"pages"')
    print(x)
    d=json.loads(x)
    d=d['data']
    c=[]
    for i in d:
        b=i.split(",")
        c.append(b)
    return c

all=[]
for i in strData:
    y=to2DList(i)
    all=all+y
    print(i)


csvIO.saveCsv('D:/pycharm/表.csv',all)
