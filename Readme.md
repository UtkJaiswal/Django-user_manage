# User Management

Basic User Management with SignUp, Login and Logout Features

## Table of Contents

- [Installation](#installation)
- [Running the Development Server](#running-the-development-server)
- [API Endpoints](#api-endpoints)
    - [Sign Up](#sign-up)
    - [Login](#login)
    - [Logout](#logout)
    - [User Details](#user-details)




## Installation

1. Clone the repository:
```bash
git clone https://github.com/UtkJaiswal/user_manage.git
```


2. Change to the project directory:
```bash
cd user_manage
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```




## To start the development server

```bash
python manage.py runserver
```


The server will be accessible at `http://localhost:8000/`.

## API Endpoints

### Sign Up

Create a new user account by sending a POST request to `/signup/`.

Request Body:

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "1234567890",
  "password": "secretpassword"
}
```

### Login

Authenticate and obtain an access token by sending a POST request to /login/.

Request Body:

```json
{
  "email": "john@example.com",
  "password": "secretpassword"
}
```

### Logout

Log out and invalidate the access token by sending a POST request to /logout/.

Request Body:

```json
{
  "refresh_token": "your_refresh_token"
}
```

### User Details

Fetch user details by sending a GET request to /user-details/.

Requires authentication with an access token provided in the Authorization header as:

`Authorization: Bearer your_access_token_here`





