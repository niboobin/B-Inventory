# Assignment 2
### Muhammad Obin Mandalika -2206046771

> [Link](https://b-inventorypro.adaptable.app/) to access

## Step by step Assignment Explanation

#### 1. Creating a new Django Project
    - Create a python virtual environment

    ```
    python -m venv env
    ```

    - Activate the virtual environment

    ```
    env\Scripts\activate
    ```

    - I create a file named `requirements.txt` and added these dependencies :
    
    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ``` 

    - Install the dependencies :
    
    ```
    pip install -r requirements.txt
    ```

    - create a django project, i use the name "inventory"
    
    ```
    django-admin startproject inventory .
    ```

    - Finally, in the main directory, open `settings.py` and add `"*"` to `ALLOWED_HOST`
    The list of hosts permitted to access the web application is called ALLOWED_HOSTS. The application will be broadly accessible since you allow access from any host by changing the value to ["*"]

#### 2. Creating a new app for the project
  - Create a `main` application in the B-Inventory project by running the following command :
  
  ```
  python manage.py startapp main
  ```

  - We have to register the app by adding `main` in `settings.py`
  - Create a new folder `templates` inside the main directory and create `main.html`

#### 3. Creating a URL routing config to access the `main` app
    - Inside the `inventory` directory, Import the `include` function in `urls.py`

    -  in the `urls.py` add 
   
    ```
    path('main/', include('main.urls'))
    ```

#### 4. Creating a model on the main app
    - In `models.py`, create a class named `Item` and fill in these attributes :
        - `name` as the name of the item, with type `CharField`.
        - `amount` as the amount/count of the item, with type `IntegerField`.
        - `description` as the description of the item, with type `TextField`.
        - `price` as the amount that items worth, with type `TextField`

    - Create model migrations with:
    
    ```
    python manage.py makemigrations
    ```

    - After that, apply the migrations with the local database :
    
    ```
    python manage.py migrate
    ```

#### 5. Integrating MVT Components
    - In the `main` directory, open `views.py` and add the following codes :

    ```
     from django.shortcuts import render

    def show_main(request):
    context = {
        'application_name': 'B-Inventory',
        'name': 'Muhammad Obin Mandalika',
        'class': 'PBP KKI'
    }

    return render(request, 'main.html', context)
    ```

#### 6. Routing in `urls.py` to map the function in `views.py` to an URL
    - In the main `directory`,  create `urls.py` and add the following codes :

    ```
    from django.urls import path
    from main.views import show_main
    
    app_name = 'main'

    urlpatterns = [
       path('', show_main, name='show_main'),
    ]
    ```

#### 7. Deploy the app to adaptable
    - Add,commit, and push the project to the repository 
    - Deploy the app to adaptable

## Django Diagram

![Diagram](https://cdn.discordapp.com/attachments/314315831465213953/1151309311671291977/image.png)

`Client/Browser`: Represents the users interacting with the web application through their web browsers or client-side applications.

`urls.py`: Maps incoming URLs to specific views or controllers and Determines which view should handle a particular HTTP request.

`Templates`:Contains HTML and presentation logic,
Used to generate the user interface and render dynamic content, Templates can include placeholders for data provided by views.

`views.py`: Handle incoming HTTP requests,
Contain the application's logic, Interact with models to retrieve or manipulate data, Render templates to generate HTML responses.

`models.py`: Define the data structure and interact with the database, Represent the application's data and business logic, Provide an object-oriented interface for database operations.

`Database`: Stores the application's data, often using a relational database management system (e.g., PostgreSQL, MySQL). Models define the database schema, and Django's Object-Relational Mapping (ORM) manages database interactions.

## Purpose of Virtual Environment

A virtual environment is a self-contained directory or environment that allows you to isolate and manage Python packages and
dependencies for a specific project or application.
Now, regarding Django web applications, it is highly recommended to create and use a virtual environment for your Django projects. You can technically create a Django web app without a virtual environment, but it's generally considered a bad practice for the reasons mentioned above. When you create a Django project within a virtual environment, you can control and isolate the Python packages and dependencies specific to that project, making it easier to manage and deploy your application.


## MVC, MVT MVVM
MVC(Model-View-Controller) is a general architectural pattern used in various application types.

MVT(Model-View-Template) is a variation of MVC tailored for web development, emphasizing the separation of presentation logic into templates.

MVVM(Model-View-ViewModel) is used primarily in client-side web applications, focusing on two-way data binding and separating the View from the underlying logic in the ViewModel.

