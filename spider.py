import requests
import json

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

def storeData(text,pageNum):
    filename = 'commitData.json'
    # with open(pageNum+filename,'a',encoding='utf-8') as f:
    #     f.write(text)
    # print(pageNum+'done !')
    data = json.loads(text)
    with open(pageNum+filename,'w',encoding='utf-8') as f:
        f.write(json.dumps(data,indent=2,ensure_ascii=False))
        print(pageNum+'done !')

if __name__ == '__main__':
    for i in range(1,461):
        url = 'https://api.bilibili.com/x/v2/reply?pn='+str(i)+'&type=1&oid=286054084'
        print(url)
        html = fetchURL(url)
        storeData(html,str(i))
        #print(html)