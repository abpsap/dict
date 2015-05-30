#!/usr/bin/env python3

import os
import demo2
import try1
import samp1



def main ():
#    std_dict = (Anand="10", John="50", Mary="35", Tom="70")
    #print (std_dict["Mary"])
    try1.call_try1()
    demo2.demoex2()
    samp1.rand1()

    str1 = "My name is python"
    samp1.strprnt(str1)
    print ("In main: ", str1)
    str1 = samp1.strprnt(str1)
    print ("In main: ", str1)

main()

