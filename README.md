# Trading App Backend
This is the backend of a trading application, built with Django and PostgreSQL. It provides RESTful APIs to enable users to perform trading transactions and retrieve market data.


## Getting Started

### Prerequisites
Before you can run this application, you need to have the following software installed on your machine:
* Python (version 3.6 or higher)
* PostgreSQL

### Installation
1. Clone the repository:
```
git clone https://github.com/preciousimo/Trading-app-backend.git
```

2. Install dependencies:
```
cd Trading-app-backend
pip install -r requirements.txt
```

3. Create a .env file in the root directory of the project, and add the following environment variables::
```
DB_HOST=<database-host>
DB_NAME=<database-name>
DB_USER=<database-user>
DB_PASSWORD=<database-password>
```
Replace database-host, database-name, database-user, and database-password with your own values.

4. Run the database migrations:
```
python manage.py migrate
```

5. Start the server:
```
python manage.py runserver
```


## API Documentation

### Endpoints
GET /api/accounts/int:pk/
Retrieve a single trading account by ID.

GET /api/equities/
Retrieve a list of equities.

GET /api/equities/int:pk/
Retrieve a single equity by ID.

GET /api/balances/
Retrieve a list of balances.

GET /api/balances/int:pk/
Retrieve a single balance by ID.

GET /api/marketwatchtimes/
Retrieve a list of market watch times.

GET /api/marketwatchtimes/int:pk/
Retrieve a single market watch time by ID.

All endpoints require authentication, except for /api/equities/. The authenticated user can only access their own data (e.g. their own accounts, balances, etc.). 


NB: The JWT must be included in the Authorization header of the request, using the Bearer scheme.(This has not been set yet)

In addition to the above endpoints, there are also endpoints for creating, updating, and deleting objects:

POST /api/accounts/
PUT /api/accounts/int:pk/
DELETE /api/accounts/int:pk/
POST /api/equities/
PUT /api/equities/int:pk/
DELETE /api/equities/int:pk/
POST /api/balances/
PUT /api/balances/int:pk/
DELETE /api/balances/int:pk/
POST /api/marketwatchtimes/
PUT /api/marketwatchtimes/int:pk/
DELETE /api/marketwatchtimes/int:pk


## Contributing
If you find a bug or have a feature request, please open an issue on the Github repository. Pull requests are also welcome.
