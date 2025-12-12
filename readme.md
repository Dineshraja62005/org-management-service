# Organization Management Service – Backend

A **multi-tenant backend application** built with **FastAPI**, **MongoDB**, and **JWT authentication**.  
The system allows creating, managing, and securing organizations, where each organization is isolated and managed by its own admin.

---

## 🚀 Features

- Modular and clean architecture with clear separation of concerns
- Domain-based structure (Organization, Authentication, Security)
- Easily extensible to a **class-based service layer**
- Secure password handling using SHA-256 + bcrypt
- Admin authentication using JWT (Bearer tokens)
- Organization-level authorization
- Full CRUD operations for organizations
- Multi-tenant MongoDB design (one collection per organization)
- Interactive API documentation using Swagger (OpenAPI)

---

## 🛠 Tech Stack

- **Backend Framework:** FastAPI (Python)
- **Database:** MongoDB
- **Authentication:** JWT (Bearer Token)
- **Password Hashing:** SHA-256 + bcrypt
- **API Documentation:** Swagger (OpenAPI)

---

## 📂 Project Structure

```
app/
├── core/
│   └── security.py          # JWT & password security utilities
├── models/
│   ├── organization.py     # Pydantic request/response models
│   └── admin.py            # Admin login model
├── routes/
│   ├── org.py              # Organization CRUD APIs
│   └── auth.py             # Authentication APIs
├── database.py             # MongoDB connection setup
└── main.py                 # FastAPI application entry point
```

Each module follows the **single responsibility principle**, keeping the codebase clean, readable, and maintainable.  
The structure also allows easy migration to a **class-based service design** if required.

---

## ⚙️ Setup Instructions (How to Run)

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd org-management-service
```

### 2️⃣ Create & Activate Virtual Environment (Windows)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Start MongoDB

Ensure MongoDB is running locally on:

```
mongodb://127.0.0.1:27017
```

### 5️⃣ Run the Application

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🔐 Authentication Flow

1. **Create Organization** – `POST /org/create`
2. **Admin Login** – `POST /admin/login` → JWT token
3. **Authorize Requests** using `Authorization: Bearer <token>`
4. **Access Protected APIs** (update / delete organization)

---

## 🔗 API Endpoints Summary

| Method | Endpoint | Description | Auth Required |
|------|---------|------------|---------------|
| POST | /org/create | Create organization | ❌ |
| POST | /admin/login | Admin login | ❌ |
| GET | /org/get | Get organization | ❌ |
| PUT | /org/update | Update organization | ✅ |
| DELETE | /org/delete | Delete organization | ✅ |

---

## 🧠 High-Level Architecture Diagram

```
Client (Swagger / Curl / Frontend)
        |
        v
FastAPI Application
  |        |
  |        ├── Auth Routes (/admin/login)
  |        ├── Org Routes (/org/*)
  |
  ├── Security Layer (JWT + Password Hashing)
  |
  v
MongoDB
  ├── organizations (master collection)
  └── org_<organization_name> (tenant collections)
```

---

## 🧩 Design Choices (Brief Explanation)

- **FastAPI** was chosen for its performance, built-in validation, and automatic API documentation.
- **JWT Authentication** provides stateless and scalable security.
- **Multi-collection tenancy** ensures strong isolation between organizations.
- The architecture is intentionally kept modular to support a **class-based service layer** in the future.

---

## ⚖️ Trade-offs

- A large number of organizations can result in many MongoDB collections
- Renaming an organization requires collection migration
- Cross-organization queries are intentionally restricted

These trade-offs are acceptable for **small to medium-scale systems** and clearly demonstrate backend design decisions.

---

## 🔮 Future Improvements

- Environment-based configuration using `.env`
- Role-based access control (RBAC)
- Refresh tokens
- Rate limiting and request logging
- Dedicated service layer (fully class-based design)

---

## ✅ Conclusion

This project demonstrates a **clean, modular, and secure backend architecture** using modern Python tooling.  
It is suitable for **academic submissions, interviews, and real-world SaaS backends**.

---

**Author:** Dinesh Raja M

