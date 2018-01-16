# -*- coding:utf-8 -*-
import openpyxl

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import time
import argparse
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

input_file = u'E:/工作目录/pydata-book-2nd-edition/datasets/usda_food/database.json'
# 设置mapping
def set_mapping(es, index_name="content_engine", doc_type_name="en"):
    my_mapping = {
        "en": {
            "properties": {
                "content": {
                    "type": "string"
                },
                "url": {
                    "type": "string"
                }
            }
        }
    }

    # 创建Index和mapping
    create_index = es.indices.create(index=index_name, body=my_mapping)  # {u'acknowledged': True}
    mapping_index = es.indices.put_mapping(index=index_name, doc_type=doc_type_name,
                                           body=my_mapping)  # {u'acknowledged': True}
    if create_index["acknowledged"] != True or mapping_index["acknowledged"] != True:
        print "Index creation failed..."

        # 将文件中的数据存储到es中


def set_date(es, input_file, index_name="content_engine", doc_type_name="en"):
    # 读入数据
    line_list = open(input_file).read()

    # 创建ACTIONS
    ACTIONS = []
    for line in line_list:
        fields = line.split("\t")
        # print fields[1]
        action = {
            "_index": index_name,
            "_type": doc_type_name,
            "_source": {
                "url": fields[0],
                "content": fields[1]}
        }
        ACTIONS.append(action)

        # 批量处理
    success, _ = bulk(es, ACTIONS, index=index_name, raise_on_error=True)
    print('Performed %d actions' % success)


# 读取参数
def read_args():
    parser = argparse.ArgumentParser(description="Search Elastic Engine")
    parser.add_argument("-i", dest="input_file", action="store", help="input file1", required=True)
    # parser.add_argument("-o", dest="output_file", action="store", help="output file", required=True)
    return parser.parse_args()


if __name__ == '__main__':
    args = read_args()
    es = Elasticsearch(hosts=["192.168.129.128:9200"], timeout=5000)
    set_mapping(es)
    set_date(es, args.input_file)