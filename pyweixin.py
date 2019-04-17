#!/usr/local/python3/bin/python3.5
import json
import sys
import os
import time
import urllib.request

tkapi      = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
msgapi     = 'https://qyapi.weixin.qq.com/cgi-bin/message/send'
corpid     = sys.argv[1]
corpsecret = sys.argv[2]
agentid    = sys.argv[3]
tokentmp   = '/tmp/token.txt'
url        = "%s?corpid=%s&corpsecret=%s" % (tkapi,corpid,corpsecret)
senduser   = sys.argv[4]
msg        = sys.argv[5]
nowtime    = int(time.time())

def gettoken():
	try:
		res = urllib.request.urlopen(url)
		if res.status == 200:
			result = res.read()
			result = str(result, encoding = "utf-8")
			jresult = json.loads(result)
			errcode = jresult['errcode']
			if errcode == 0:
				token = jresult['access_token']
				token = token.strip('\r')
				token = token.strip('\n')
				f = open(tokentmp,'w')
				log = "%s:%s" % (nowtime,token)
				f.write(log)
				f.close()
				return('0',token)
			else:
				return('1','get token fail')
		else:
			return('1','get token return http code error')
	except Exception as e:
		#print(Exception,":",e)
		return('1','get token http request fail')

def sendmsg(token,senduser,msg):
	SendMsgUrl = "%s?access_token=%s" % (msgapi,token)
	data = {'touser':senduser,'msgtype':'text','agentid':agentid,'text':{'content':msg}}
	data = json.dumps(data)  
	data = data.replace('-n','\\n')
	data = bytes(data,'utf8')

	try:
		request = urllib.request.Request(SendMsgUrl)  
		res1 = urllib.request.urlopen(request,data)
		if res1.status == 200:
			result1 = res1.read()
			result1 = str(result1, encoding = "utf-8")
			jresult1 = json.loads(result1)
			errcode1 = jresult1['errcode']
			if errcode1 == 0:
				return('0',errcode1)
			else:
				return('1','send msg fail')
		else:
			return('1','send msg return http code error')
	except:
		return('1','send msg http request fail')

if os.path.exists(tokentmp):		
	tk  = open(tokentmp,'r').readline()
	tk  = str(tk)
	tkstrs = tk.split(':')
	lasttime = int(tkstrs[0])
	if nowtime - lasttime < 3600:
		token = tkstrs[1]
		stat = '0'
	else:
		(stat,token) = gettoken()
else:
	(stat,token) = gettoken()



if stat == '0':
	(stat1,msgresult) = sendmsg(token,senduser,msg)
	if stat1 == '0':
		print('send message success')
	else:
		print('get token success,send message fail errinfo:'+msgresult)
else:
	print('get token fail errinfo:'+token)



