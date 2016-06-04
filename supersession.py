#!/usr/bin/env python
#-*- coding: utf-8 -*-
if __name__ != "__main__":
	import requests, cookielib, re, random
	from getpass import getpass

	class SuperSession(requests.Session):

		def __init__(self):
			requests.Session.__init__(self)
			self.login_url = "http://www.zhihu.com"
			self.cookies = cookielib.CookieJar()
			self.post_data = {}

		def get_xsrf(self)	:
			response = self.get("http://www.zhihu.com")
			if response.status_code != 200:
				exit("Get www.zhihu.com failed!")
			self.post_data["_xsrf"] = re.search(r"name=\"_xsrf\" value=\"(.+?)\"", response.content).group(1)
			return self

		def get_info(self):
			account = raw_input("Please input your account: ")
			if re.match(r".+@.+", account):
				self.account_type = "email"
			else:	
				self.account_type = "phone_num"
			self.post_data[self.account_type] = account
			self.post_data["password"] = getpass("Please input your password: ")
			return self

		def get_captcha(self):	
			response = self.get("https://www.zhihu.com/captcha.gif", params = {"type": "login"}, verify = False)
			if response.status_code != 200:
				exit("Get captcha failed!")
			open("captcahr.gif", "wb").write(response.content)
			self.post_data["captcha"] = raw_input("Please input the captcha: ")
			return self

		def login(self):
			self.post("http://www.zhihu.com/login/" + self.account_type, data = self.post_data, verify = False, headers = {
				"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36",
				"Host": "www.zhihu.com",
				"Origin": "http://www.zhihu.com",
				"Pragma": "no-cache",
				"Referer": "http://www.zhihu.com/",
				"X-Requested-With": "XMLHttpRequest"
				})
			return self

		def do(self):
			self.get_xsrf().get_info().get_captcha().login()
			return self
else:
	exit("It need to be loaded as a module!(`python index.py`)")