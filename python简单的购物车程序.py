#!/usr/bin/env python 
#_*_coding:utf-8_*_

#创建商品列表
product_list = [
    ('Robot',200000),
    ('MacPro',12000),
    ('Iphone8',8888),
    ('Hello World',1200),
                ] 

#创建购物车列表				
shopping_list = []

user_salary=input("请输入你的工资：")
if user_salary.isdigit():
    user_salary = int(user_salary)
    while True:
        print("商品如下：")
        for index,item in enumerate(product_list): 
            
            print (index,item)
        user_choice = input("请输入要购买的商品编号：")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice > -1:
                p_item = product_list[user_choice]
                if user_salary>=p_item[1]:
                    shopping_list.append(p_item)
                    user_salary-=p_item[1]
                    print("购买商品",p_item,"成功您的余额为",user_salary,"元！" )
                else:
                    print("您的余额为",user_salary,"余额不足以购买此商品，购买失败！")
                            
            else:
                print("并无此产品！")
        elif user_choice == "q":
            print("--------shopping list-------")
            for i in shopping_list:
                print(i)
            exit()
        else:
            print("invalidate！！！")