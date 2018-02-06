# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 14:09:59 2018

@author: Administrator
"""
import urllib
class HtmlDownloader(object):
    
    def download(self,url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        
        if response.getcode() != 200:
            return None
        
        return response.read()
    
    