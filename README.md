# Fraud Detection System 🔍💳

## 🚨 Why This Project Matters
Financial fraud is one of the biggest challenges in modern banking and e‑commerce. Traditional rule‑based systems often fail to detect complex fraud patterns, especially when fraudsters exploit relationships between accounts and transactions.  
This project builds a **hybrid fraud detection pipeline** that combines **Graph Neural Networks (GNN)** for relational learning with **XGBoost** for classification, delivering a scalable and explainable solution.

---

## ⚙️ Features
- **Transaction Graph Builder** – converts raw transaction data into graph structures
- **Feature Engineering Pipeline** – extracts statistical and relational features
- **Hybrid Model** – GNN for embeddings + XGBoost for classification
- **FastAPI Service** – REST API for real‑time predictions
- **Explainability** – SHAP values for model transparency
- **Streaming Integration** – Kafka producer/consumer for live transaction feeds
- **Database Layer** – PostgreSQL schema for transaction storage

---

## 🛠️ Tech Stack
- **Python 3.12**
- **PyTorch + PyTorch Geometric**
- **XGBoost**
- **FastAPI + Uvicorn**
- **Kafka**
- **PostgreSQL**
- **Docker & Docker Compose**

---

## 🚀 Getting Started
Clone the repo and set up your environment:

```bash
git clone https://github.com/vedantk28/fraud-detection-system.git
cd fraud-detection-system
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
