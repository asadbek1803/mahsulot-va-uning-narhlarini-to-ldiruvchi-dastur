# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 10:40:52 2022

@author: User 4
"""
print('Mahsulot va uning narhlarini to\'ldiruvchi dastur')
e_bozor={}
ishora=True
while ishora:
    mahsulot1=input('Mahsulotni nomini kiritning\n...')
    narhi=input(f"{mahsulot1.title()} ning narhini kiriting\n>>>> ")
    e_bozor[mahsulot1]= int(narhi)
    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
    if javob == "yo'q":
        ishora = False
