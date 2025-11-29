# Rabble Web Application

## Overview

**Rabble** is a simple Reddit-like web application built using the Django framework for [CMSC 22000 - Introduction to Software Development](https://uchicago-cs.github.io/cmsc22000/) at the University of Chicago. The project was developed as a series of homeworks to introduce and practice web development concepts, full-stack architecture, and software engineering.

Rabble allows users to create accounts, submit posts, comment on posts, and interact with communities ("subRabbles") with core features described below.  
*Please note: this code was originally written as part of a course assignment.*

---

## Features

- **User Authentication:** Sign up, login, logout, session and token-based auth
- **Posts:** Create, edit, delete, and view posts within communities ("subRabbles")
- **Comments:** Add, edit, delete comments on posts, including support for threaded/threadable replies
- **SubRabbles:** Organize content into subRabbles (similar to subreddits), including private subRabbles
- **Anonymous Interactions:** Optionally post and comment anonymously
- **CRUD Operations:** Full Create, Read, Update, Delete functionality for posts, comments, and communities
- **RESTful API:** API endpoints for interacting with posts, comments, and subRabbles (with permissions)
- **Frontend:** Responsive HTML/CSS templates using Django templating
- **Testing:** Automated tests for core views and endpoints (Django test framework)
- **Continuous Integration (CI):** Workflow status badge (see below)
- **Deployment:** Instructions and support for Heroku deployment

---

## Language Composition

- **Python:** 83.4%
- **HTML:** 14.5%
- **CSS:** 2.1%

---

## Getting Started

### Prerequisites

- Python 3.8+
- Django 3.x or 4.x
- Pip
- Git

Optional for advanced features:
- Heroku CLI (for deployment)
- Coverage.py (for measuring test coverage)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/fredricngo/rabble.git
    cd rabble
    ```

2. **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **(Optional) Set up environment variables:**
    - Rename `.env.example` to `.env` and fill in necessary secrets (e.g., Django `SECRET_KEY`)
    - Set up database settings in `settings.py` if deploying

5. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    Access the site at [http://localhost:8000](http://localhost:8000)

---

## Usage

- Register as a new user or log in with an existing account
- Create and join subRabbles (communities)
- Browse, create, and reply to posts
- Add threaded comments and replies
- Explore API endpoints (see `/api/`)
- For anonymous interactions, check for checkbox/options

---

## API Documentation

Basic endpoints are available under `/api/` (see `api/urls.py` for full list).

- **Authentication:** Login and token-based
- **Posts, Comments, SubRabbles:** CRUD operations
- API permissions enforced to restrict sensitive operations to logged-in users

---

## Running Tests

To run automated unit tests:
```bash
python manage.py test
```

To check test coverage (if coverage.py enabled):
```bash
coverage run manage.py test
coverage report
```

---

## Deployment

Deploy to Heroku:

1. **Create Heroku app and add remote:**
    ```bash
    heroku create your-app-name
    git push heroku main
    ```

2. **Set environment variables on Heroku:**
    - `heroku config:set SECRET_KEY=your_secret`
    - Set up database, storage, etc.

---

## Improvements & TODOs

- Add/delete comments (CRUD)
- Threaded replies
- Private subRabbles & anonymous posts
- Permissions and session-based authentication for API
- Improve frontend UX (avoid full page reloads when commenting)
- Add more comprehensive test coverage
- Add CI workflow badge  
    ![CI](https://github.com/fredricngo/rabble/actions/workflows/ci.yml/badge.svg)
- Clean up unnecessary files (no virtual environments, homework reports, etc.)

---

## License

This repository is released as part of a class assignment for [CMSC 22000 - Introduction to Software Development](https://uchicago-cs.github.io/cmsc22000/).  
You may reuse or modify the code as long as you attribute the original assignment context.

---

## Acknowledgments

- [University of Chicago CMSC 22000](https://uchicago-cs.github.io/cmsc22000/)
- Django and open-source library authors


