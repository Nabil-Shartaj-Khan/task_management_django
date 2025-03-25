<h1> *My First Django App* </h1> 
created for my course assignment.

To run, use command: python manage.py runserver --insecure 

User can add and view tasks based on certain categories. Admin can add, view, delete and update the tasks and categories using django admin panel.


*Security Implementations*

🔒 CSRF Protection: All forms include {% csrf_token %} to prevent cross-site request forgery.

🔒 SQL Injection Prevention: Uses get_object_or_404() instead of raw SQL queries.

🔒 Role-Based Access Control: Only admins can manage categories and tasks.

🔒 Custom Error Handling: Implements custom 404.html and 500.html pages to prevent data leakage.

