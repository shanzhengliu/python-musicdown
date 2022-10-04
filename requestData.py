#-*- coding: utf-8 -*-
import requests
import  json
import sys
def report(count, blockSize, totalSize):
  percent = int(count*blockSize*100/totalSize)
  sys.stdout.write("\r%d%%" % percent + ' complete')
  sys.stdout.flush()
print(u"输入搜索关键词")
import urllib
name=input()
print(u"搜索引擎，1:163，2: 虾米 3: 一听 ,4: 酷狗 5:酷我")
downlist =[]
namelist=[]
type= input()
if type==1:
    type='163'
if type==2:
    type='xiami'
if type==3:
    type='1ting'
if type==4:
    type='kugou'
if type==5:
    type='kuwo'
mydata = {
"music_input":name,
"music_filter":"name",
"music_type":type

}
header = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'Content-Length':'63',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        #'Cookie':'UM_distinctid=15b88dac07d156-0e5cf000836a3a-396a7807-13c680-15b88dac07ee07; CNZZDATA1261550119=2105194965-1492648025-http%253A%252F%252Fsearch.chongbuluo.com%252F%7C1492648025',
        'Host':'music.ifkdy.com',
        'Origin':'http://music.ifkdy.com',
        'Referer':'http://music.ifkdy.com/',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
 }

result = requests.post("http://music.ifkdy.com/",data=mydata,headers=header)
x= 0

myresult=json.loads(result.text.encode('utf-8'))
try:
    for temp in myresult['data']:
        #downlist.append(temp)
        print(x,temp['name'],temp['author'])
        downlist.append(temp['music'])
        getname=temp['name']+"_____"+temp['author']
        namelist.append(getname)
        x+=1
    #print requests.getmethod("http://music.ifkdy.com/",data=mydata).text
    #print result.text
    print("你要下哪一首")
    select=input()
   # print downlist[select]
    filename=u"./"+namelist[select]+'.mp3'
    #filename=filename.decode('utf-8').encode('utf-8')
    urllib.urlretrieve(downlist[select],filename,reporthook=report)

except:
    print("没有结果")
