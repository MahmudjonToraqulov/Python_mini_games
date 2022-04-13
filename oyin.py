# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 16:32:17 2022

@author: User
"""
a = " *** Pyhonda birinchi yaratgan o'yinim!!! Baho berasilar Biznessmenlar !!! by Mahmoodjan *** "

import random as r
komResult = 0
userResult = 0
while True:
    print(f"     \n  *** Keling o'yin o'ynaymiz!!! ***\n\n "
          f" 1 dan 100 gacha son o'yladim topingchi! ")
    
    taxKomp = r.randint(1, 100) 
    sonTax = 1
    while True:
        taxUser = int(input(" -> "))
        if taxKomp < taxUser:
            sonTax += 1
            print( f" Men o'ylagan son {taxUser} dan kichik!!! ")
            continue
        elif taxKomp > taxUser:
            sonTax += 1
            print( f" Men o'ylagan son {taxUser} dan katta!!! ")
            continue
        else:
            print(f" Javobingiz to'g'ri!!! Siz {sonTax} ta uriniwda toptingiz!!! \n")
            break
    
    
    print(f" Endi siz oylang men topaman!!! Endi men sizdan so\'rayman iltimos adolatli bo'ling!!! \n ")
    
    
    kompTax2 = r.randint(1, 10)
    kompTaxSon = 1
    while True:
        userNum = input(f" Siz o'ylagan son {kompTax2} mi? ({kompTax2} dan katta -> k) ({kompTax2} ga teng -> t) ({kompTax2} dan kichik -> kic): ")
        if userNum == 'k':
            kompTax2 = r.randint(kompTax2, 10)
            kompTaxSon += 1
            continue
        elif userNum == 'kic':
            kompTax2 = r.randint(1,kompTax2)
            kompTaxSon += 1
            continue
        else:
            print(f" \n Qoyil! Men {kompTaxSon} ta urinishda toptim \n")
            break
       
    print(f" Kompyuter urinishlari soni -> {kompTaxSon} "
          f" Ishtirokchi urinishlari soni -> {sonTax} "      
          )
    
    if kompTaxSon > sonTax:
        print(f" Siz yutdingiz!!! ")
        userResult += 1
    elif kompTaxSon == sonTax:
        print(f" Durang!!! ")
    else:
        print(f" Men yutdim!!! ")
        komResult += 1
        
    print(f"\n Umumiy hisob:\n Kompyuter -> {komResult}\n Ishtirokchi -> {userResult}\n ")
    req = input( " Yana o'ynashni xohlaysizmi? ( yes/no ) " )
    
    if req == 'yes':
        continue
    elif req == 'no':
        break













