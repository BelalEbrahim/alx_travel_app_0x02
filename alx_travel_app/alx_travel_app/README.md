# 🧳 ALX Travel App (alx_travel_app_0x00)

A backend application for a travel booking platform built with **Django** and **Django REST Framework (DRF)**. This project provides a RESTful API to manage **travel listings, user bookings, reviews, and payments**. It serves as a practical example of building a **scalable, API-driven web service**.

---

## ✨ Key Features
- **Listings Management**: CRUD (Create, Read, Update, Delete) operations for travel listings.
- **Booking System**: Endpoints for users to create and manage their bookings.
- **User Reviews**: Functionality for users to leave reviews and ratings (1–5) on listings.
- **Payment Tracking**: Supports payment records linked to bookings, with status (`pending`, `completed`, `failed`).
- **Database Seeding**: A custom management command to populate the database with sample data for testing.
- **Environment-Based Configuration**: Securely manages settings like secret keys and database credentials using a `.env` file.

---

## 🚀 Tech Stack
- **Backend**: Python, Django  
- **API**: Django REST Framework (DRF)  
- **Database**: SQLite (default for development)  
- **Environment Variables**: `django-environ`  
- **Data Seeding**: `Faker` library for generating sample data  

---

## ⚡ Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/BelalEbrahim/alx-backend-graphql_crm.git
cd alx-backend-graphql_crm
