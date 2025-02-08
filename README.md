## Overview
This is the Django-based project that follows MVC (Model-View-Controller) architecture

## Project Structure
**models.py** - defines database tables

**views.py** - fetches and process data from models.py

**urls.py** - maps URLS to views

**admin.py** - makes the models manageable via Django Admin

**apps.py**  - helps Django recognize the app inside the project

## Accounts app
In the views.py
**register functionality** - The function that takes request as a parameter that allows user to register (function name is register).

**login functionality** - The function that allows user to login (function name is login).

**dashboard functionality**  - The function that takes the request as a parameter and allows user to see the dashboard that belong to that user(function name is dashboard).

In the urls.py
**register url** - It maps the url to the views of the register function  

**login url**  - It maps the url to the view of the login function

**dashboard** - It maps the url to the view of the dashboard function

**logout** - it maps the url to the view of the logout function

## Accounts Templates 

**register.html**  - The html page that displays the registration page of the website

**login.html**  - The html page that displays the login page of the website

**dashboard.html** - The html page that displays the dashboard page of the website

## Pages app
In the views.py
**home functionality** - The function that takes request as a parameter that allows user to see the main page.

**about functionality** - The function takes request and allow user to know about the company

**services functionality**  - The function taske the request and render all the posible services

**contact functionality**  - The function allow user to contact via the site

In the urls.py
**'' url** - It maps the url to the views of the home function 

**about url**  - It maps the url to the view of the *about function

**services** - It maps the url to the view of the ervices function

**contact** - it maps the url to the view of the contact function

## Pages Templates 
**home.html**  - The html page that displays the home page of the website

**about.html**  - The html page that displays the about page of the website

**services.html** - The html page that displays the services page of the website

**contact.html** - The html page that displays the contact page of the website

**base.html**  - This will hold code that will be use accross pages html


