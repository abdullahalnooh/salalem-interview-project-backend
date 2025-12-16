# Backend – Interview Task

## Purpose

This backend was built as part of a technical interview task. Its sole goal is to demonstrate backend fundamentals

## What This Backend Does

* Exposes a GraphQL API for CRUD operations
* Provides an admin panel for managing data
* Separates concerns clearly (settings, apps, API layer)
* Runs locally or inside Docker without special configuration

## Tech Stack

* Python
* Django
* GraphQL (Graphene)
* SQLite (default)
* Docker

## Key Endpoints

* GraphQL API: `/graphql/`
* Admin panel: `/admin/`

## Running Locally

```
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic 
python manage.py runserver
```

## Running with Docker

```
docker compose up --build
```

## Notes for Reviewers

* Business logic is intentionally simple
* Focus is on correctness, structure, and clarity
* Code is written to be readable and easy to evaluate

## Scope Limitations

* Minimal validation
* No advanced permissions
* No performance optimizations

This backend fulfills the interview requirements and is not intended as a production-ready system.
