#!/usr/bin/env python 
#_*_coding:utf-8_*_

#������Ʒ�б�
product_list = [
    ('Robot',200000),
    ('MacPro',12000),
    ('Iphone8',8888),
    ('Hello World',1200),
                ] 

#�������ﳵ�б�				
shopping_list = []

user_salary=input("��������Ĺ��ʣ�")
if user_salary.isdigit():
    user_salary = int(user_salary)
    while True:
        print("��Ʒ���£�")
        for index,item in enumerate(product_list): 
            
            print (index,item)
        user_choice = input("������Ҫ�������Ʒ��ţ�")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice > -1:
                p_item = product_list[user_choice]
                if user_salary>=p_item[1]:
                    shopping_list.append(p_item)
                    user_salary-=p_item[1]
                    print("������Ʒ",p_item,"�ɹ��������Ϊ",user_salary,"Ԫ��" )
                else:
                    print("�������Ϊ",user_salary,"�����Թ������Ʒ������ʧ�ܣ�")
                            
            else:
                print("���޴˲�Ʒ��")
        elif user_choice == "q":
            print("--------shopping list-------")
            for i in shopping_list:
                print(i)
            exit()
        else:
            print("invalidate������")