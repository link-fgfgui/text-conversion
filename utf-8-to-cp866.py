try:
    print('输出:'+input('输入:').encode('utf-8').decode('cp866'))
except UnicodeDecodeError:
    print('输入错误!\n程序编码失败，无输出')
input()
