try:
    print('输出:'+input('输入:').encode('utf-8').decode('gbk'))
except UnicodeDecodeError:
    print('输入错误!\n程序编码失败，无输出')
except UnicodeEncodeError:
    print('输入错误!\n程序解码失败，无输出')
input()
