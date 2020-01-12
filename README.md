# Zpider

这里是Zpider的说明文档，您也可以访问这里
[Github-Zpider](https://github.com/pntehan/Zpider)
查看更多.
###Introduction
Zpider是一个非常简单的爬虫库，底层使用的是pysocks，使用socket.http连接方式，
进行get和post请求。在请求方式上采用的发送报文的方法。内容上还有许多不足，
但是在爬取简单的小网站时，还是可以的，在爬取比较正规的网站时。
会因为报文头部的格式的问题无法正确的连接，后续的改进会在头部信息进行优化。
####Config
配置文件里存放了部分的user-agent代理头供选择
####GET
该方法包括了六个参数：url, user_agent, proxy_ip, timeout, retry, cookies<br>
url：请求的连接地址<br>
user_agent：默认False不使用代理头，default使用配置文件的代理头，或者自行填写<br>
proxy_ip：默认False不使用代理ip，否则为"<ip>:<port>"格式传参<br>
timeout：设置链接时长，默认3s<br>
retry：重新连接次数，默认3次<br>
cookies：设置cookie，格式为字典格式<br>
该方法返回一个字典键值为：status, header, text, etree, content<br>
status：服务端响应状态<br>
header：为服务端响应头部<br>
text：解码之后的Html信息，字符串格式<br>
etree：html的树型结构，支持xpath路径直接获取元素<br>
content：未解码的数据，供于文件下载
####POST
POST方法和GET方式的形式大同小异<br>
该方法包括了六个参数：url, data, user_agent, proxy_ip, timeout, retry, cookies<br>
url：请求的连接地址<br>
data：发送报文的正文内容，格式为字典类型<br>
user_agent：默认False不使用代理头，default使用配置文件的代理头，或者自行填写<br>
proxy_ip：默认False不使用代理ip，否则为"<ip>:<port>"格式传参<br>
timeout：设置链接时长，默认3s<br>
retry：重新连接次数，默认3次<br>
cookies：设置cookie，格式为字典格式<br>
该方法返回一个字典键值为：status, header, text, etree, content<br>
status：服务端响应状态<br>
header：为服务端响应头部<br>
text：解码之后的Html信息，字符串格式<br>
etree：html的树型结构，支持xpath路径直接获取元素<br>
content：未解码的数据，供于文件下载<br>

