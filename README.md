# 🚀 Amazon Clone (Flask + SQLite + Responsive UI) 🛒

A full-featured e-commerce web application inspired by Amazon, built using **Flask**, **SQLite**, and a fully responsive **HTML/CSS/JavaScript** frontend. This project replicates core shopping functionalities like cart management, order placement, user authentication, and more — all wrapped in a clean, modern UI.

---

## 📦 Features

- 🛒 Add to Cart & Checkout
- 🔐 User Registration & Login (Flask-Login)
- 📦 Order Placement with History Tracking
- 🌗 Dark/Light Mode Toggle (with localStorage)
- 📧 Newsletter Subscription Form
- 📱 Fully Responsive Design (Mobile + Desktop)
- 🖼️ Social Media Integration (Footer Icons)
- ⚠️ Flash Messages for Feedback
- 🧾 Clean UI with Amazon-Inspired Layout

---

## 🧰 Tech Stack

| Layer        | Technology                     |
|--------------|--------------------------------|
| Backend      | Python, Flask, Flask-Login     |
| Database     | SQLite                         |
| Frontend     | HTML, CSS, JavaScript          |
| Templating   | Jinja2                         |
| Styling      | Custom CSS + Responsive Layout |
| Extras       | Flask-Mail (optional), Flask-Migrate |

---

## 📂 Project Structure

amazon-clone-flask/ │ ├── app/ │ ├── static/ # CSS, JS, Images │ ├── templates/ # HTML templates │ ├── models.py # Database models │ ├── routes.py # Flask routes │ └── init.py # App factory │ ├── migrations/ # Flask-Migrate files ├── store.db # SQLite database ├── run.py # Entry point └── README.md

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/amazon-clone-flask.git
cd amazon-clone-flask
```
### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 5. Run the Application

```bash
flask run
```

---


## ✅ Default Routes

| Route        | Description                      |
|--------------|----------------------------------|
| `/`          | Home page with product listings  |
| `/login`     | User login page                  |
| `/register`  | User registration page           |
| `/cart`      | View and manage cart items       |
| `/checkout`  | Place an order                   |
| `/orders`    | View order history               |
| `/subscribe` | Newsletter subscription          |
| `/privacy`   | Privacy policy page              |
| `/terms`     | Terms of service page            |
| `/help`      | Help & FAQ page                  |

---

## 🔗 Social Links

[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/tanishqsakhare)
[![GitHub](https://img.shields.io/badge/GitHub-black?style=for-the-badge&logo=github)](https://github.com/tanishqsakhare)
[![Gmail](https://img.shields.io/badge/Gmail-red?style=for-the-badge&logo=gmail)](mailto:tanishqsakhare@gmail.com)

---

## 🛡️ License 

![License](https://img.shields.io/badge/license-MIT-blue.svg)

---
