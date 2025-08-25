# ELK Stack Concepts:

### Core Concepts of the ELK Stack (Elasticsearch + Logstash + Kibana)

1. `Elasticsearch`
* A distributed search and analytics engine.
* Stores log data in JSON format, indexes it for fast search, and supports queries/aggregations.
* Key concepts:
   * `Cluster` → group of Elasticsearch nodes.
   * `Node` → single instance of Elasticsearch.
   * `Document` → individual log entry in JSON.
   * `Index` → A logical namespace for data (like a database).
   * `Shard` → A physical partition of an index. (provides scalability and distribution).
   * `Replica` → A copy of a shard for redundancy and high availability.

2. `Logstash`
* A server-side data processing pipeline.
* Collects logs from multiple sources, processes/transforms them, and sends them to Elasticsearch (or other destinations).
* Key concepts:
  * `Input plugins` → define where data comes from (e.g., syslog, filebeat, TCP, Kafka).
  * `Filter plugins` → process/transform data (e.g., Grok, JSON, Mutate, Date).
  * `Output plugins` → define where data goes (e.g., Elasticsearch, file, stdout).
  * `Pipeline` → the complete flow of input → filter → output.

3. `Kibana`
* A web-based visualization and dashboard tool for Elasticsearch.
* Allows searching, analyzing, and visualizing data stored in Elasticsearch.
* Key features:
  * `Discover` → query/search logs interactively.
  * `Visualize` → create graphs, charts, and maps.
  * `Dashboard` → combine multiple visualizations into one view.
  * `Alerts` → trigger alerts based on conditions.

4. `Beats` (optional but common in production)
* Lightweight agents installed on servers.
* Ship logs/metrics directly to Logstash or Elasticsearch.
* Types:
  * `Filebeat` → ships log files(Nginx, Apache, MySQL).
  * `Metricbeat` → ships system and service metrics(CPU, memory).
  * `Packetbeat` → ships network traffic data.
  * `Winlogbeat` → ships Windows event logs.

5. `Grok Pattern`
  Convert normal logs:
  ```sh
  192.168.1.10 - - [19/Aug/2025:10:30:12 +0200] "GET /index.html HTTP/1.1" 200 1024
  ```
  into JSON format:
  ```json
  {
  "client_ip": "192.168.1.10",
  "timestamp": "19/Aug/2025:10:30:12 +0200",
  "method": "GET",
  "url": "/index.html",
  "status": "200",
  "bytes": "1024"
  }
  ```
6. `Index Lifecycle Management` (ILM)
* Controls how indices are rolled over, retained, and deleted (hot, warm, cold phases).
7. `Scaling & Performance`
* `Elasticsearch Cluster` → consists of one or more nodes.
  * `Master Node` → manages the cluster and metadata.
  * `Data Node` → stores data and executes queries.
  * `Ingest Node` → processes data before indexing.
  * `Coordinating Node` → (handles client requests).
* `Sharding` → splits data across nodes for load balancing.
* `Replication` → increases availability and redundancy.
8. `Monitoring & Alerting`
* `X-Pack` (Elastic Stack Plugin) → used for security, monitoring, and alerting.
* `Watcher` → configure alerts (e.g., send an email if the number of error logs spikes).
* `Grafana Integration` → Elasticsearch can be connected to Grafana for more advanced dashboards.



