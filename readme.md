# Organization Management Service – Backend

A **multi-tenant backend application** built with **FastAPI**, **MongoDB**, and **JWT authentication**. This project allows creating, managing, and securing organizations where each organization has isolated data and an admin authenticated via JWT.

---

## 🚀 Features

- Organization creation with admin credentials
- Secure password hashing (SHA-256 + bcrypt)
- Admin login with JWT authentication
- Org-level authorization (admins can act only on their org)
- Full CRUD operations on organizations
- Multi-tenant MongoDB design (one collection per organization)
- Interactive API documentation using Swagger

---

## 🛠 Tech Stack

- **Backend Framework:** FastAPI (Python)
- **Database:** MongoDB
- **Authentication:** JWT (Bearer Token)
- **Password Hashing:** SHA-256 + bcrypt
- **API Docs:** Swagger (OpenAPI)

---

## 📂 Project Structure

```
app/
├── core/
│   └── security.py          # Password hashing & JWT logic
├── models/
│   ├── organization.py     # Pydantic models
│   └── admin.py             # Admin login model
├── routes/
│   ├── org.py               # Organization CRUD APIs
│   └── auth.py              # Admin login API
├── database.py              # MongoDB connection
└── main.py                  # FastAPI app entry point
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd org-management-service
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Start MongoDB

Make sure MongoDB is running locally on:
```
mongodb://127.0.0.1:27017
```

### 5️⃣ Run the Server

```bash
uvicorn app.main:app --reload
```

Server will run at:
```
http://127.0.0.1:8000
```

---

## 📘 API Documentation

Swagger UI:
```
http://127.0.0.1:8000/docs
```

---

## 🔑 Authentication Flow

1. **Create Organization** (`POST /org/create`)
   - Stores admin credentials securely
2. **Admin Login** (`POST /admin/login`)
   - Returns JWT token
3. **Authorize**
   - Use `Authorization: Bearer <token>`
4. **Access Protected APIs**
   - Update/Delete organization

---

## 🔐 API Endpoints Summary

| Method | Endpoint | Description | Auth Required |
|------|---------|------------|---------------|
| POST | /org/create | Create organization | ❌ |
| POST | /admin/login | Admin login | ❌ |
| GET | /org/get | Get organization | ❌ |
| PUT | /org/update | Update organization | ✅ |
| DELETE | /org/delete | Delete organization | ✅ |

---

## 🧠 Architecture Overview

- **FastAPI** handles REST APIs and validation
- **JWT** ensures stateless authentication
- **MongoDB** stores:
  - Master collection (`organizations`)
  - Tenant collections (`org_<name>`)
- Each request validates admin + organization from JWT

---

## ⚖️ Trade-offs

### Pros
- Strong data isolation
- Simple authorization logic
- Secure authentication

### Cons
- Many collections for large number of orgs
- Renaming org requires data migration

---

## 🔮 Future Improvements

- Environment-based configuration
- Role-based access control (RBAC)
- Refresh tokens
- Rate limiting
- Centralized logging

---

## ✅ Conclusion

This project demonstrates a **secure, scalable, and clean backend architecture** using modern Python tooling. It is suitable for learning, assignments, and as a foundation for real-world SaaS backends.

---

**Author:** Dinesh Raja M

