# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 14:10:42 2018

@author: Administrator
"""

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    

    def output_html(self,output_form):
        
        with open('output.html','w',encoding='utf-8') as fout:
            fout.write('<html>')
            fout.write('<body>')
            fout.write('<table>')
            
            #默认输出ascii
            for data in self.datas:
                if output_form =='table':
                    fout.write('<tr>')
                    fout.write('<td>%s</td>'%data['url'])
                    fout.write('<td>%s</td>'%data['title'])
                    fout.write('<td>%s</td>'%data['summary'])
                    fout.write('</tr>')
                    
                if output_form =='text':
                    fout.write('<a href = %s>%s</a>'%(data['url'],data['title']))
                    fout.write('<p>%s</p>'%data['summary'])
                
            fout.write('</table>')
            fout.write('</body>')
            fout.write('</html>')