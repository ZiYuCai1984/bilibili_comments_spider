from function import fetchURL, repliesIsNull
import json, time

'''
测试function功能
'''

filename = 'data\\33081097\\1_33081097.json'

f = open(filename,'r',encoding='utf-8')
dict = json.load(f)
    
replies = dict['data']['replies']

fw = open('comments.txt','a',encoding='utf-8')
length = len(replies)
while len(replies) > 0: 
    # 从replies提取出单条评论
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