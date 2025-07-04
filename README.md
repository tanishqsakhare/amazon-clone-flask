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

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

flask run
