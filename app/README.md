# Home Insurance Pricing Tool

## FastAPI Application Requirements
### Install initial global dependencies:
* [PostgreSQL](https://www.postgresql.org/download/) for data storage.
* [Python3](https://www.python.org/downloads/) Application requires Python v3.11.5
* [Poetry](https://python-poetry.org/docs/#installation) for Python package and environment management.
* [FastAPI](https://fastapi.tiangolo.com/#installation) as the web framework with support for data validation using type annotations using Pydantic.

### Install application-level dependencies:
Install Python package dependencies from app directory: `./app`:

```bash
poetry install
```
You can then start the poetry created virtual environment/shell:

```bash
poetry shell
```


## Local backend startup:

* Start FastAPI application from project root directory: quote-pricing-tool or `.`:
    * This first step is necessary for the PostgreSQL database creation. The app must be started atleast once before the next step can be performed successfully. 

        ```bash
         uvicorn app.main:app --reload
        ```
    * Execute this alembic command to run scripts for quotes table creation and to seed table with test data. This command must be executed from the db directory in a new terminal: `./app/db`

        ```bash
         alembic upgrade head
        ```
* APIs can be accessed at this address: http://127.0.0.1:8000  
Example:
    * http://127.0.0.1:8000/price/quote_id/1

## Running unit tests
To run unit tests for services and router endpoints, go into the `./app/tests` directory and run:

```bash
pytest 

or 

pytest -s -vv (for more detail from test case result output)
```

## Future Enhancements
**Pricing algorithm:** Although price values returned by endpoint are exact, assignment requirements didn't specify how to round values. Sample data provided in the instructions are not using consistent pattern for rounding. It could also be the case that the front end handles what to do with final values displayed (along with '$' sign).  

**Database Setup and Seed Data for testing:** Database seeding and table creation can be optimized and automated properly on application start up, especially if this backend was dockerized to automate and organize some of initial setup steps. A second "test-sure" database would be additional improvement for organizing and running tests in separate, isolated environments so they can have a single responsibility making development workflow much more effective.  

**Future migration for quote prices:** `Quotes` table should be updated with a new `latest_price` column so that record's column is updated with that latest price when a price for a quote is requested.

**Testing:** Add test cases for failure errors and exception handling logic. Also, add test cases for asserting proper log messages based on success or failure.