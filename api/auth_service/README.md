# Auth Service

This is the **Authentication Service** for the **CloudScaler** project. It is built using **Flask** and provides JWT-based authentication for both **B2B** and **B2C** clients. The service integrates with **MySQL** as the backend and supports multiple environments (dev, test, uat, prod). It is fully containerized with Docker and can be deployed on AWS.

---

## **Features**

- **JWT Authentication & Authorization**
- **Flask with Production-Grade Structure**
- **MySQL Database Support**
- **Environment-Based Configuration**
- **Swagger API Documentation**
- **Dockerized for Easy Deployment**

---

## **Project Structure**

```
CloudScaler/
├── docker-compose.yml        # Root-level Docker Compose for all microservices
├── auth-service/             # Auth Service
│   ├── app/
│   │   ├── __init__.py       # App Initialization
│   │   ├── config.py        # Configuration Management
│   │   ├── models.py        # Database Models
│   │   ├── routes.py        # API Routes
│   │   ├── services.py      # Business Logic
│   │   ├── utils.py         # Helper Functions
│   │   ├── swagger_config.json  # Swagger API Docs
│   ├── sql/
│   │   ├── auth_db.sql      # SQL Script for Database Setup
│   ├── .env                 # Environment Variables
│   ├── Dockerfile           # Dockerfile for the Auth Service
│   ├── requirements.txt     # Python Dependencies
│   ├── wsgi.py              # Entry Point for Running the Service
│   ├── README.md            # Project Documentation
```

---

## **Installation & Setup**

### **1. Clone the Repository**
```sh
git clone https://github.com/your-username/CloudScaler.git
cd CloudScaler/auth-service
```

### **2. Setup Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4. Configure Environment Variables**
Create a `.env` file inside `auth-service/`:

```ini
MYSQL_HOST=db
MYSQL_PORT=3306
MYSQL_DATABASE=auth_db
MYSQL_USER=user
MYSQL_PASSWORD=password
JWT_SECRET_KEY=supersecretkey
APP_ENV=development
```

---

## **Running the Application**

### **1. Run Locally**
```sh
python wsgi.py
```

### **2. Run with Docker**

#### **Build & Run**
```sh
docker build -t auth-service .
docker run --env-file .env -p 5000:5000 auth-service
```

#### **Using Docker Compose (Recommended)**
Navigate to the root of the repository and run:
```sh
docker-compose up --build
```

---

## **API Documentation (Swagger)**

Swagger is pre-configured and can be accessed at:
```
http://localhost:5000/api/docs
```

---

## **Database Setup**

Run the SQL script to set up the database:
```sh
mysql -u user -p -h localhost auth_db < sql/auth_db.sql
```

---

## **Endpoints**

### **1. User Registration**
**POST** `/api/auth/register`
```json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "securepassword"
}
```

### **2. User Login**
**POST** `/api/auth/login`
```json
{
  "username": "testuser",
  "password": "securepassword"
}
```
_Response:_
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs..."
}
```

### **3. Protected Route** (Requires JWT Token)
**GET** `/api/auth/protected`
_Add Authorization Header:_
```sh
Authorization: Bearer <your-jwt-token>
```

_Response:_
```json
{
  "message": "Access granted"
}
```

---

## **Contributing**
Feel free to submit **pull requests** and improve the service!

---

## **License**
MIT License © 2025 CloudScaler

---

🚀 **Auth Service is ready for deployment!**