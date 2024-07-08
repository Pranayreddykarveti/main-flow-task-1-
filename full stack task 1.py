#!/usr/bin/env python
# coding: utf-8

# In[1]:


# HTML content
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Landing Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>Welcome to Our Website</h1>
            <p>Your journey to excellence begins here.</p>
            <a href="#cta" class="cta-button">Get Started</a>
        </header>
        <section class="features">
            <div class="feature">
                <h2>Feature One</h2>
                <p>Description of feature one.</p>
            </div>
            <div class="feature">
                <h2>Feature Two</h2>
                <p>Description of feature two.</p>
            </div>
            <div class="feature">
                <h2>Feature Three</h2>
                <p>Description of feature three.</p>
            </div>
        </section>
        <footer>
            <p>&copy; 2024 Your Company. All rights reserved.</p>
        </footer>
    </div>
</body>
</html>
'''

# CSS content
css_content = '''
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

header {
    text-align: center;
    padding: 50px 0;
    background-color: #333;
    color: white;
}

header h1 {
    margin: 0;
    font-size: 3em;
}

header p {
    font-size: 1.2em;
    margin: 20px 0;
}

.cta-button {
    display: inline-block;
    padding: 10px 20px;
    background-color: #007BFF;
    color: white;
    text-decoration: none;
    border-radius: 5px;
}

.cta-button:hover {
    background-color: #0056b3;
}

.features {
    display: flex;
    justify-content: space-around;
    padding: 50px 0;
    background-color: white;
}

.feature {
    text-align: center;
    width: 30%;
}

.feature h2 {
    font-size: 2em;
    margin: 10px 0;
}

.feature p {
    font-size: 1em;
    color: #555;
}

footer {
    text-align: center;
    padding: 20px 0;
    background-color: #333;
    color: white;
}
'''

# Write HTML content to a file
with open('index.html', 'w') as html_file:
    html_file.write(html_content)

# Write CSS content to a file
with open('styles.css', 'w') as css_file:
    css_file.write(css_content)

print("HTML and CSS files have been created.")


# In[ ]:




