# SQL-ALCHEMY
# Restaurant Review App

This is a restaurant review application that allows users to review and rate restaurants. It provides features for managing restaurants, customers, and their reviews. The project is built using Python and SQLAlchemy for database management.
# Table of Contents

   # Getting Started
        Prerequisites
        Installation
  # Usage
        Database Setup
        Running the Application
   #  Project Structure
   #  Contributing
   #  License

# Getting Started
# Prerequisites

Before you begin, ensure you have met the following requirements:

    Python 3.x installed
    SQLAlchemy installed (you can install it using pip install SQLAlchemy)
    SQLite or another supported database system

# Installation

    Clone the repository:

    shell

git clone https://github.com/your-username/restaurant-review-app.git
cd restaurant-review-app

Set up a virtual environment (optional but recommended):

shell

python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install project dependencies:

shell

    pip install -r requirements.txt

Usage
Database Setup

    Create the database tables by running migrations:

    shell

python manage.py db init
python manage.py db migrate
python manage.py db upgrade

Seed the database with sample data:

shell

    python seeds.py

Running the Application

Start the application:

shell

python app.py

The application will start and be accessible at http://localhost:5000. You can access the endpoints and interact with the restaurant review system.

# Project Structure

    app.py: The main application file.
    models.py: SQLAlchemy model definitions for Restaurant, Customer, and Review.
    seeds.py: A script to populate the database with sample data.
    migrations/: Directory containing database migration scripts.
    templates/: HTML templates for the user interface (if applicable).
    static/: Static assets (CSS, JavaScript, images, etc.).

# Features

    View and manage restaurants.
    View and manage customers.
    Add and delete restaurant reviews.
    Find a customer's favorite restaurant.
    Retrieve the fanciest restaurant based on price.
    View all reviews for a restaurant.
    ...

# Contributing

# Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

    Fork the project.
    Create your feature branch (git checkout -b feature/your-feature-name).
    Commit your changes (git commit -am 'Add some feature').
    Push to the branch (git push origin feature/your-feature-name).
    Create a new pull request.

# License

This project is licensed under the MIT License.
AUTHOR:BRIAN MARTIN