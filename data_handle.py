import json
'''
处理json文件，只提取评论部分进行处理
'''


def getReplies(filename):
    f = open(filename,'r',encoding='utf-8')
    dict = json.load(f)


    fw = open('commits.txt','a',encoding='utf-8')
    for i in range(20):
        fw.write(dict['data']['replies'][i]['content']['message']+'\n')    
    print(filename+'done !')

    # 提取data字段
    # dict_data = {key: value for key, value in dict.items() if key == 'data'}
    # # 提取replies字段
    # dict_replies= {key: value for key, value in dict_data.items() if key == 'page'}

    # print(dict_replies)

    # list_replies = []
    # list_replies.append(dict_data['replies'])

    # print(dict_data['page'])

    # data.append(dict['data'])
    # print(type(dict_data))



