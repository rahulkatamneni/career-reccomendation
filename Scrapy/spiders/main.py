#!/usr/bin/env python
# -*- coding: utf-8 -*-
#coding=utf-8

from scrapy import cmdline
def main(name):
    if name:
        cmdline.execute(name.split())



if __name__ == '__main__':
    print('[*] beginning main thread')
    name = "scrapy runspider stack_spiderDemo.py"
    #name = "scrapy crawl spa"
    main(name)
    print('[*] main thread exited')
    print('main stop====================================================')