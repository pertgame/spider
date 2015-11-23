__author__ = 'thunder'
# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import pdb
import tagtool
import os
#下载chinaunix 指定id的blog所有文章
#http://blog.chinaunix.net/uid/293474.html

class ChinaUnix:
    #初始化方法
    def __init__(self):
        self.base_blog_url = "http://blog.chinaunix.net"
        self.uid = 293474
        self.base_uri  = "/uid/" + str(self.uid) + "/abstract/"
        self.first_uri = self.base_uri + "1.html"
        
        self.first_page_url = self.base_blog_url + self.first_uri

        self.max_page = 1
        self.tool = tagtool.Tool()
        self.article_urls = []
 
    #获取所有页数信息
    def get_max_page_num(self, page):
        pattern = re.compile('<li class="page selected">.*?class="last">.*?href="(.*?)\.html">',re.S)
        result = re.search(pattern, page)
        last = result.group(1)
        ss = last.split("/")
        self.max_page = int(ss[len(ss)-1])
        print "get max page:", self.max_page

    def get_url_data(self, url):
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        page = response.read().decode('utf-8')
        return page        

    def get_all_pages(self):
        page = self.get_url_data(self.first_page_url)
        self.get_max_page_num(page)
   
    def parse_article_url(self, page):
        #todo: 从每页数据中，把每篇文章的url和title取下来保存
        #pattern = re.compile('<td class="Blog_td1">.*?href="(.*?)">(.*?)</a>',re.S)
        pattern = re.compile('<td class="Blog_td1">.*?href="(.*?)">(.*?)</a>.*?<td>(.*?)</td>',re.S)
        result = re.findall(pattern,page)
        for item in result:
            print "----------------------------"
            print "url:",item[0]
            print "title:",item[1]
            print "read:",item[2]
            self.article_urls.append((self.base_blog_url + item[0], item[1]))
        #self.article_urls = []

    def get_all_article_list(self):
        for i in range(1, self.max_page + 1):
            url = self.base_blog_url + self.base_uri + str(i) + ".html"
            print "url:",url
            page = self.get_url_data(url)
            self.parse_article_url(page)
    def down_all_articles(self):
        #todo 获取每篇文章内容，并保存下来
        base_path = "./blogs/"
        os.system("mkdir -p " + base_path)

        pattern = re.compile('<div class="Blog_wz1".*?>(.*?)</div>',re.S) 
        for item in self.article_urls:
            title = item[1].replace("/","&")
            url   = item[0]
            page = self.get_url_data(url)
            result = re.search(pattern, page)
            content = result.group(1).strip()
            content = self.tool.replace(content)
            content = content.replace("&nbsp;"," ")
            f = open(base_path + title + ".txt" , "w")
            f.write(content.encode('utf-8'))
            f.close()

    #程序运行主干
    def main(self):
        self.get_all_pages()
        self.get_all_article_list()
        self.down_all_articles()

chinaunix = ChinaUnix()
chinaunix.main()
