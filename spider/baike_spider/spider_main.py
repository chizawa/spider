# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 14:11:11 2018

@author: Administrator
"""
from baike_spider import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain():
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    #爬虫的调度程序
    def craw(self,root_url,maxitem=100,output_form='text'):
        '''
            root_url  -   启动url
            maxitem   -   获取的词条个数
            output_form   -   输出格式('text','table')
        '''
        
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw '+str(count)+new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                
                if count == maxitem:
                    break
                count += 1
        
            except Exception as e:
                print('craw failed')

        self.outputer.output_html(output_form)

if __name__ =="__main__":
    root_url = "https://baike.baidu.com/item/Python/407313?fr=aladdin"  #入口url
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)  #启动爬虫