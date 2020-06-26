from function import fetchURL, getComments, storeData, getComments2
from av import av_1, av_2, av_3
'''
入口
'''

if __name__ == "__main__":
    # 在这统一修改av号
    av = av_3

    api_url = 'https://api.bilibili.com/x/v2/reply?'
    for i in range(1,474):
        # i为评论的页数范围
        url = api_url + 'pn=' + str(i) + '&type=1&oid=' + str(av)
        text = fetchURL(url)

        # 方法1：直接提取评论
        # getComments(text,str(av))

        # 方法2：先保存在本地文件中在处理
        filename = storeData(text,str(av),str(i))
        getComments2(filename,str(av))