# Part 4: Dynamic Routes - URL Parameters

## 🎯 Learning Goals
- Create dynamic routes with `<variable>` syntax
- Use type converters (`int`, `float`, `path`)
- Capture multiple parameters in one route
- Use `url_for()` to generate URLs dynamically

## 📖 Concepts Covered

### Basic Dynamic Route
```python
@app.route('/user/<username>')
def user_profile(username):
    return f"Hello, {username}!"
```
Visit `/user/Alice` → "Hello, Alice!"

### Type Converters
```python
@app.route('/post/<int:post_id>')    # Only integers
@app.route('/price/<float:amount>')  # Floating point
@app.route('/file/<path:filepath>')  # Includes slashes
```

### Multiple Parameters
```python
@app.route('/user/<username>/post/<int:post_id>')
def user_post(username, post_id):
    return f"{username}'s post #{post_id}"
```

### url_for() Function
```python
from flask import url_for

# Generate URLs dynamically
url_for('home')                        # Returns '/'
url_for('user_profile', username='Bob') # Returns '/user/Bob'
```

In templates:
```html
<a href="{{ url_for('user_profile', username='Alice') }}">Alice</a>
```

## 🚀 How to Run

```bash
cd part-4
python app.py
```

Try these URLs:
- `http://localhost:5000/` - Home with demos
- `http://localhost:5000/user/YourName` - Dynamic user page
- `http://localhost:5000/post/1` - Post by ID
- `http://localhost:5000/user/Alice/post/1` - Multiple params
- `http://localhost:5000/links` - url_for() demo

## ✏️ Exercises

1. **Create a product route** - `/product/<int:id>` with product data
2. **Add category routes** - `/category/<name>/product/<int:id>`
3. **Build a search route** - `/search/<query>`

## ✅ Checklist
- [ ] User route works with different names
- [ ] Post route accepts only integers
- [ ] Multiple parameter routes work
- [ ] url_for() generates correct URLs
