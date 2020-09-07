#Coded By Jejak_Internet
#YouTube Jejak_Internet
#Vortex Indonesia
#coding: utf-8
import os,sys,time

 # KALAU MAU RECODE KASIH BINTANG DULU KE SCRIPT INI #

def main():
    time.sleep(1)
    os.system ('clear')
    print '[96m'
    os.system ('figlet Spam sms v1')
    print'[92m================================='
    print'[97m Author : [96mJejak Internet '
    print'[97m YouTube   : [96mJejak Internet '
    print'[97m Github : https://github.com/hadapan'
    print'[92m================================='
    print'[92m============ [97mM E N U [92m============='
    print'[92m[[97m1[92m] [97mSpam sms v1 '
    print'[92m[[91m0[92m] [91mExit '
    gans = raw_input ('[97m==>[93m ')
    if gans in ['1']:
        time.sleep(1)
        os.system ('git clone https://github.com/Yutixcode/Kangspam ')
        print 
        print (' [+] Silakan ketik cd Kangspam')
        print (' [+] Silakan ketik python run.py ')
        exit()
    if gans in ['0']:
        time.sleep(2)
        exit()
    else:
        time.sleep(1)
        print '[97m Pilih Yang Bener [92mBro . . .'
        time.sleep(1)
        main()

main()
