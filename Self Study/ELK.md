# ELK Stack (ElasticSearch, LogStash, Kibana)

### Create Docker Containers:
```sh
# Docker Compose file for creating ElasticSearch & Kibana containers:
version: '3.8'

services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:9.0.1
    container_name: elasticsearch
    environment:
      - node.name=es-node
      - discovery.type=single-node
      - cluster.name=es-cluster
      - network.host=0.0.0.0
      - xpack.security.enabled=false
      - xpack.security.enrollment.enabled=false
      - xpack.monitoring.collection.enabled=true
      - bootstrap.memory_lock=true
      - ES_JAVA_OPTS=-Xms1g -Xmx1g
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - esdata:/usr/share/elasticsearch/data
    ports:
      - 9200:9200
      - 9300:9300

  kibana:
    image: docker.elastic.co/kibana/kibana:9.0.1
    container_name: kibana
    ports:
      - 5601:5601
    environment:
      - SERVER_NAME=kibana
      - ELASTICSEARCH_HOSTS=http://elasticsearch:9200
    depends_on:
      - elasticsearch

volumes:
  esdata:
    driver: local
```

### ElasticSearch Concepts:
* `Node` : Each ElasticSearch Server
* `Shard` : Pieces of data splits on nodes
* `Replica` : Shards are keeping in replicas & distributing on all nodes
* `Index` : Tables
* `Docs` : Records in index



### ElasticSearch Commands:
```sh
PUT /product # Create an index(Table)
GET /_cat/indices # List indexes
GET /_cat/nodes # List Elastics nodes (servers)
GET /_cat/health # Check node health
DELETE /product # Delete index
GET /product/_search # List all data in an index
```
### Create Index & Document:
```sh
# Create a document in product index with ID 1:
POST /product/_doc/1
{
  "name":"Phone",
  "qty":250,
  "price":"500000",
  "cat":"digital"
}
GET /product/_doc/1 # List document with ID 
```

### Update Document:
```sh
# Update a document in index with ID:
POST /product/_update/1
{
  "doc": {
      "qty":150,
  }
}
```

### Add Multiple Documents in Index:(Bulk Insert)
```sh
PUT /products
POST /products_bulk
{"index":{"_id":100}}
{"name":"product1","price":150000,"qty":20}
{"index":{"_id":101}}
{"name":"product2","price":250000,"qty":30}
```
### Meta Field:
```sh
GET /products/_doc/100
# Result:
{
  "_index": "products",
  "-id": 100,
  "_version": 1,
  "_seq_no": 0,
  "_primary_term": 1,
  "found": true,
  "_source": {
   "price": 150000,
   "qty": 20,
   "name": "product1
  }
}
```

### Mapping:

**data types (Field Types)** : Types of variable
* `text` : for text
* `keyword`: for exact words
* `integer`, `long`, `float` : for number
* `boolean` : for true/false
* `date` : for date
* `object` : for array or complicated json
* `nested` : for array, better than `object`

**Dynamic Map:**
* Insert data without field types
* Field type will detect automatically

```sh
GET /products/_mapping # Display mappings
```

```sh
# Dynamic Mapping:
PUT /products/_mapping
{
  "properties":{
    "age":{
      "type":"integer"
    },
    "code":{
      "type":"long"
    }
  }
}
```

```sh
# Manual Mapping:
PUT /products/
{
    "mapping": {
        "dynamic":false,
        "properties":{
            "age":{
                "type":"long"
            },
            "name":{
                "type":"text"
            }
        }
    }
}
```

### Mapping Parameters:
* `dynamic` : True/False => Disable/Enable Dynamic Mapping
* `copy_to` : Field: FirstName , Field: LastName => Field: FullName = FirstName + LastName
* `coerce` : Field: integer => تبدیل به عدد صحیح می کند
    - "coerce": false => Disable it
* `format` : Date format
    - "type":"date,
    - "format":"yyyy/MM/dd HH:mm:ss||yyyy/MM/dd"
* `null_value` : "null_value":0 => Don't let the data to be null. Null data must have value.
* `norms` : True/False. Give score to data when searching.

### Multi Field:
```sh
"name": {
    "type": "text",
    "fields": {
        "keyword": {
            "type": "keyword"
        }
    }
}
```

### Analyzer:
> `Analyze` is a process in which ElasticSearch transforms the data into a searchable form in ElasticSearch.

**Steps of Analyzing:**
1. `Character Filters` : Removing extra characters
2. `Tokenizer` : Removing characters which has no meaning
3. `Token Filters` : Transform uppercase characters into lowercase

```sh
# Example of analyzing:
<strong>Two</strong> words! -> Two words! # Character Filter
Two words! -> [Two, words] # Tokenizer
[Two, words] ->  [two, words] # Token Filters
```









