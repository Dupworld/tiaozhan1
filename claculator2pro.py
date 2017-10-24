#! /usr/bin/env python3
import sys

bxtable={'yanglao':0.08,'yiliao':0.02,'shiye':0.005,'gongshang':0,'shengyu':0,'gongjijin':0.06}

shuitable=[
    (80000, 0.45, 13505),
    (55000, 0.35, 5505),
    (35000, 0.30, 2755),
    (9000, 0.25, 1005),
    (4500, 0.2, 555),
    (1500, 0.1, 105),
    (0, 0.03, 0)
]


def gzjs():
    wx=gz*sum(bxtable.values())
    suode=gz-wx-3500
    
    for suodee in shuitable:
        if suode>suodee[0]:
            shui=suode*suodee[1]-suodee[2]
            sjgz=format((gz-wx-shui),".2f")
            return sjgz

        elif suode<=0:
            sjgz=format((gz-wx),'.2f')
            return sjgz

for a in  sys.argv[1:]:
    try:
        gh=a.split(':')[0]
        gz=int(a.split(':')[1])
    except ValueError:
        print("Parameter Error")
        exit()
    ds=gzjs()
    print (gh,ds,sep=":")
