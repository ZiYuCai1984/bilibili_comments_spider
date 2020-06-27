import requests
import json
import time
import os

def fetchURL(url):
    '''
    功能：访问url，获取网页返回内容
    参数：
        url：目标网页的url
    返回：目标网页的html内容,dict类型
    '''
    headers = {
        'accept':'*/*',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    }

    try:
        r = requests.get(url,headers = headers)
        r.raise_for_status()
        # 将str类型转化为dict类型
        data = json.loads(r.text)
        print(r.url)
        return data
    except requests.HTTPError as e:
        print(e)
        print("HTTPError")
    except requests.RequestException as e:
        print(e)
    except:
        print("Unkown Error !")

def storeData(data,av,pageNum):
    '''
    功能：保存text到json文件中，以便后续处理
    参数：
        data:网页返回的信息，dict类型
        av:视频av号，str类型
        pageNum:评论的页数，str类型
    返回：文件的路径，str类型
    '''
    # 判断是否存在data以及av文件夹，否则新建
    if not os.path.exists('data'):
        os.mkdir('data')
    if not os.path.exists('data\\' + av):
        os.mkdir('data\\' + av)

    filename = 'data\\' + av + '\\' + pageNum + '_' + av + '.json'

    with open(filename,'a',encoding='utf-8') as f:
        f.write(json.dumps(data,indent=2,ensure_ascii=False))
        print(pageNum+'done !')
    return filename

def getComments(data,av):
    '''
    功能：处理网页返回信息，只提取评论部分
    参数：
        data，待处理信息，dict类型
        av:视频av号，str类型
    '''

    replies = data['data']['replies']

    fw = open(av + 'comments.txt','a',encoding='utf-8')
    while len(replies) > 0: 
        # 从replies提取出单条评论
        reply = replies.pop()  
        # 发表评论的用户名称
        uname = reply['member']['uname']
        # 评论内容
        comments = reply['content']['message']
        # 评论发表的时间
        ctime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(reply['ctime']))
        msg = 'bilibili users///' + uname + '///  ' + ctime + ':::' + '  say:  '+ comments
        fw.write(msg+'\n')    
    print('done !')

def getComments2(filename,av):
    '''
    功能：提取本地文件中的用户评论
    参数：
        filename:待处理的本地文件路径，str类型
        av:视频av号，str类型
    返回：len(replies)：评论条数
    '''
    f = open(filename,'r',encoding='utf-8')
    dict = json.load(f)
    
    replies = dict['data']['replies']

    fw = open(av + 'comments.txt','a',encoding='utf-8')
    length = len(replies)
    while len(replies) > 0: 
        # 从replies提取出首条评论赋值给reply并在replies中删除
        reply = replies.pop(0)  
        # 发表评论的用户名称
        uname = reply['member']['uname']
        # 评论内容
        comments = reply['content']['message']
        # 评论发表的时间
        ctime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(reply['ctime']))
        msg = 'bilibili users///' + uname + '///  ' + ctime + ':::' + '  say:  '+ comments
        fw.write(msg+'\n')    
    print('done !')
    return length

def repliesIsNull(data):
    '''
    功能：判断data中的replies参数是否为空
    参数：
        data：网页返回的信息，dict类型
    返回：Boolean类型
    '''    
    replies = data['data']['replies']
    if replies is None:
        return True
    else:
        return False 
