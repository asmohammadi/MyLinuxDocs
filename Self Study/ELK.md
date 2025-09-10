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
PUT /products # Create an index(Table)
GET /_cat/indices # List indexes
GET /_cat/nodes # List Elastics nodes (servers)
GET /_cat/health # Check node health
DELETE /products # Delete index
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





