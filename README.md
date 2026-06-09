AI Based Online Cake Ordering and Recommendation System (BakeBridge)
Project Overview

BakeBridge is an AI-powered online bakery ordering system developed using Django and Machine Learning. The system allows users to browse bakery products, add items to cart, manage quantities, receive intelligent product recommendations, and view analytics through an interactive dashboard.

Features
User Registration and Login
Browse Multiple Product Categories
Add Products to Cart
Increase or Decrease Product Quantity
Remove Products from Cart
AI-Based Product Recommendation System
Machine Learning Category Prediction
Analytics Dashboard
Customer Purchase Analysis
Modern User-Friendly Interface
Product Categories
Cakes
Cupcakes
Bouquets
Brownies
Pastries
Cookies
Savouries
Technologies Used
Backend
Python
Django Framework
Frontend
HTML
CSS
JavaScript
Database
SQLite
Data Processing
Pandas
NumPy
Machine Learning
Scikit-learn
Decision Tree Classifier
Joblib
Visualization
Chart.js
Dataset
CSV Dataset containing 200 customer purchase records
Machine Learning Module

The project uses a Decision Tree Classifier to predict the customer's preferred product category based on:

Total Purchase Amount
Quantity of Products Purchased

The trained model is stored using Joblib as:

model.pkl
encoder.pkl
Recommendation System

The recommendation engine uses a dataset of 200 customer purchase records.

It analyzes previous customer buying patterns and suggests related bakery products to users.

Example:

If a customer purchases a cake, the system may recommend:

Brownies
Cupcakes
Bouquets
Analytics Dashboard

The dashboard provides useful insights such as:

Total Sales
Total Items Purchased
Top Selling Product
Most Preferred Category
Category Distribution Charts
Predicted Customer Category
System Workflow
User visits the website.
User signs up or logs in.
User browses bakery products.
Products are added to the cart.
Cart stores quantity and pricing information.
Machine Learning model predicts preferred category.
Recommendation engine suggests related products.
Analytics dashboard displays customer insights.
Project Structure
bakebridge_project/
│
├── bakery/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── urls.py
│   ├── model.pkl
│   ├── encoder.pkl
│   └── ...
│
├── bakebridge_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── bakery_orders_200_records.csv
├── db.sqlite3
├── manage.py
└── README.md
Installation Steps
1. Clone the Repository
git clone <repository-url>
cd bakebridge_project
2. Create Virtual Environment
python -m venv venv
3. Activate Virtual Environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate
4. Install Dependencies
pip install django pandas numpy scikit-learn joblib
5. Apply Migrations
python manage.py migrate
6. Run the Server
python manage.py runserver
7. Open the Application

Open your browser and visit:

http://127.0.0.1:8000/
Expected Output
Functional online bakery ordering system.
AI-based product recommendations.
Customer category prediction using Machine Learning.
Interactive analytics dashboard.
Enhanced customer shopping experience.
Future Scope
Online Payment Gateway Integration
Order Tracking System
Mobile Application Development
Admin Dashboard for Bakery Owners
Advanced Deep Learning Recommendation Models
Email and SMS Notifications
Conclusion

BakeBridge successfully combines web development and machine learning to create an intelligent bakery ordering platform. The system improves customer experience through personalized recommendations, predictive analytics, and an attractive user interface, making bakery management smarter and more efficient.

Developed By

Vinita Pawar
