# Prometheus Concepts

### Prometheus:
> Prometheus is an open-source monitoring and alerting system designed to collect and store metrics data (e.g., CPU usage, memory consumption, number of HTTP requests).

Key Features:
* Stores data in a `time-series database`
* Collects metrics `using a pull model` (Prometheus scrapes targets)
* Uses a powerful query language: `PromQL`
* Integrates well with Kubernetes, Docker, Grafana, and other DevOps tools

### 📚 Core Concepts of Prometheus

1️⃣ **Metrics**
* Numeric data about the state of a system/service at a specific time.
* Example: `cpu_usage=60%`, `http_requests_total=12345`

2️⃣ **Time-Series**
* Metrics stored along with a `timestamp`.
* Example:
  ```sh
  12:00 → cpu_usage=40%
  12:01 → cpu_usage=42%
  ```

3️⃣ **PromQL (Prometheus Query Language)**
* A query language designed for Prometheus to filter and analyze metrics.
* Example:
  ```sh
  rate(http_requests_total[5m]) # Average rate of HTTP requests over the past 5 minutes.
  ```

4️⃣ **Scraping**
* The process of collecting metrics from a target endpoint by Prometheus.
* Services must expose a `/metrics` endpoint.
* Example: `http://localhost:9100/metrics`

5️⃣ **Exporter**
* A tool that exposes metrics from a system/service in a Prometheus-compatible format.
* Common examples:
  * `Node Exporter` : system metrics (CPU, memory, disk)
  * `cAdvisor` : Docker container metrics
  * `Kube-State-Metrics` : Kubernetes metrics

6️⃣ **Targets**
* The list of services or IPs Prometheus scrapes metrics from.
* Defined inside the `prometheus.yml` configuration file.

7️⃣ **AlertManager**
* Prometheus component for handling alerts.
* Allows defining rules & conditions (e.g., CPU > 90%).
* Can send alerts via Email, Slack, PagerDuty, etc.

8️⃣ **Grafana Integration**
* Prometheus handles collection and queries.
* `Grafana` is used to build visual dashboards on top of Prometheus data.

9️⃣ **Retention & Storage**
* Prometheus stores metrics data locally on disk.
* Best suited for `short-term storage` (e.g., 15 days).
* For long-term retention, external tools like `Thanos` or `VictoriaMetrics` are used.

🔟 **Service Discovery**
* Especially critical in `Kubernetes`.
* Prometheus can automatically discover services and pods to scrape metrics from.

# 🎯 Summary

To get started with Prometheus monitoring, you should focus on these key areas:

* Metrics and Time-Series
* PromQL (querying data)
* Scraping and Exporters
* Targets configuration
* Alertmanager
* Grafana integration




