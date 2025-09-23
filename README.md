# ETL_End_to_End


This project implements a complete **ETL (Extract, Transform, Load) pipeline** using **Python, MySQL, and GitHub Actions**.  
It automates the process of **collecting raw data**, **transforming it into structured formats**, and **ingesting it into a relational database** for further analysis (e.g., Power BI dashboards).


## 📂 Project Structure

ETL_End_to_End/
│
├── config/ # Database config & schema files
│ ├── db_config.json
│ └── schema.sql
│
├── data/ # Data layers
│ ├── raw/ # Raw datasets (collected)
│ ├── processed/ # Intermediate cleaned data
│ └── gold/ # Final transformed datasets (Excel/JSON)
│
├── src/ # Source code
│ ├── collect/ # Data extraction scripts
│ │ └── collect_data.py
│ ├── transform/ # Data transformation scripts
│ │ └── transform_data.py
│ └── ingest/ # Data ingestion scripts
│ └── ingest_data.py
│
├── .github/
│ └── workflows/
│ └── etl_pipeline.yml # GitHub Actions workflow
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation


## ⚡ Pipeline Overview

The ETL pipeline is divided into **3 stages**:

1. **Collect**  
   - Fetches raw datasets (e.g., from Kaggle API).  
   - Saves to `data/raw/`.

2. **Transform**  
   - Cleans, preprocesses, and enriches raw data.  
   - Outputs structured datasets in **Excel** and **JSON** format.  
   - Saves to `data/gold/`.

3. **Ingest**  
   - Loads transformed data into a **MySQL database**.  
   - Uses schema validation and error handling.  

---

## 🔄 CI/CD with GitHub Actions

The project uses **GitHub Actions** for automation:

- **Setup**: Create directories, install dependencies.  
- **Collect**: Run data extraction script.  
- **Transform**: Run cleaning & transformation.  
- **Ingest**: Load into MySQL.  
- **Artifacts**: Pass data files between jobs.  

---

## 🛠️ Setup Instructions

### 1️⃣ Clone Repo
```bash
git clone https://github.com/<your-username>/ETL_End_to_End.git
cd ETL_End_to_End
2️⃣ Create Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Configure Database
Update config/db_config.json with your MySQL credentials:

json
Copy code
{
  "host": "localhost",
  "user": "root",
  "password": "your_password",
  "database": "etl_db"
}
Run schema:

bash
Copy code
mysql -u root -p etl_db < config/schema.sql
5️⃣ Run Scripts Locally
bash
Copy code
# Collect raw data
python src/collect/collect_data.py

# Transform data
python src/transform/transform_data.py

# Ingest into MySQL
python src/ingest/ingest_data.py

📊 Use Case
Demonstrates end-to-end data engineering (ETL pipelines, automation, DB integration).

Prepares data for Power BI / Tableau dashboards.

Real-world workflow showing CI/CD for data pipelines.

Great for portfolio / hiring showcase.

📌 Tech Stack
Python (pandas, openpyxl, mysql-connector)

MySQL for structured data storage

GitHub Actions for CI/CD automation

Power BI (optional) for visualization

📈 Next Steps
Add data quality checks

Enable logging & monitoring

Deploy pipeline on cloud (AWS/GCP/Azure)

Integrate with orchestration tools (Airflow/Prefect)

👨‍💻 Author: [Parnavi Chavan]
📌 Repo: ETL_End_to_End

