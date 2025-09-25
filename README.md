<h1>🛍️ Flask E-Commerce Web App</h1>

<p>
A simple yet powerful <strong>Flask-based e-commerce application</strong> built for learning and experimentation.  
The project supports <em>user authentication</em>, <em>role-based access</em>, and <em>SQLite database integration</em> for managing users, products, and orders.
</p>

<hr>

<h2>📂 Project Layout</h2>

<p>The repository is organized as follows:</p>

<pre>
ECOMMERCE_APP/
├── instance/            # Contains SQLite database file
│   └── ecommerce.db
├── routes/              # Modular route blueprints
│   ├── orders/          # Order-related routes
│   │   └── orders.py
│   ├── products/        # Product-related routes
│   │   └── products.py
│   └── users/           # User authentication routes
│       └── users.py
├── static/              # CSS, JS, images
│   └── style.css
├── templates/           # HTML templates (Jinja2)
│   ├── orders/
│   │   ├── orders.html
│   │   └── place_order.html
│   ├── products/
│   │   ├── add_product.html
│   │   └── products.html
│   ├── users/
│   │   └── home.html
│   └── layout.html      # Base layout for all pages
├── app.py               # Main application entry point
├── models.py            # Database models/schema
├── requirements.txt     # Python dependencies
</pre>

<hr>

<h2>🗄️ Database Design</h2>

<p>The application uses <strong>SQLite</strong> as the default database.  
Three main tables are used to support different roles and operations:</p>

<ul>
  <li><strong>Users</strong> → Stores login info & roles (Customer, Seller, Admin)</li>
  <li><strong>Products</strong> → Keeps product details (name, price, stock, seller)</li>
  <li><strong>Orders</strong> → Tracks customer purchases (product, quantity, date)</li>
</ul>

<hr>

<h2>👥 Roles & Permissions</h2>

<ul>
  <li><strong>Customer:</strong> Register, log in, browse products, place orders</li>
  <li><strong>Seller:</strong> Log in, add products, update stock & pricing</li>
  <li><strong>Admin:</strong> Manage users, monitor products, view all orders</li>
</ul>

<hr>

<h2>⚙️ Getting Started</h2>

<ol>
  <li>Clone this repository:
    <pre><code>git clone &lt;repo-url&gt;</code></pre>
  </li>
  <li>Create and activate a virtual environment</li>
  <li>Install dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Initialize the SQLite database (or use the included <code>ecommerce.db</code>)</li>
  <li>Run the Flask app:
    <pre><code>flask run</code></pre>
  </li>
  <li>Visit <a href="http://127.0.0.1:5000" target="_blank">http://127.0.0.1:5000</a> in your browser</li>
</ol>

<hr>

<h2>✨ Features</h2>

<ul>
  <li>User registration and login with hashed passwords</li>
  <li>Role-based navigation (Customer, Seller, Admin)</li>
  <li>Product catalog with add/edit functionality</li>
  <li>Shopping cart & order placement system</li>
  <li>Admin dashboard for management</li>
  <li>Beginner-friendly SQLite integration</li>
</ul>

<hr>

<h2>🚀 Future Improvements</h2>

<ul>
  <li>Add product categories and search functionality</li>
  <li>Improve UI with Bootstrap or Tailwind</li>
  <li>Generate order invoices</li>
  <li>Switch database to PostgreSQL/MySQL for production</li>
</ul>
