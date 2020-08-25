# -*- coding: utf-8 -*-
from mathmatic import plus
from mathmatic import subtract
from datapreprocessing import processing
from datapreprocessing import importdata

a=3
b=4

def main():
    print("~~사칙 연산을 시작합니다~~")
    print("a - b=", subtract.minus(a,b))
    print("a + b =", plus.add(a, b))
    print("~~사칙 연산을 종료합니다~~")

data=importdata.readData()
processing.process_data(data)

if __name__=="__main__":
  main()
