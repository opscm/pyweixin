## 介绍  
基于python3写的发送微信消息的脚本，可用于zabbix微信报警等场景
  
## 准备工作  
* 安装python3  
* 注册一个微信企业号并在企业号后台创建一个APP

## 使用说明
* 首先要添加联系人到微信企业,且联系人关注微信企业号才能发送消息
* 消息换行符为 -n
* CORPID CORPSECRET APPID等参数登陆微信企业号后台可以查看

命令格式：
`python3 pyweixin.py CORPID CORPSECRET APPID 联系人 消息内容`
