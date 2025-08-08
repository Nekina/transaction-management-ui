# Transaction Management UI

A Flask-based web application offering a user interface and server-side operations for managing financial transactions—built to practice CRUD functionalities with server-side rendering and search.

## Features

- Create, Read, Update, and Delete (CRUD) transaction entries  
- Server-Side Rendering (SSR) using Flask and Jinja2 templates  
- Built-in search to filter transactions by amount  
- Modular routing and utility code for clarity and extensibility (e.g., `app.py`, `utils.py`)  
- Practice-driven foundation following IBM's template for skill building

## Tech Stack

- **Python** – Core programming language  
- **Flask** – Lightweight web framework for routing and views  
- **Jinja2** – Templating engine for server-rendered UI  
- **HTML/CSS** – For front-end rendering  
- Possibly **SQLite** or similar – For managing transaction data storage (if included or intended)  

## Installation and Setup

1. Clone the repository:  
   ```bash
   git clone https://github.com/Nekina/transaction-management-ui.git
   cd transaction-management-ui
2. (Recommended) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
3. Install dependencies (add requirements.txt if available):
   ```bash
   pip install flask
   # pip install -r requirements.txt  # if such file exists
4. Launch the Flask development server:  
   ```bash
   flask run
   ```
   or if app.py is the entry point:
   ```bash
   python app.py
5. Open your browser and navigate to http://127.0.0.1:5000 to begin interacting with the application.
