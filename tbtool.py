__author__ = 'CQC'
# -*- coding:utf-8 -*-

import re

#处理获得的宝贝页面
class Tool:

    #初始化
    def __init__(self):
        pass

    #获得页码数
    def getPageNum(self,page):
        pattern = re.compile('"totalPage":(.*?)}',re.S)
        result = re.search(pattern,page)
        if result:
            print "找到了共多少页"
            pageNum = result.group(1).strip()
            print '共',pageNum,'页'
            return pageNum

    def getGoodsInfo3(self,page):
        page = page.replace("true","True")
        page = page.replace("false","False")
        orders = eval(page)
        ors = orders["mainOrders"]
        for order in ors:
            createtime = order["orderInfo"]["createTime"]
            orderid    = order["extra"]["id"]
            fee        = order["payInfo"]["actualFee"]
            shopname   = order["seller"]["shopName"]
            status     = order["statusInfo"]["text"]
            goodsname  = "\n"
            for item in order["subOrders"]:
                goodsname += item["itemInfo"]["title"] + "\n"

            print '------------------------------------------------------------'
            print "购买日期:",createtime
            print '宝贝名称:',goodsname
            #goods = item[5].strip()
            print '订单号  :',orderid
            print '实际支付:',fee
            print '卖家店铺:',shopname
            print '交易状态:',status

    def getGoodsInfo2(self,page):
        pattern = re.compile(u'"createTime":"(.*?)","id":"(.*?)".*?"actualFee":"(.*?)".*?"shopName":"(.*?)".*?"text":.*?"text":.*?"text":"(.*?)".*?"subOrders":(.*?)},{"extra":')
        result = re.findall(pattern,page)
        for item in result:
            print '------------------------------------------------------------'
            print "购买日期:",item[0].strip()
            #print '宝贝名称:',item[5].strip()
            goods = item[5].strip()
            print '订单号  :',item[1].strip()
            print '实际支付:',item[2].strip()
            print '卖家店铺:',item[3].strip()
            print '交易状态:',item[4].strip()
    def getGoodsInfo(self,page):
        #u'\u8ba2\u5355\u53f7'是订单号的编码
        #u'\u67e5\u770b\u7269\u6d41' 查看物流
        #pattern = re.compile(u'dealtime.*?>(.*?)</span>.*?\u8ba2\u5355\u53f7.*?<em>(.*?)</em>.*?shopname.*?title="(.*?)".*?baobei-name">.*?<a.*?>(.*?)</a>.*?'
        #                     u'price.*?title="(.*?)".*?quantity.*?title="(.*?)".*?amount.*?em.*?>(.*?)</em>.*?trade-status.*?<a.*?>(.*?)</a>',re.S)
        pattern = re.compile(u'"createTime":"(.*?)","id":"(.*?)".*?"actualFee":"(.*?)".*?"shopName":"(.*?)".*?"text":.*?"text":.*?"text":"(.*?)".*?skuText":.*?"title":"(.*?)"')
        result = re.findall(pattern,page)
        for item in result:
            print '------------------------------------------------------------'
            print "购买日期:",item[0].strip()
            print '宝贝名称:',item[5].strip()
            print '订单号  :',item[1].strip()
            print '实际支付:',item[2].strip()
            print '卖家店铺:',item[3].strip()
            print '交易状态:',item[4].strip()
