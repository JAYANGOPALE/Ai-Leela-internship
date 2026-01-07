# Part 5: Mini Project - Personal Website

## 🎯 Learning Goals
- Combine all Flask concepts into a complete project
- Use template inheritance with a base template
- Serve static files (CSS)
- Build a multi-page website with navigation
- Create a personalized portfolio site

## 📖 New Concepts

### Template Inheritance
Instead of repeating the navbar and footer on every page, we use a **base template**:

```html
<!-- base.html -->
<html>
<head>...</head>
<body>
    <nav>...</nav>
    {% block content %}{% endblock %}
    <footer>...</footer>
</body>
</html>
```

Child templates extend it:
```html
<!-- index.html -->
{% extends "base.html" %}

{% block content %}
    <h1>My Content Here</h1>
{% endblock %}
```

### Static Files (CSS, JS, Images)
Flask serves static files from the `static/` folder:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

Project structure:
```
part-5/
├── app.py
├── static/
│   └── style.css
└── templates/
    ├── base.html
    ├── index.html
    └── ...
```

## 🚀 How to Run

```bash
cd part-5
python app.py
```

Visit:
- `http://localhost:5000/` - Home page
- `http://localhost:5000/about` - About & skills
- `http://localhost:5000/projects` - Project list
- `http://localhost:5000/project/1` - Project details
- `http://localhost:5000/contact` - Contact info

## ✏️ Exercises

1. **Personalize it!** - Update `PERSONAL_INFO`, `SKILLS`, and `PROJECTS` in `app.py`
2. **Add a blog page** - Create `/blog` route with blog posts
3. **Custom styling** - Modify `static/style.css` with your colors
4. **Add images** - Put images in `static/` and use them in templates

## 📂 Project Structure

```
part-5/
├── app.py                 # Main application with routes and data
├── static/
│   └── style.css          # All CSS styles
└── templates/
    ├── base.html          # Base template (navbar, footer)
    ├── index.html         # Home page
    ├── about.html         # About page with skills
    ├── projects.html      # Projects list
    ├── project_detail.html # Single project view
    └── contact.html       # Contact information
```

## ✅ Final Checklist
- [ ] All pages load correctly
- [ ] Navigation works on all pages
- [ ] CSS styles are applied
- [ ] Dynamic project pages work
- [ ] Personalized with your information
- [ ] Ready to submit screenshots!

## 📤 Submission Requirements

1. **Screenshot 1:** Terminal with `(venv)` and Flask server running
2. **Screenshot 2:** Browser showing your website at `localhost:5000`
3. **Screenshot 3:** Your `app.py` code showing `@app.route`

**Caption:** "Successfully launched my first Python server! My personal website is now being served by Flask."
