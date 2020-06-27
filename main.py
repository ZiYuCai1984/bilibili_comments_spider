from function import fetchURL, getComments, storeData, getComments2, repliesIsNull
from av import av_1, av_2, av_3, av_4, av_5
'''
入口
'''

if __name__ == "__main__":
    # 在这统一修改av号，只需要修改这个参数即可
    av = av_3
    
    
    # 评论页数
    i = 1
    # 评论条数
    j = 0
    api_url = 'https://api.bilibili.com/x/v2/reply?'
    while True:
        # i为评论的页数范围
        url = api_url + 'pn=' + str(i) + '&type=1&oid=' + str(av)
        data = fetchURL(url)

        # 判断是否包含reply
        if repliesIsNull(data):
            print('共有' + str(i-1) + '页评论，' + str(j) + '条评论')
            break

        # 方法1：直接提取评论
        # getComments(text,str(av))

        # 方法2：先保存在本地文件中在处理
        filename = storeData(data,str(av),str(i))
        repliesNUm = getComments2(filename,str(av))
        j = j + repliesNUm
        i = i + 1