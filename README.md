# 🌱 **Syngenta Asset Management System**

An enterprise-grade **Flask-based Asset Management System** built for **Syngenta**, designed to streamline **asset tracking, employee management, and permission control** using secure and scalable web technologies.

---

## 🚀 **Overview**

This system enables Syngenta to **scan, manage, and monitor assets** through QR codes, ensuring accountability and efficiency across all operations.
It implements **role-based access control**, **audit trails**, and **secure user management**, all while maintaining an intuitive user experience.

---

## 🧩 **Core Features**

### 🔍 Asset Scanning & Management

* Scan assets via **QR codes** for quick lookups.
* Maintain detailed records of all company assets.
* Export data to **Excel** for reporting and analytics.

### 👥 Role-Based Access Control

* **Admin** and **Regular User** roles with separate permissions.
* Admins can grant, revoke, and track permission changes (audit trail).
* Regular users have limited scanning and feedback functionalities.

### 🧾 Feedback Collection

* After scanning, regular users can submit feedback directly from the interface.
* Helps track asset conditions and field issues.

### 🧠 Audit & Security

* Secure password hashing and **SQL injection prevention**.
* Tracks permission changes and login activity.
* Full **session management** with safe logout mechanisms.

### ⚙️ CLI Tools

* Maintenance commands to manage system health:

  * Disconnect active users
  * Clean temporary tables
  * Run database maintenance tasks

---

## 🏗️ **Technical Architecture**

| Component        | Description                                    |
| ---------------- | ---------------------------------------------- |
| **Framework**    | Flask (Python)                                 |
| **Database ORM** | SQLAlchemy                                     |
| **Blueprints**   | Modular design separating core functionalities |
| **Security**     | Password hashing, safe query execution         |
| **Sessions**     | Role-based authentication and tracking         |
| **Utilities**    | Excel export, QR code generation               |
| **Project Size** | ~120MB                                         |

---

## 👤 **User Roles**

### 🛠️ **Admin**

* Full access to all system modules
* Grant/remove user permissions
* View audit logs and activity trails
* Manage employee and asset data
* Export reports to Excel
* Perform QR code scans and feedback reviews

### 👨‍💼 **Regular User**

* Limited access — **QR scanning and feedback only**
* Clean, focused interface without admin options
* No access to audit or permission modules

---

## 🌍 **Business Context**

Developed for **Syngenta**, a global leader in agricultural technology, this system addresses real-world challenges in asset tracking and operational efficiency.

Despite being the developer’s **first Flask project**, it demonstrates **enterprise-level complexity and reliability**, showcasing strong understanding across:

* Web architecture
* Security principles
* Database management
* UX-focused design

---

## 🧰 **Installation & Setup**

### **1. Clone the Repository**

```bash
git clone https://github.com/your-username/syngenta-asset-management.git
cd syngenta-asset-management
```

### **2. Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4. Initialize the Database**

```bash
flask db upgrade
```

### **5. Run the Application**

```bash
flask run
```

Access the app at: **[http://localhost:5000](http://localhost:5000)**

---

## 📊 **Example Workflow**

1. **Admin** logs in → grants permissions → manages assets
2. **Regular user** scans asset QR code
3. System fetches asset details
4. Feedback form appears → user submits feedback
5. Data stored securely with timestamp and user ID

---

## 🛡️ **Security Highlights**

* Passwords hashed with industry-standard algorithms
* ORM-based queries prevent SQL injection
* Role-based session validation
* Comprehensive audit trail for all permission changes

---

## 🧩 **Future Improvements**

* REST API endpoints for mobile integration
* Asset condition analytics dashboard
* Email notifications for permission updates
* Multi-language support

---

## 🏁 **Conclusion**

The **Syngenta Asset Management System** exemplifies a robust, production-ready Flask application.
It merges strong **technical architecture**, **business value**, and **security practices**, serving as a model for scalable internal management tools.

---

**Tech Stack:** Flask • SQLAlchemy • HTML/CSS/JS • Excel Export • QR Integration


