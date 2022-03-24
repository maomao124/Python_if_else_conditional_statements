"""
 * Project name(项目名称)：Python_if_else条件语句
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/24 
 * Time(创建时间)： 20:08
 * Version(版本): 1.0
 * Description(描述)： 
 """

if __name__ == '__main__':
    height = float(input("输入身高（米）："))
    weight = float(input("输入体重（千克）："))
    bmi = weight / (height * height)  # 计算BMI指数
    if bmi < 18.5:
        print("BMI指数为：" + str(bmi))
        print("体重过轻")
    elif 18.5 <= bmi < 24.9:
        print("BMI指数为：" + str(bmi))
        print("正常范围，注意保持")
    elif 24.9 <= bmi < 29.9:
        print("BMI指数为：" + str(bmi))
        print("体重过重")
    else:
        print("BMI指数为：" + str(bmi))
        print("肥胖")
