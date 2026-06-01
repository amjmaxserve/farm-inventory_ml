# Phase 5 — Security, Authentication & Governance

## Overview

Phase 5 transforms the Farm Inventory MLOps Platform from a functional application into a secured enterprise platform.

This phase introduces:

* Authentication
* Authorization
* User Management
* Audit Logging
* Governance Controls

---

# Architecture

User
│
▼
OAuth2 Login
│
▼
JWT Token
│
▼
RBAC Validation
│
▼
Protected API Access

---

# Authentication

Technology:

* OAuth2 Password Flow
* JWT Access Tokens
* bcrypt Password Hashing

Authentication API:

POST /api/auth/login

Response:

{
"access_token": "<jwt-token>",
"token_type": "bearer"
}

Current User API:

GET /api/auth/me

---

# RBAC

Supported Roles:

## ADMIN

Full system access.

Permissions:

* User Management
* Inventory Management
* ML Operations
* Audit Access

---

## INVENTORY_MANAGER

Permissions:

* Inventory CRUD
* Prediction Access

Restrictions:

* Cannot manage users

---

## DATA_SCIENTIST

Permissions:

* Prediction APIs
* Prediction History

Restrictions:

* Cannot manage inventory
* Cannot manage users

---

## VIEWER

Permissions:

* Read-only operations

Restrictions:

* No modifications
* No ML operations

---

# User Management APIs

POST /api/users

Create user.

GET /api/users

List users.

GET /api/users/{id}

Retrieve user.

PUT /api/users/{id}

Update user.

PATCH /api/users/{id}/enable

Enable user.

PATCH /api/users/{id}/disable

Disable user.

DELETE /api/users/{id}

Delete user.

---

# Audit Logging

Table:

audit_logs

Structure:

* id
* username
* action
* resource
* details
* created_at

Example:

admin | CREATE | USER | Created user viewer01

---

# Security Validation

Validated:

✓ OAuth2 Login

✓ JWT Authorization

✓ Role Enforcement

✓ User Activation Control

✓ User Deactivation Control

✓ Audit Persistence

---
# Troubleshooting & Validation

## Create Default Admin User

```python
from app.database.db import SessionLocal
from app.database.models import User
from app.auth.security import hash_password

db = SessionLocal()

admin = User(
    username="admin",
    email="admin@farm.local",
    hashed_password=hash_password("Admin123"),
    role="ADMIN"
)

db.add(admin)
db.commit()

print("Admin created")
```

---

## Create Default Viewer User

```python
from app.database.db import SessionLocal
from app.database.models import User
from app.auth.security import hash_password

db = SessionLocal()

viewer = User(
    username="viewer",
    email="viewer@farm.local",
    hashed_password=hash_password("Viewer123"),
    role="VIEWER"
)

db.add(viewer)
db.commit()

print("Viewer created")
```

---

## OAuth2 Login Test

Endpoint:

```http
POST /api/auth/login
```

Credentials:

```text
Username: admin
Password: Admin123
```

Expected Response:

```json
{
  "access_token": "<jwt-token>",
  "token_type": "bearer"
}
```

---

## Swagger Authorization Test

1. Open Swagger UI
2. Click Authorize
3. Enter credentials:

```text
admin / Admin123
```

4. Click Authorize

Expected:

```text
Authorization Successful
```

Green lock icon appears.

---

## Inventory Creation Test

```json
{
  "item_name": "Urea Fertilizer",
  "category": "Fertilizer",
  "crop_type": "Rice",
  "quantity": 250,
  "unit": "Kg",
  "minimum_stock_level": 50,
  "cost": 12500,
  "supplier": "Kerala Agro Supplies",
  "storage_location": "Warehouse-A",
  "expiry_date": "2027-12-31",
  "batch_number": "UREA-2026-001",
  "season": "Kharif",
  "usage_per_month": 30
}
```

Expected:

```text
Inventory created successfully.
```

---

## Audit Log Verification

Connect PostgreSQL:

```bash
docker exec -it farm_postgres \
psql -U farmadmin -d farm_inventory
```

View audit logs:

```sql
SELECT
    username,
    action,
    resource,
    details
FROM audit_logs
ORDER BY id DESC;
```

Example Output:

```text
admin | DELETE  | USER | Deleted user viewer01
admin | ENABLE  | USER | Enabled user viewer01
admin | DISABLE | USER | Disabled user viewer01
admin | UPDATE  | USER | Updated user viewer01
admin | CREATE  | USER | Created user viewer01
```

---

## Verify User Records

```sql
SELECT
    username,
    role,
    is_active
FROM users;
```

Expected:

```text
 username | role  | is_active
----------+-------+----------
 admin    | ADMIN | t
 viewer   | VIEWER| t
```

---

## Common Issues

### Invalid Token

```json
{
  "detail": "Invalid token"
}
```

Cause:

* Expired JWT
* Incorrect Authorization header

Fix:

* Login again
* Re-authorize in Swagger

---

### User Account Disabled

```json
{
  "detail": "User account disabled"
}
```

Fix:

Enable user:

```http
PATCH /api/users/{id}/enable
```

---

### Admin Access Required

```json
{
  "detail": "Admin access required"
}
```

Cause:

Current user role is not ADMIN.

---

### ML Access Required

```json
{
  "detail": "ML access required"
}
```

Allowed Roles:

* ADMIN
* INVENTORY_MANAGER
* DATA_SCIENTIST

---

## Phase 5 Validation Checklist

✅ OAuth2 Authentication

✅ JWT Authorization

✅ RBAC Enforcement

✅ User Management APIs

✅ Audit Logging

✅ PostgreSQL Audit Persistence

✅ Swagger Integration

✅ Role Based Access Control

Phase 5 successfully completed.


---
# Achievements

Enterprise Security Foundation Completed.

Platform Status:

Production Ready Security Layer.

Next Phase:

Phase 6 — Model Registry & Advanced MLOps.
