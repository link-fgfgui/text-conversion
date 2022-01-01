try:
    print('输出:'+input('输入:').encode('gbk').decode('utf-8'))
except UnicodeDecodeError:
    print('输入错误!\n程序编码失败，无输出')
input()
