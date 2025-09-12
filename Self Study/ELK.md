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

### Analyzing Sample:
```sh
POST _analyze
{
    "tokenizer": "standard",
    "text": "I'm in the mood for "
}
POST _analyze
{
    "filter": ["lowercase"],
    "text": <p>"I'm</p> in the mood for"
}
POST _analyze
{
    "char_filter": ["html_strip"],
    "text": <p>"I'm</p> in the mood for"    
}
```

### ElasticSearch Character Filters:

**Character filter reference:**
> Character filters are used to preprocess the stream of characters before it is passed to the tokenizer.

> A character filter receives the original text as a stream of characters and can transform the stream by adding, removing, or changing characters. For instance, a character filter could be used to convert Hindu-Arabic numerals (٠١٢٣٤٥٦٧٨٩) into their Arabic-Latin equivalents (0123456789), or to strip HTML elements like <b> from the stream.

> Elasticsearch has a number of built in character filters which can be used to build custom analyzers.

* `HTML Strip Character Filter` :
The html_strip character filter strips out HTML elements like <b> and decodes HTML entities like &amp;.
* `Mapping Character Filter` :
The mapping character filter replaces any occurrences of the specified strings with the specified replacements.
* `Pattern Replace Character Filter` :
The pattern_replace character filter replaces any characters matching a regular expression with the specified replacement.

### ElasticSearch Built in Tokenizers:

**Word Oriented Tokenizers:**
> The following tokenizers are usually used for tokenizing full text into individual words:
* `Standard Tokenizer` :
The standard tokenizer divides text into terms on word boundaries, as defined by the Unicode Text Segmentation algorithm. It removes most punctuation symbols. It is the best choice for most languages.
* `Letter Tokenizer` :
The letter tokenizer divides text into terms whenever it encounters a character which is not a letter.
* `Lowercase Tokenizer` :
The lowercase tokenizer, like the letter tokenizer, divides text into terms whenever it encounters a character which is not a letter, but it also lowercases all terms.
* `Whitespace Tokenizer` :
The whitespace tokenizer divides text into terms whenever it encounters any whitespace character.
* `UAX URL Email Tokenizer` :
The uax_url_email tokenizer is like the standard tokenizer except that it recognises URLs and email addresses as single tokens.
* `Classic Tokenizer` :
The classic tokenizer is a grammar based tokenizer for the English Language.
* `Thai Tokenizer` :
The thai tokenizer segments Thai text into words.

**Partial Word Tokenizers:**
> These tokenizers break up text or words into small fragments, for partial word matching:

* `N-Gram Tokenizer` :
The ngram tokenizer can break up text into words when it encounters any of a list of specified characters (e.g. whitespace or punctuation), then it returns n-grams of each word: a sliding window of continuous letters, e.g. quick → [qu, ui, ic, ck].
* `Edge N-Gram Tokenizer` :
The edge_ngram tokenizer can break up text into words when it encounters any of a list of specified characters (e.g. whitespace or punctuation), then it returns n-grams of each word which are anchored to the start of the word, e.g. quick → [q, qu, qui, quic, quick].

**Structured Text Tokenizers:**
> The following tokenizers are usually used with structured text like identifiers, email addresses, zip codes, and paths, rather than with full text:

* `Keyword Tokenizer` :
The keyword tokenizer is a noop tokenizer that accepts whatever text it is given and outputs the exact same text as a single term. It can be combined with token filters like lowercase to normalise the analysed terms.
* `Pattern Tokenizer` :
The pattern tokenizer uses a regular expression to either split text into terms whenever it matches a word separator, or to capture matching text as terms.
* `Simple Pattern Tokenizer` :
The simple_pattern tokenizer uses a regular expression to capture matching text as terms. It uses a restricted subset of regular expression features and is generally faster than the pattern tokenizer.
* `Char Group Tokenizer` :
The char_group tokenizer is configurable through sets of characters to split on, which is usually less expensive than running regular expressions.
* `Simple Pattern Split Tokenizer` :
The simple_pattern_split tokenizer uses the same restricted regular expression subset as the simple_pattern tokenizer, but splits the input at matches rather than returning the matches as terms.
* `Path Tokenizer` :
The path_hierarchy tokenizer takes a hierarchical value like a filesystem path, splits on the path separator, and emits a term for each component in the tree, e.g. /foo/bar/baz → [/foo, /foo/bar, /foo/bar/baz ].

### ElasticSearch Token Filters:

* Apostrophe
* ASCII folding
* CJK bigram
* CJK width
* Classic
* Common grams
* Conditional
* Decimal digit
* Delimited payload
* Dictionary decompounder
* Edge n-gram
* Elision
* Fingerprint
* Flatten graph
* Hunspell
* Hyphenation decompounder
* Keep types
* Keep words
* Keyword marker
* Keyword repeat
* KStem
* Length
* Limit token count
* Lowercase
* MinHash
* Multiplexer
* N-gram
* Normalization
* Pattern capture
* Pattern replace
* Phonetic
* Porter stem
* Predicate script
* Remove duplicates
* Reverse
* Shingle
* Snowball
* Stemmer
* Stemmer override
* Stop
* Synonym
* Synonym graph
* Trim
* Truncate
* Unique
* Uppercase
* Word delimiter
* Word delimiter graph

### Searching:
* `DSL` : Query DSL is a full-featured JSON-style query language that enables complex searching, filtering, and aggregations.
* `URI` : Query params 

**Bulk Add:**
```sh
POST _bulk
{"index": ....
    ....
}
```
**URI Search:**
```sh
GET /products/_search?q=*
GET /products/_search?q=name:*
GET /products/_search?q=name:NAME
GET /products/_search?q=tag:NAME
GET /products/_search?q=attribute:NAME
GET /products/_search?q=attribute:*
GET /products/_search?q=name:NAME AND description:2
```

**DSL (Domain Specific Language) Search:**
* `Leaf` : Simple search query
* `Compound` : Complicated search query.
  - `Boolean` : Multiple search queries.

```sh
# Example1:
GET /products/_search
{
  "query": {
    "match_all": {

    }
  }
}
```
```sh
# Example2:
GET /_search
{
  "query": {
    "query_string": {
      "query": "(new york city) OR (big apple)",
      "default_field": "content"
    }
  }
}
```
```sh
# Example3:
GET /_search
{
    "bool": {
        "must":     { "match": "fox"         },
        "should":   { "match": "quick brown" },
        "must_not": { "match": "news"        }
    }
}
```
```sh
# Example4:
GET /_search
{
  "query": {
    "query_string": {
      "fields": [ "content", "name" ],
      "query": "this AND that"
    }
  }
}
```

### Relevancy:
> A way of giving score to data which has been searched.

**Relevancy Algorithms:**
* `TF/IDF` : Score based on repeated terms in document or Index. `TF` Give more score based on the amount of terms in document. `IDF` Give low score based on the amount of terms in Index.
* `OKAPI/BM25` : Give score based on standards & principals.







