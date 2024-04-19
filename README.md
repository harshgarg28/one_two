# API Documentation

This API is built using Flask, a lightweight web framework in Python, and PostgreSQL, a powerful open-source relational database management system. It provides endpoints for managing products, including creating, updating, deleting, and retrieving product information.

## Base URL

The base URL for accessing the API is: `https://one-two.onrender.com`

## Endpoints

### 1. GET /api/products

#### Description
Retrieve a list of all products stored in the database.

#### Request
- Method: GET
- URL: `/api/products`

#### Response
- Body: JSON array of product objects. Each object contains `id`, `name`, and `price` attributes.

### 2. POST /create

#### Description
Create a new product entry in the database.

#### Request
- Method: POST
- URL: `/create`
- Body Parameters:
  - `name`: Name of the product (string)
  - `price`: Price of the product (float)

#### Response
- Redirects to the homepage (`/`) after successful creation.

### 3. POST /update

#### Description
Update an existing product entry in the database.

#### Request
- Method: POST
- URL: `/update`
- Body Parameters:
  - `id`: ID of the product to be updated (integer)
  - `name`: New name of the product (string)
  - `price`: New price of the product (float)

#### Response
- Redirects to the homepage (`/`) after successful update.

### 4. POST /delete

#### Description
Delete a product entry from the database.

#### Request
- Method: POST
- URL: `/delete`
- Body Parameters:
  - `id`: ID of the product to be deleted (integer)

#### Response
- Redirects to the homepage (`/`) after successful deletion.

## Running Locally
To run this API locally, make sure you have Python and PostgreSQL installed. Then follow these steps:
1. Clone this repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Set up your PostgreSQL database and update the `DATABASE_URL` environment variable in the `.env` file with your database connection string.
4. Run the Flask application with `python app.py`.
5. Access the API endpoints using a web browser or tools like cURL or Postman.

## Deployment
This API is deployed on Render. Any changes pushed to the repository will automatically trigger a deployment.
