# Synthetic Monitoring Platform

A Python-based **synthetic monitoring platform** that periodically runs `ping` commands, stores metrics in **Prometheus**, and visualizes them in **Grafana** for real-time network performance insights.

This project was built as part of the Build Fellowship program and emphasizes **DevOps**, **observability**, and **site reliability engineering** concepts.

---

## 📌 Table of Contents
- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Learning Outcomes](#learning-outcomes)
- [License](#license)

---

## 📖 About
I built this platform as part of the **Build Fellowship program**, where I took upon the role of a Software Developer under the guidance of an experienced Build Fellow (Sonu Gupta).  

The project simulates the operations of a real software development team and focuses on **DevOps** and **observability** practices. We developed a **synthetic monitoring platform** in Python that uses `ping` to measure network performance, exports the results to **Prometheus**, and visualizes them in **Grafana**.  

This hands-on project helped me gain industry-relevant experience with:
- Writing Python monitors for early problem detection.  
- Configuring Prometheus and creating PromQL queries.  
- Building Grafana dashboards for real-time observability.  
- Applying concepts of synthetic monitoring, site reliability engineering (SRE), and troubleshooting distributed apps.  

---

## ✨ Features
- Automated periodic `ping` execution.
- Prometheus metrics exporter for ping results.
- Real-time Grafana dashboards.
- Configurable monitoring intervals and targets.
- Supports multiple hosts.

---

## 🛠 Tech Stack
- **Python 3.x** — Synthetic monitor implementation.
- **Prometheus** — Time-series database for metrics.
- **PromQL** — Query language for analysis.
- **Grafana** — Visualization and dashboarding.

---

## 🏗 Architecture (will be updated soon)
[Python Script] → [Prometheus TSDB] → [Grafana Dashboards]
⚙️ Setup & Installation
1. Clone Repository
```
git clone https://github.com/deebran/synthetic-monitoring-platform.git
cd synthetic-monitoring-platform
```
3. Start Prometheus & Grafana (locally)
Instructions to install: 
    - [Prometheus](https://prometheus.io/docs/prometheus/latest/installation/)
    - [Grafana](https://grafana.com/docs/grafana/latest/setup-grafana/installation/)
4. Run the Python Synthetic Monitor
python ping_monitor.py
▶️ Usage
Edit config.yaml to change monitored targets and intervals.

Access Grafana at http://localhost:3000.

Access Prometheus at http://localhost:9090.

🎯 Learning Outcomes
By completing this project, I learned to:

Understand synthetic monitoring and its role in SaaS reliability.

Write Python scripts for automated network checks.

Configure and query Prometheus using PromQL.

Build Grafana dashboards for observability.

Apply project management and peer review workflows.

📄 License
This project is licensed under the MIT License.
See LICENSE for details.


---

