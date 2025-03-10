Below is the revised, professional README.md file incorporating all the provided information with a clear, step-by-step structure.

---

# Product Management API

**CONFIDENTIAL: For Vibeosys Software Pvt LTD Use Only**

This document provides detailed, step-by-step instructions for setting up and using the Product Management API. Follow the guidelines below to get your API up and running.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [1. Database Setup](#1-database-setup)
  - [2. Project Setup](#2-project-setup)
  - [3. Running the API](#3-running-the-api)
- [API Endpoints](#api-endpoints)
  - [Add Product](#1-add-product)
  - [List Products](#2-list-products)
  - [Get Product Info](#3-get-product-info)
  - [Update Product](#4-update-product)
- [Data Specifications](#data-specifications)
  - [Product Categories](#product-categories)
  - [Units of Measure](#units-of-measure)
- [Response Codes](#response-codes)
- [Project Structure](#project-structure)

---

## Prerequisites

- **Python 3.11** or higher
- **MySQL Server**
- **Git** (optional)

---

## Setup Instructions

### 1. Database Setup

1. Log into your MySQL server and execute the following SQL commands:

   ```sql
   CREATE DATABASE products_db;
   USE products_db;
   CREATE TABLE products (
       product_id BIGINT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(100) NOT NULL,
       category ENUM('finished', 'semi-finished', 'raw') NOT NULL,
       description VARCHAR(250),
       product_image TEXT,
       sku VARCHAR(100) UNIQUE NOT NULL,
       unit_of_measure ENUM('mtr', 'mm', 'ltr', 'ml', 'cm', 'mg', 'gm', 'unit', 'pack') NOT NULL,
       lead_time INT(3) NOT NULL,
       created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
       updated_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
   );
   ```

### 2. Project Setup

1. **Create a Virtual Environment:**

   Open your terminal and run:

   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment:**

   - **Windows:**

     ```cmd
     venv\Scripts\activate
     ```

   - **Linux/Mac:**

     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies:**

   With the virtual environment activated, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**

   Create a `.env` file in the project root with the following content. Replace `your_password` with your MySQL password.

   ```env
   DATABASE_URL=mysql+mysqlconnector://root:your_password@localhost:3306/products_db
   ```

### 3. Running the API

Start the server using Uvicorn:

```bash
uvicorn app.main:app --reload
```

Once the server is running, the API will be available at:

- **API Base URL:** [http://localhost:8000](http://localhost:8000)
- **Swagger Documentation:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc Documentation:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## API Endpoints

### 1. Add Product

- **Request (Bash):**

  ```bash
  curl -X POST "http://localhost:8000/product/add" \
  -H "Content-Type: application/json" \
  -d '{
      "name": "Steel Rod",
      "category": "raw",
      "description": "High quality steel rod",
      "product_image": "https://example.com/steel-rod.jpg",
      "sku": "SR001",
      "unit_of_measure": "mtr",
      "lead_time": 5
  }'
  ```

- **Windows CMD:**

  ```cmd
  curl -X POST "http://localhost:8000/product/add" -H "Content-Type: application/json" -d "{\"name\": \"Steel Rod\", \"category\": \"raw\", \"description\": \"High quality steel rod\", \"product_image\": \"https://example.com/steel-rod.jpg\", \"sku\": \"SR001\", \"unit_of_measure\": \"mtr\", \"lead_time\": 5}"
  ```

### 2. List Products

- **Default Pagination (10 items per page):**

  ```bash
  curl "http://localhost:8000/product/list"
  ```

- **Custom Pagination:**

  ```bash
  curl "http://localhost:8000/product/list?page=1&page_size=5"
  ```

### 3. Get Product Info

Retrieve detailed information for a product with a specific ID:

```bash
curl "http://localhost:8000/product/1/info"
```

### 4. Update Product

- **Request (Bash):**

  ```bash
  curl -X PUT "http://localhost:8000/product/1/update" \
  -H "Content-Type: application/json" \
  -d '{
      "name": "Modified Steel Rod",
      "lead_time": 7,
      "description": "Updated high quality steel rod"
  }'
  ```

- **Windows CMD:**

  ```cmd
  curl -X PUT "http://localhost:8000/product/1/update" -H "Content-Type: application/json" -d "{\"name\": \"Modified Steel Rod\", \"lead_time\": 7, \"description\": \"Updated high quality steel rod\"}"
  ```

---

## Data Specifications

### Product Categories

- **finished**
- **semi-finished**
- **raw**

### Units of Measure

- **mtr** (Meter)
- **mm** (Millimeter)
- **ltr** (Liter)
- **ml** (Milliliter)
- **cm** (Centimeter)
- **mg** (Milligram)
- **gm** (Gram)
- **unit**
- **pack**

---

## Response Codes

- **200:** Success
- **201:** Created successfully
- **400:** Bad request (e.g., duplicate SKU)
- **404:** Resource not found
- **422:** Validation error
- **500:** Server error

---

## Project Structure

```
product_api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── routes.py
├── requirements.txt
└── README.md
```

---

