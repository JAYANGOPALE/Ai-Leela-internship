# Part 1: Hello Flask - The Basics

## 🎯 Learning Goals
- Create your first Flask application
- Understand the `@app.route()` decorator
- Run a development server
- See the request-response cycle in action

## 📖 Concepts Covered

### The Flask App Structure
```python
from flask import Flask      # 1. Import
app = Flask(__name__)        # 2. Create app

@app.route('/')              # 3. Define route
def home():                  # 4. Handler function
    return "Hello!"          # 5. Response

app.run(debug=True)          # 6. Start server
```

### What is `@app.route('/')`?
- It's a **decorator** that tells Flask which URL should trigger the function
- `/` means the home page (root URL)
- `/about` would mean `localhost:5000/about`

### What is `debug=True`?
- Auto-reloads server when you save changes
- Shows detailed errors in the browser
- **Never use in production!**

## 🚀 How to Run

```bash
# Make sure you're in the part-1 folder
cd part-1

# Run the app
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Debugger is active!
```

Open `http://localhost:5000` in your browser.

## ✏️ Exercises

1. **Change the message** - Edit the return text and refresh browser
2. **Return HTML** - Try returning `<h1>Hello</h1>` instead of plain text
3. **Add a route** - Create `/about` route that returns different text

## ✅ Checklist
- [ ] Server runs without errors
- [ ] Browser shows "Hello Flask!" message
- [ ] Completed at least one exercise
