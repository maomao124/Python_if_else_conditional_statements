"""
 * Project name(项目名称)：Python_if_else条件语句
 * Package(包名): 
 * File(文件名): test4
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/24 
 * Time(创建时间)： 20:13
 * Version(版本): 1.0
 * Description(描述)： Python if语句嵌套
 """

if __name__ == '__main__':
    proof = int(input("输入驾驶员每 100ml 血液酒精的含量："))
    if proof < 20:
        print("驾驶员不构成酒驾")
    else:
        if proof < 80:
            print("驾驶员已构成酒驾")
        else:
            print("驾驶员已构成醉驾")
