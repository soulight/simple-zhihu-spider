#!/usr/bin/env python
#-*- coding: utf-8 -*-
if __name__ == "__main__":

	from supersession import SuperSession	

	session = SuperSession()
	response = session.do().get("http://www.zhihu.com", headers = {
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36",
		"Host": "www.zhihu.com",
		"Origin": "http://www.zhihu.com",
		"Pragma": "no-cache",
		"Referer": "http://www.zhihu.com/",
		"X-Requested-With": "XMLHttpRequest"
		}, verify = False)
	open("index.html", "wb").write(response.content)
