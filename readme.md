# ✅ TODO Using Flask

A simple and elegant **To-Do List Web Application** built with **Flask**, **SQLite**, **Jinja2 templates**, and styled using **Tailwind CSS**. This app allows users to add, complete, and delete tasks with a responsive and minimal user interface.

---

## 📁 Project Structure

```

TODO\_USING\_FLASK/
├── Flask1.py                  # Main Flask application
├── instance/
│   └── project.db             # SQLite database file
├── static/
│   └── style.css              # Custom styling (optional alongside Tailwind)
├── templates/
│   ├── Home.html              # Main UI for the to-do app
│   └── includes/
│       └── base.html          # Base template (header, footer, layout)

````

---

## ✨ Features

- ✅ Add new tasks
- 📋 View current tasks
- ❌ Delete completed tasks
- 💾 Persistent storage using SQLite (`project.db`)
- 🎨 Responsive design using Tailwind CSS
- 🧩 Template inheritance with `base.html`

---

## 🔧 Tech Stack

- **Flask** – Lightweight Python web framework  
- **SQLite** – Embedded relational database  
- **Jinja2** – Templating engine for HTML  
- **Tailwind CSS** – Utility-first CSS framework (via CDN)  

---

## 🚀 Getting Started

### 🧱 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### ⚙️ Installation Steps

1. **Clone the repository**

```bash
git clone https://github.com/thevip01/TODO_USING_FLASK.git
cd TODO_USING_FLASK
````

2. **(Optional) Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Flask**

```bash
pip install flask
```

4. **Run the app**

```bash
python Flask1.py
```

5. Open your browser and navigate to:
   🌐 [http://localhost:5000](http://localhost:5000)

---

You can also customize styles further in `static/style.css`.

---

## 🗃️ Database

The app uses a local SQLite database stored in:

```
instance/project.db
```

If `project.db` doesn't exist, Flask will create it automatically when the app is first run.

---


## 👤 Author

**Vipul Parmar**
GitHub: [@thevip01](https://github.com/thevip01)

---

## 📄 License

This project is licensed for educational and personal use. Feel free to fork and modify.

---

## 🔮 Future Improvements

* Task due dates and sorting
* User login system
* Deployment to Render, Vercel, or Heroku
* Dark mode toggle with Tailwind
