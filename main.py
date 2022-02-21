import url2WebVpn
import pyperclip

welcome = '''
  _      ________  ____________  _      __    __ _   _____  _  __
 | | /| / / __/ / / / __/_  __/ | | /| / /__ / /| | / / _ \/ |/ /
 | |/ |/ / _// /_/ /\ \  / /    | |/ |/ / -_) _ \ |/ / ___/    / 
 |__/|__/_/  \____/___/ /_/     |__/|__/\__/_.__/___/_/  /_/|_/  
 
潍坊科技学院图书馆电子资源授权访问系统 代理链接快速生成工具  V22.2.20
快速使用说明：识别剪切板内URL信息将其转换为代理地址后拷贝回剪切板
'''

print(welcome)

gUrl = url2WebVpn.url2WebVpn('zy.wfust.edu.cn:81', 'http')

while True:
    print('-------------------------------------------------------')
    targetUrl = pyperclip.paste()
    # 判断是否为URL
    if gUrl.isUrl(targetUrl) == False:
        print('当前剪切板内不是有效链接！')
        str = input('按回车键继续...')
        continue

    # 判断当前URL是否为代理系统内
    print('当前识别URL: '+ targetUrl)
    if gUrl.isWebVpnUrl(targetUrl):
        print('当前剪切板内已是代理系统链接！')
        str = input('按回车键继续...')
        continue

    proxyUrl = gUrl.generateWebVpnUrl(targetUrl)
    print('当前代理URL: '+ proxyUrl)
    pyperclip.copy(proxyUrl)
    str = input('按回车键继续...')

