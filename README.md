# 🔗 URL Shortener

A simple and lightweight **URL Shortener Web Application** built with **Python, Flask, HTML/CSS, and JSON-based storage**.

The application allows users to enter a long URL, generate a unique 6-character short code, and access the original URL through the generated short link. It also tracks the number of clicks for each shortened URL.

## 👨‍💻 Author

**Shashank Kumar**

GitHub: [Shashank14105](https://www.github.com/Shashank14105)

---

## 🚀 Features

- 🔗 Convert long URLs into short URLs
- ✅ Validate URLs before shortening
- 🎲 Generate unique 6-character alphanumeric short codes
- ↪️ Redirect short URLs to their original URLs
- 📊 Track the number of clicks for each short URL
- 💾 Store URL data persistently in a JSON file
- 🔒 Thread-safe JSON file access using a locking mechanism
- ❌ Custom 404 page for invalid/non-existent short links
- 🖥️ Simple and responsive web interface

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Flask 3.0.3 | Web framework and routing |
| HTML5 | Web page structure |
| CSS3 | User interface styling |
| JSON | Persistent data storage |
| Jinja2 | Dynamic HTML templating |

---

## 📁 Project Structure

```text
URL-Shortener/
│
├── app.py                  # Flask application and routes
├── shortener.py            # URL validation, normalization and code generation
├── storage.py              # JSON data storage and click tracking
├── requirements.txt        # Python dependencies
│
├── data/
│   └── urls.json           # Stores shortened URL records
│
└── templates/
    ├── index.html           # Main URL shortener interface
    └── 404.html             # Custom 404 error page
```

---

## 🔄 Project Workflow

The application follows this workflow:

```text
                    ┌─────────────────────┐
                    │       User          │
                    │ Enters Long URL     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Flask /shorten  │
                    │      POST Route     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Normalize URL     │
                    │     trim spaces     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Validate URL     │
                    │ http / https + host │
                    └──────────┬──────────┘
                               │
                         ┌─────┴─────┐
                         │           │
                      Invalid      Valid
                         │           │
                         ▼           ▼
                  ┌────────────┐ ┌─────────────────┐
                  │ Show Error │ │ Generate Unique │
                  │  Message   │ │ 6-char Code     │
                  └────────────┘ └────────┬────────┘
                                          │
                                          ▼
                                ┌──────────────────┐
                                │ Store URL +      │
                                │ clicks = 0       │
                                │ in urls.json     │
                                └────────┬─────────┘
                                         │
                                         ▼
                                ┌──────────────────┐
                                │ Display Short    │
                                │ URL to User      │
                                └────────┬─────────┘
                                         │
                                         ▼
                                ┌──────────────────┐
                                │ User opens       │
                                │ /<short_code>    │
                                └────────┬─────────┘
                                         │
                                         ▼
                                ┌──────────────────┐
                                │ Find URL in      │
                                │ urls.json        │
                                └────────┬─────────┘
                                         │
                                  ┌──────┴──────┐
                                  │             │
                               Not Found      Found
                                  │             │
                                  ▼             ▼
                              ┌───────┐   ┌───────────────┐
                              │ 404   │   │ Increment     │
                              │ Page  │   │ Click Counter │
                              └───────┘   └───────┬───────┘
                                                  │
                                                  ▼
                                         ┌────────────────┐
                                         │ Redirect to    │
                                         │ Original URL   │
                                         └────────────────┘
```

### Workflow Explanation

1. **User Input**  
   The user enters a long URL on the home page.

2. **URL Normalization**  
   The application removes unnecessary leading/trailing whitespace.

3. **URL Validation**  
   The URL is checked using `urlparse()`. It must use either `http://` or `https://` and contain a valid network location/domain.

4. **Short Code Generation**  
   A random 6-character combination of letters and numbers is generated. The application checks the existing codes to avoid collisions.

5. **Data Storage**  
   The short code, original URL, and initial click count are stored in `data/urls.json`.

6. **Short URL Generation**  
   Flask creates a complete short URL such as:

   ```text
   http://127.0.0.1:5000/aB92xK
   ```

7. **Redirection**  
   When the user visits the short URL, Flask searches for the corresponding code.

8. **Click Tracking**  
   If the code exists, its click count is increased by one.

9. **Original URL Redirect**  
   The user is redirected to the original long URL.

10. **404 Handling**  
    If the short code does not exist, a custom 404 page is displayed.

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Shashank14105/URL-Shortener.git
cd URL-Shortener
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

The application will start on:

```text
http://127.0.0.1:5000
```

Open the address in your web browser.

---

## 🧪 Example

Suppose the user enters:

```text
https://www.example.com/a/very/long/url
```

The application may generate:

```text
http://127.0.0.1:5000/X7kP2a
```

When the user opens the short URL:

```text
/X7kP2a
```

the application:

```text
Short Code → Find URL → Increment Clicks → Redirect
```

---

## 💾 Data Format

The application stores URL information in `data/urls.json`.

Example:

```json
{
    "X7kP2a": {
        "original_url": "https://www.example.com/a/very/long/url",
        "clicks": 3
    }
}
```

Where:

- `X7kP2a` → Generated short code
- `original_url` → Original long URL
- `clicks` → Number of times the short URL has been accessed

---

## 🔐 Data Safety

The storage module uses a Python `threading.Lock` while reading and writing the JSON file. This helps prevent concurrent requests from corrupting the stored data.

> **Note:** This project uses JSON file storage for simplicity and learning purposes. A production URL shortener would typically use a database such as PostgreSQL, MySQL, MongoDB, or Redis.

---

## 📌 API Routes

| Method | Route | Description |
|---|---|---|
| `GET` | `/` | Displays the URL shortener interface |
| `POST` | `/shorten` | Validates and shortens a submitted URL |
| `GET` | `/<code>` | Redirects to the original URL and increments clicks |
| `GET` | Any invalid route | Displays the custom 404 page |

---

## 🔮 Future Improvements

Possible improvements for future versions:

- Add a database instead of JSON storage
- Add custom aliases for short URLs
- Add URL expiration
- Add QR code generation
- Add user authentication
- Add an analytics dashboard
- Add API endpoints for programmatic URL shortening
- Add rate limiting and stronger URL validation
- Deploy the application using a production WSGI server
- Add automated tests

---

## 📄 License

This project is intended for educational and development purposes.

---

## ⭐ Author

**Shashank Kumar**

GitHub: [https://www.github.com/Shashank14105](https://www.github.com/Shashank14105)

