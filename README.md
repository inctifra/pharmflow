
# 💊 Pharmflow – Pharmacy Inventory Management MVP

**Pharmflow** is a simple, minimal Django-based web application built to help small pharmacy stores manage their drug inventory effectively. This MVP version focuses on essential features such as stock tracking, expiry date monitoring, and basic inventory operations — without any authentication or user roles.

---

## 🚀 Features

- 📦 Add and manage drugs
- 🗂️ Add stock entries for drugs
- ⏰ Automatically flag expired stock
- 🧾 View current stock levels
- 🗑️ Delete stock entries
- 🎨 Clean and responsive Bootstrap 5 UI

---

## 🛠️ Built With

- [Django](https://www.djangoproject.com/) – Backend framework
- [Bootstrap 5](https://getbootstrap.com/) – Frontend styling
- Python 3.12
- SQLite (default database)

---


---

## ⚙️ How to Run

1 **clone the repos**

   ```bash
   git clone https://github.com/inctifra/pharmflow.git
   cd pharmalite
````

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install django
   ```

4. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

6. **Open in browser**:

   ```
   http://127.0.0.1:8000/
   ```

---

## 📌 Notes

* This is a **Minimal Viable Product (MVP)** version meant for demonstration and initial client feedback.
* No authentication or user access control is implemented in this version.
* Admin dashboard is enabled for managing drugs and stocks (`/admin`).

---

## 🎯 Future Improvements

* User authentication and roles (e.g., staff vs. owner)
* Export stock reports to PDF or Excel
* Barcode scanner support
* SMS or email alerts for expired/low stock
* Multi-branch support
* Hosting (e.g., PythonAnywhere, Render, Heroku)

---

## 📄 License


---

## 🙋‍♂️ About the Developer

I'm a pharmacy student and web developer passionate about solving real-world problems using code.
For collaboration, customization, or deployment help, feel free to reach out.
[email](inctifra@gmail.com)
<br />
[phone](254745547755)

---



