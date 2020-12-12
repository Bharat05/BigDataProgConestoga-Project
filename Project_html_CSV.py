#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 16:52:37 2020

Project : PROG8420 - Programming for Big Data


@author: dev
"""

import html2text
import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'https://www.toyota.ca/toyota/en/frequently-asked-questions')

h_str = r.data.decode('utf-8')
h = html2text.HTML2Text()
str_faq = 'Frequent'
end_faq = '#### Contact Us'
q_str = ''
faq_list = {}
in_faq = 0

for s in h.handle(h_str).split('\n') :
    if len(s) > 0 :
        if in_faq == 0 :
            if s.find(str_faq) != -1 :
                in_faq = 1
            continue
        if in_faq == 1 :
            if s.find(end_faq) != -1 :
                break
            if s[-1] == '?' : # Question found
                q_str = s
                faq_list[q_str] = ''
                continue
            if q_str != '' : # Answer part
                faq_list[q_str] = faq_list[q_str] + ' ' + s

#Print FAQ ins CSV format - first & second field embedded in quote as comma is data
for k,v in faq_list.items() :
    print('"'+k.replace('#','').replace('*','').lstrip()+'","'+v.replace('#','').lstrip()+'"')
     
        
    
