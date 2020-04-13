# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class BigchuangPipeline(object):
#     def process_item(self, item, spider):
#         return item
import pymysql


class PolicyPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host='localhost', user='root', passwd='pwd', db='db', charset='utf8')

        self.cursor = self.connect.cursor()
        print("success")

    def process_item(self, item, spider):
        insert_sql = """
        insert into POLICY(Title, Time, Articles) VALUES (%s,%s,%s)
        """
        self.cursor.execute(
            insert_sql, (item['title'],item['timee'],   item['articles']))

        self.connect.commit()

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
