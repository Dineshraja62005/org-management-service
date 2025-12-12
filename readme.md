# Organization Management Service – Backend

A **multi-tenant backend application** built with **FastAPI**, **MongoDB**, and **JWT authentication**. This project allows creating, managing, and securing organizations where each organization has isolated data and an admin authenticated via JWT.

---

## 🚀 Features

- Modular and clean architecture (route-wise and responsibility-based separation)
- Clear separation of concerns (models, routes, security, database)
- Logic grouped by domain (Organization, Auth)
- Easily extensible to class-based services if needed (service layer can be added)


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
│   ├── organization.py     # Pydantic request models
│   └── admin.py             # Admin login model
├── routes/
│   ├── org.py               # Organization CRUD APIs
│   └── auth.py              # Admin login API
├── database.py              # MongoDB connection setup
└── main.py                  # FastAPI app entry point
```

Each module has a **single responsibility**, making the design clean and maintainable.


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

## ⚙️ Setup Instructions (How to Run)

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd org-management-service
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
venv\\Scripts\\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Start MongoDB

Ensure MongoDB is running locally:
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

### High-Level Diagram

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

### Flow Summary
- Client sends request to FastAPI
- FastAPI validates input using Pydantic models
- JWT middleware validates admin identity
- MongoDB performs CRUD operations


- **FastAPI** handles REST APIs and validation
- **JWT** ensures stateless authentication
- **MongoDB** stores:
  - Master collection (`organizations`)
  - Tenant collections (`org_<name>`)
- Each request validates admin + organization from JWT

---

## ⚖️ Design Choices & Trade-offs

### Why FastAPI?
- High performance
- Built-in validation
- Automatic Swagger documentation

### Why JWT Authentication?
- Stateless and scalable
- No server-side session storage
- Industry standard

### Why Multi-Collection (One per Org)?
- Strong data isolation
- Easy org deletion
- Clear tenant boundaries

### Trade-offs
- Large number of collections if org count is very high
- Cross-organization queries are harder
- Organization rename requires collection migration

These trade-offs are acceptable for **small to medium-scale SaaS systems** and for demonstrating clean backend design.


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

