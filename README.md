# 🛡 Intrusion Detection System (IDS) – Anomaly Detection

A Machine Learning-based Intrusion Detection System (IDS) that classifies network traffic as **Normal** or **Anomalous (Attack)** using the **NSL-KDD dataset**.

This project demonstrates a complete end-to-end ML deployment pipeline including:

- Data preprocessing  
- Model training (Random Forest)  
- FastAPI backend  
- Docker containerization  
- Cloud deployment (Render)  
- API documentation  

---

# 📌 Project Overview

The IDS analyzes network traffic features and predicts whether the traffic is legitimate or malicious.

##  Workflow

1. Data preprocessing  
2. Feature encoding and scaling  
3. Model training (Random Forest Classifier)  
4. Model evaluation  
5. Model serialization (`.pkl`)  
6. FastAPI API integration  
7. Docker containerization  
8. Deployment on Render  

---

# 📊 Dataset

Dataset Used: **NSL-KDD**

Files:

- `KDDTrain+.txt` – Training dataset  
- `KDDTest+.txt` – Testing dataset  
- `kddcup.names` – Feature names  

The NSL-KDD dataset is an improved version of the KDD Cup 1999 dataset and is widely used for intrusion detection research.

---

## 🌐 Live API

🔗   
https://ids-api-rx23.onrender.com/docs


---

## 📦 Docker Hub Repository

🔗 https://hub.docker.com/repository/docker/kanyewest69/ids-api/general

---

