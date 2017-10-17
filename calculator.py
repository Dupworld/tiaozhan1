#! /usr/bin/env python
import sys
try:
    gz=int(sys.argv[1])
    suode=gz-3500
except:
    print("Parameter Error")
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
print (format((shui),".2f"))
