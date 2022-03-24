"""
 * Project name(项目名称)：Python_if_else条件语句
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/24 
 * Time(创建时间)： 20:07
 * Version(版本): 1.0
 * Description(描述)： 
 """
import sys

if __name__ == '__main__':
    age = int(input("请输入你的年龄："))
    if age < 18:
        print("警告：你还未成年，不能使用该软件！")
        sys.exit()
    else:
        print("你已经成年，可以使用该软件。")
    print("软件正在使用中...")
