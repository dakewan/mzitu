# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import requests,os
base_path = 'F:\mzitu'
class MzituPipeline(object):
    def process_item(self, item, spider):
        # print(item['title'],item['img_url'])
        title = item['title']
        url = str(item['img_url'])
        if os.path.exists(os.path.join(base_path,item['title'])):
            pass
        else:
            os.makedirs(os.path.join(base_path,item['title']))
        dict = url.rsplit('/', maxsplit=1)
        file_name = os.path.join(base_path,title,dict[1])

        if os.path.exists(file_name):
            pass
        else:
            response = requests.get(url=url, headers={'Referer': 'http://www.mzitu.com/net/'})
            print('正在下载', title, '......')
            with open(file_name,'wb') as f:
                f.write(response.content)
            print('下载完成.')
        raise DropItem()
