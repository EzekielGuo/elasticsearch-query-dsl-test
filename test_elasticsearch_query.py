from elasticsearch import Elasticsearch
import time
import datetime
import os

def elastic(ip,port,index):
    es = Elasticsearch([{'host': 'xx', 'port': 9200, 'timeout': 10000}])
    keyword = "down"
    doc = {
        "query": {
            "bool":{
                "must":[
                    {
                        "match":{
                            "host":{
                                "query":ip,
                                "operator":"and"
                            }

                        }
                     },
                    {
                        "match_phrase":{
                            "message":{
                                "query":port
                            }
                        }
                    },
                    {
                        "match":{
                            "message":{
                                "query":keyword,
                                "operator":"and"
                            }
                        }
                    },
                ]
            }
        },
        "from": 0,
        "size": 1000,
    }
    result = es.search(index=index,body=doc)
    count = 0
    for result_single in result['hits']['hits']:
        print(result_single)
        print(' ')
        host = result_single["_source"]["host"]
        time = result_single["_source"]["@timestamp"]
        index = result_single["_index"]
        message = result_single["_source"]["message"]
        count += 1
        print(count)
        print(host)
        print(time)
        print(message)
        print(' ')




ip = "211.99.160.10"
port = "xe-3/0/3"
# index = es_index
index = 'ordinary-2019.01*'
elastic(ip,port,index)




