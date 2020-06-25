from function import fetchURL, getComments
'''
入口
'''

if __name__ == "__main__":
    av_1 = 286054084
    av_2 = 583623415
    api_url = 'https://api.bilibili.com/x/v2/reply?'
    for i in range(1,230):
        # i为评论的页数范围
        url = api_url + 'pn=' + str(i) + '&type=1&oid=' + str(av_2)
        text = fetchURL(url)
        getComments(text)