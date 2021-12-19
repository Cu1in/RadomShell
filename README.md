# RadomShell

##python免杀

随机对Cobaltstrike生成的Powershell进行免杀.最高可全国Virustotal

使用Cobaltstrike生成Powershell.ps1文件,随后使用脚本进行免杀

python mian.py

将他们整体Base64编码,然后随机分离,生成免杀后的powershell.ps1生成的文件结果每次都是随机.有时候生成的变量可能达到上百个。

经过Virustotal检测,已经过了很多杀软了

##使用py2exe生成exe

ps2exe项目地址如下

https://github.com/MScholtes/PS2EXE.git

存在图形化操作界面,我们直接使用即可,成功生成XXX.exe文件

最终成功生成一个EXE文件,经测试绕过了360,火绒等绝大多数杀软，并且可以正常加载。

##详细使用介绍地址:https://mp.weixin.qq.com/s/znyLqniUX_WXRizGV6TQlA


