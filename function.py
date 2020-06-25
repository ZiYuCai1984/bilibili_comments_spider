import requests
import json
import time

def fetchURL(url):
    '''
    功能：访问url，获取网页返回内容
    参数：
        url：目标网页的url
    返回：目标网页的html内容
    '''
    headers = {
        'accept':'*/*',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    }

    try:
        r = requests.get(url,headers = headers)
        r.raise_for_status()
        print(r.url)
        return r.text
    except requests.HTTPError as e:
        print(e)
        print("HTTPError")
    except requests.RequestException as e:
        print(e)
    except:
        print("Unkown Error !")

def getComments(text):
    '''
    功能：处理json文件，只提取评论部分
    参数：
        filename，待处理文件的路径
    '''
    dict = json.loads(text)

    replies = dict['data']['replies']

    fw = open('comments.txt','a',encoding='utf-8')
    while len(replies) > 0: 
        # 从replies提取出单条评论
        reply = replies.pop()  
        # 发表评论的用户名称
        uname = reply['member']['uname']
        # 评论内容
        comments = reply['content']['message']
        # 评论发表的时间
        ctime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(reply['ctime']))
        msg = 'bilibili users///  ' + uname + '///' + ctime + ':::' + '  say:  '+ comments
        fw.write(msg+'\n')    
    print('done !')