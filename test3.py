"""
 * Project name(项目名称)：Python_if_else条件语句
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/24 
 * Time(创建时间)： 20:11
 * Version(版本): 1.0
 * Description(描述)： 
 """

if __name__ == '__main__':

    b = False
    if b:
        print('b是True')
    else:
        print('b是False')
    n = 0
    if n:
        print('n不是零值')
    else:
        print('n是零值')
    s = ""
    if s:
        print('s不是空字符串')
    else:
        print('s是空字符串')
    l = []
    if l:
        print('l不是空列表')
    else:
        print('l是空列表')
    d = {}
    if d:
        print('d不是空字典')
    else:
        print('d是空字典')


    def func():
        print("函数被调用")


    if func():
        print('func()返回值不是空')
    else:
        print('func()返回值为空')
