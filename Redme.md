# 🧮 Calculator 3-Tier Application

A modern **3-Tier Calculator Application** built using **HTML, CSS, JavaScript, Python Flask, MySQL, Docker, and Docker Compose**. The application follows the three-tier architecture by separating the Presentation Layer, Business Logic Layer, and Database Layer into independent containers.

---

# 📌 Project Overview

This project demonstrates how a frontend, backend, and database communicate with each other using REST APIs in a containerized environment.

* **Presentation Layer:** HTML, CSS, JavaScript, Nginx
* **Application Layer:** Python Flask REST API
* **Database Layer:** MySQL

Each tier runs inside its own Docker container, making the application portable, scalable, and easy to deploy.

---

# 🏗 Project Structure

```text
calculator-3tier/

├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   ├── Dockerfile
│   └── nginx.conf
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── db/
│   └── init.sql
│
├── docker-compose.yml
└── README.md
```

---

# 🏛 Architecture

```text
                User
                  │
                  ▼
      Frontend (Nginx + HTML/CSS/JS)
                  │
          HTTP REST API Request
                  │
                  ▼
      Backend (Python Flask API)
                  │
            SQL Queries
                  │
                  ▼
          MySQL Database
```

---

# 🚀 Features

* Modern responsive UI
* Addition, Subtraction, Multiplication, Division
* REST API communication
* Calculation history
* MySQL database integration
* Dockerized frontend, backend, and database
* Docker Compose support
* Beginner-friendly 3-tier architecture

---

# 🛠 Technologies Used

| Layer            | Technology                     |
| ---------------- | ------------------------------ |
| Frontend         | HTML5, CSS3, JavaScript, Nginx |
| Backend          | Python, Flask, Flask-CORS      |
| Database         | MySQL 8                        |
| Containerization | Docker                         |
| Orchestration    | Docker Compose                 |

---

# ⚙ Prerequisites

Before running the project, make sure you have:

* Docker
* Docker Compose

Verify installation:

```bash
docker --version
docker compose version
```

---

# ▶️ How to Run

### Clone the repository

```bash
git clone https://github.com/fahadkh14/calculator-3tier.git

cd calculator-3tier
```

---

### Build the Docker images

```bash
docker compose build
```

---

### Start the application

```bash
docker compose up -d
```

---

### Check running containers

```bash
docker ps
```

---

# 🌐 Access the Application

| Service     | URL                   |
| ----------- | --------------------- |
| Frontend    | http://localhost:8080 |
| Backend API | http://localhost:5000 |
| MySQL       | localhost:3306        |

---

# 📡 API Endpoints

## Home

**GET**

```text
/
```

Returns backend status.

---

## Calculate

**POST**

```text
/calculate
```

### Request Body

```json
{
  "num1": 20,
  "num2": 10,
  "operation": "add"
}
```

### Response

```json
{
  "result": 30
}
```

Supported operations:

* add
* sub
* mul
* div

---

## Calculation History

**GET**

```text
/history
```

Returns the latest calculation history stored in the database.

---

# 🗄 Database Schema

**Table: history**

| Column     | Type        |
| ---------- | ----------- |
| id         | INT         |
| num1       | FLOAT       |
| num2       | FLOAT       |
| operation  | VARCHAR(20) |
| result     | FLOAT       |
| created_at | TIMESTAMP   |

---

# 🐳 Docker Containers

| Container | Description                            |
| --------- | -------------------------------------- |
| frontend  | Serves the web interface using Nginx   |
| backend   | Runs the Flask REST API                |
| db        | Stores calculation history using MySQL |

---

# 📂 Docker Commands

Start containers

```bash
docker compose up -d
```

View logs

```bash
docker compose logs -f
```

Stop containers

```bash
docker compose down
```

Stop and remove volumes

```bash
docker compose down -v
```

Rebuild containers

```bash
docker compose up --build
```

---

# 🎯 Learning Objectives

* Understand Three-Tier Architecture
* Build REST APIs with Flask
* Connect Flask with MySQL
* Use Docker for containerization
* Use Docker Compose for multi-container applications
* Prepare applications for Kubernetes deployment

---

# 🚀 Future Enhancements

* User Authentication
* Calculator History Search
* Export History (CSV/PDF)
* Dark/Light Theme
* Kubernetes Deployment
* GitHub Actions CI/CD Pipeline
* Monitoring with Prometheus & Grafana

---

# 👨‍💻 Author

**Mohd Fahad Khan**

This project was created for learning Docker, Flask, MySQL, and Three-Tier Architecture using containerized applications.
