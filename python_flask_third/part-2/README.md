# Part 2: Templates - Rendering HTML Files

## 🎯 Learning Goals
- Use the `templates/` folder to store HTML files
- Learn the `render_template()` function
- Understand separation of concerns (Python vs HTML)
- Create multiple pages with navigation

## 📖 Concepts Covered

### Why Templates?
In Part 1, we returned HTML as strings:
```python
return "<h1>Hello</h1>"  # Hard to maintain!
```

With templates, we keep HTML in separate files:
```python
return render_template('index.html')  # Clean and organized!
```

### The templates/ Folder
Flask automatically looks for a folder named `templates/` in your project:
```
part-2/
├── app.py
└── templates/      <- Flask looks here!
    ├── index.html
    └── about.html
```

### Using render_template()
```python
from flask import Flask, render_template  # Import it!

@app.route('/')
def home():
    return render_template('index.html')  # Renders templates/index.html
```

## 🚀 How to Run

```bash
cd part-2
python app.py
```

Visit:
- `http://localhost:5000/` - Home page
- `http://localhost:5000/about` - About page

## ✏️ Exercises

1. **Modify the templates** - Add your own content to `index.html`
2. **Create a contact page** - Add `contact.html` and a `/contact` route
3. **Add navigation** - Make sure all pages link to each other

## ✅ Checklist
- [ ] Both pages render correctly
- [ ] Navigation links work
- [ ] Created at least one new template
