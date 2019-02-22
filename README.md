# elasticsearch-query-dsl-test
elasticsearch 使用 query dsl 进行查询优选的demo

### 提高精度
匹配包含任意个数查询关键字的文档可能会得到一些看似不相关的结果，这是一种霰弹策略(shotgun approach)。然而我们可能想得到包含所有查询关键字的文档。换句话说，我们想得到的是匹配'brown AND dog'的文档，而非'brown OR dog'。
match查询接受一个'operator'参数，默认值为or。如果要求所有查询关键字都匹配，可以更改参数值为and：
GET /my_index/my_type/_search
{
    "query": {
        "match": {
            "title": {      <1>
                "query":    "BROWN DOG!",
                "operator": "and"
            }
        }
    }
}

<1> 为了加入``'operator'``参数，``match``查询的结构有一些不同。


### 精确匹配
match_phrase
{
  "query": {
    "match_phrase": {
        "content" : {
            "query" : "我的宝马多少马力"
        }
    }
  }
}



参考资料：
https://es.xiaoleilu.com/100_Full_Text_Search/10_Multi_word_queries.html
https://www.cnblogs.com/bonelee/p/6105394.html

