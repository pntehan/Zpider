# -*- coding:utf-8 -*-
# author:Pntehan


import socks
from urllib.parse import urlparse
from Zpider import config as C
from lxml import etree

def get(url, user_agent=False, proxy_ip=False, timeout=3, retry=3):
    # 通过socket请求网页
    if url == "why is Zpider":
        print("Because I love ZJ.")
        return
    host, path = parse_url(url)
    if path == "":
        path = "/"
    if isinstance(retry, int):
        r = 0
        while r < retry:
            flag, data = connect_server(host, path, user_agent, proxy_ip, timeout)
            if flag:
                break
            print(">>>服务器未响应，第{}次重试...".format(r+1))
            r += 1
        assert flag, data
    html_headers = data.decode().split('\r\n\r\n')[0]
    html_data = data.decode().split('\r\n\r\n')[1]
    return {"header": html_headers, "text": html_data, "etree": etree.HTML(html_data), "content": data}

def connect_server(host, path, user_agent, proxy_ip, timeout):
    # 通过socket连接服务器
    client = socks.socksocket()
    if user_agent == "default":
        # 使用自带的代理头
        from random import randint
        user_agent = C.USER_AGENT[randint(0, len(C.USER_AGENT) - 1)]
    elif not user_agent:
        user_agent = ""
    if proxy_ip:
        # 使用自带的代理ip地址
        proxy_ip = C.IP[randint(0, len(C.IP) - 1)]
        client.setproxy(socks.HTTP, proxy_ip.split(":")[0], int(proxy_ip.split(":")[1]))
    if isinstance(timeout, int):
        # 设置超时时间
        client.settimeout(timeout)
    try:
        client.connect((host, 80))
        mess = "GET {} HTTP/1.1\r\n"\
               "Host: {}\r\n"\
               "User-Agent: {}\r\n"\
               "Connection: close\r\n\r\n".format(path, host, user_agent)
        print(mess)
        client.sendall(mess.encode())
        data = b""
        while True:
            d = client.recv(1024)
            if d:
                data += d
            else:
                break
        client.close()
        return True, data
    except Exception as e:
        client.close()
        return False, Exception("连接错误，可能是连接超时，可能是主机拒绝您的请求，可以更换请求头或者代理ip重新尝试...")

def parse_url(url):
    # 分析网页地址，返回域名和路径
    url = urlparse(url)
    return url.netloc, url.path


