from data_handle import getReplies
'''
数据处理的入口
'''
for i in range(1,461):
    filename = 'data\\'+ str(i) +'commitData.json'
    getReplies(filename)