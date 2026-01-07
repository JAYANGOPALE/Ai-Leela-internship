# Part 3: Jinja2 Variables - Passing Data to Templates

## 🎯 Learning Goals
- Pass variables from Python to HTML templates
- Use `{{ variable }}` syntax to display data
- Use Jinja2 filters (`|upper`, `|length`, etc.)
- Loop through lists with `{% for %}`
- Use conditionals with `{% if %}`

## 📖 Concepts Covered

### Passing Variables
```python
@app.route('/')
def home():
    name = "Alex"
    return render_template('index.html', name=name)
```

In the template:
```html
<h1>Hello, {{ name }}!</h1>
```

### Jinja2 Filters
```html
{{ name|upper }}      <!-- ALEX -->
{{ name|lower }}      <!-- alex -->
{{ name|length }}     <!-- 4 -->
{{ name|title }}      <!-- Alex -->
```

### Conditionals
```html
{% if is_enrolled %}
    <span>Enrolled</span>
{% else %}
    <span>Not Enrolled</span>
{% endif %}
```

### For Loops
```html
{% for skill in skills %}
    <li>{{ skill }}</li>
{% endfor %}
```

### Loop Variables
- `loop.index` - Current iteration (starts at 1)
- `loop.index0` - Current iteration (starts at 0)
- `loop.first` - True if first iteration
- `loop.last` - True if last iteration
- `loop.length` - Total number of items

## 🚀 How to Run

```bash
cd part-3
python app.py
```

Visit:
- `http://localhost:5000/` - Single variable demo
- `http://localhost:5000/profile` - Multiple variables + conditionals
- `http://localhost:5000/skills` - Looping through a list
- `http://localhost:5000/projects` - List of dictionaries

## ✏️ Exercises

1. **Add more profile fields** - Add email, city to profile page
2. **Create a grades page** - Pass a dict of subjects and grades
3. **Style based on data** - Show different colors for different project statuses

## ✅ Checklist
- [ ] Variables display correctly on all pages
- [ ] Conditionals work (enrolled badge)
- [ ] For loops iterate through lists
- [ ] Created at least one new data-driven page
