#! /usr/bin/env python3
import sys
try:
    a=sys.argv[1]
    gh=int(a.split(':')[0])
    gz=int(a.split(':')[1])
except ValueError:
    print("Parameter Error")
    exit()

def gzjs():
    bx=0.08+0.02+0.005+0.06
    wx=gz*bx
    suode=gz-wx-3500

    if suode<=0:
        shui=0
    elif suode<=1500:
        shui=suode*0.03
    elif 1500<suode<=4500:
        shui=suode*0.1-105
    elif 4500<suode<=9000:
        shui=suode*0.2-555
    elif 9000<suode<=35000:
        shui=suode*0.25-1005
    elif 35000<suode<=55000:
        shui=suode*0.3-2755
    elif 55000<suode<=80000:
        shui=suode*0.35-5505
    elif suode>80000:
        shui=suode*0.45-13505
    sjgz=format((gz-wx-shui),".2f")
    return sjgz

for a in  sys.argv[1:]:
    try:
        gh=int(a.split(':')[0])
        gz=int(a.split(':')[1])
    except ValueError:
        print("Parameter Error")
        exit()
    ds=gzjs()
    print (gh,ds,sep=":")
