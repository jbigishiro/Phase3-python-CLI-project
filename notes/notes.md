# Phase 3 project Notes

## In this project, we're going to use these skills to create a CLI. You won't be able to fit everything in from phase 3, but the following are the minimum requirements

- A CLI application that solves a real-world problem and adheres to best practices.
- A database created and modified with SQLAlchemy ORM with 2+ related tables.
- A well-maintained virtual environment using Pipenv.
- Proper package structure in your application.
- Use of lists and dicts.

## Consider these stretch goals as you progress through your project

A database created and modified with SQLAlchemy ORM with 3+ related tables.
Use of many-to-many relationships with SQLAlchemy ORM.
Use of additional data structures, such as ranges and tuples.

A rubric for this project is available on the next page in this Canvas module. Make sure to take a look before you get started!

# Main idea: Supplier App

## User story

Suppliers can add, update, read and delete their product details. Users can view different products and their suppliers

How I will use the concepts I recently learned to meet the project requirements:

## Object Oriented Python

- Class for Supplier with attributes

- Class for Product with attributes

## Database Tables

### Table: Product

ProductID: INTEGER NOT NULL PRIMARY KEY AUTO INCREMENTED
ProductName: STRING NOT NULL
SupplierID: STRING NOT NULL
UnitPrice: FLOAT

### Table: Supplier

SupplierID: INTEGER NOT NULL PRIMARY KEY AUTO INCREMENTED
CompanyName: STRING 
Address: STRING 
HomePage: STRING UNIQUE

## Object Relationships

The relationship between Supplier and Product is one-to-many.

## Aggregate and Association Methods

The supplier can add, remove or update product information.

## Use of Data Structures

A user can make a list of suppliers from his city
A user can make a dictionary of the most expensive products and their respective price
