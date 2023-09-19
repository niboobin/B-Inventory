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

- Create a file named `requirements.txt` and added these dependencies :
    
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

- Create a django project, I use the name "inventory"
    
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

# Assignment 3

## Step by step Assignment Explanation

#### 1. Create a data input to show the product data
- Create `forms.py` in the main folder
    ```
    from django.forms import ModelForm
    from main.models import Product

    class ProductForm(ModelForm):
        class Meta:
            model = Product
            fields = ["name", "price", "description"]
    ```

- Add some imports and create_product function in `views.py`
    ```
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    from main.forms import ProductForm
    from main.models import Product

    def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
    ```

- Import the create_product function and add a new url path in `urls.py` inside the main folder

    ```
    from main.views import show_main, create_product

    path('create-product', create_product, name='create_product'),
    ```

- Create a new HTML file `create_product.html` in the templates folder
    ```
    {% extends 'base.html' %} 

    {% block content %}
    <h1>Add New Product</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Product"/>
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}
    ```

- Update the `main.html`
    ```
    <table>
        <tr>
            <th>Name</th>
            <th>Price</th>
            <th>Description</th>
            <th>Date Added</th>
        </tr>

        {% comment %} Below is how to show the product data {% endcomment %}

        {% for product in products %}
            <tr>
                <td>{{product.name}}</td>
                <td>{{product.price}}</td>
                <td>{{product.description}}</td>
                <td>{{product.date_added}}</td>
            </tr>
        {% endfor %}
    </table>

    <br />

    <a href="{% url 'main:create_product' %}">
        <button>
            Add New Product
        </button>
    </a>
    ```



#### 2. Add 5 `views` to view the added objects in HTML, XML, JSON, XML by ID, and JSON by ID formats.
- add all the views to the `views.py` in the main directory
    ```
    def show_xml(request):
        data = Product.objects.all()
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    def show_xml_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
    
#### 3. Add all the new URL path and import all the functions
- Import all the functions you created earlier
    ```
    from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
    ```

- Add the new URL path for all the views you created
    ```
    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-product', create_product, name='create_product'),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    ]
    ```
    


## Difference between POST form and GET form

In Django, both POST and GET are HTTP methods used to submit form data from the client to the server. However, they have distinct characteristics and are used for different purposes.

GET Method:

- Parameters are appended to the URL as a query string.
- Limited amount of data can be sent because URL has length     restrictions.
- Data is visible in the URL, making it less secure for sensitive or confidential information.
- Typically used for data retrieval and non-sensitive operations.
- Parameters can be bookmarked, making it easier to share links.

POST Method:

- Parameters are sent in the body of the HTTP request, not visible in the URL.
- Can handle larger amounts of data and various data types (e.g., file uploads).
- More secure for sensitive information as it's not visible in the URL.
- Typically used for data submission and sensitive operations.
- Parameters are not bookmarkable, and refreshing the page does not resubmit the data.

## Main differences between XML, JSON, and HTML in the context of data delivery

XML (Extensible Markup Language), JSON (JavaScript Object Notation), and HTML (HyperText Markup Language) are all widely used for data exchange and delivery, but they serve different purposes and have distinct characteristics in the context of data delivery:

1. Purpose and Usage:

    - XML: Designed to store and transport data, primarily used for data representation and data interchange between systems. It provides a way to structure and organize data in a hierarchical format using tags.
    - JSON: Primarily used for data interchange between a server and a web application. It is often used to transmit data between a server and a web page. JSON is derived from JavaScript and provides a lightweight, human-readable format for representing data structures.
    - HTML: Primarily used for rendering content in web browsers. It defines the structure of web pages and specifies how content should be displayed in a browser.

2. Syntax and Structure:

    - XML: Uses a tag-based structure with opening and closing tags to define elements and their attributes. It allows nesting elements to create a hierarchical structure.
    - JSON: Uses key-value pairs to represent data objects, and arrays to represent ordered lists of values. It has a more concise and lightweight syntax compared to XML.
    - HTML: Also uses a tag-based structure similar to XML, but it is specifically designed for rendering content in web browsers. HTML elements define the structure of a web page.

3. Data Types:

    - XML: Supports various data types, including text, numbers, dates, and more. It provides flexibility in defining custom data types and structures.
    - JSON: Supports basic data types such as strings, numbers, booleans, null, arrays, and objects. It's simple and effective for most data representation needs.
    - HTML: Primarily focused on representing text-based content, links, images, forms, and other web page elements.

## Why JSON is often used in data exchange between modern web applications

JSON (JavaScript Object Notation) is commonly used in data exchange between modern web applications for several reasons:

1. Lightweight and Efficient:

    - JSON is a lightweight and compact data-interchange format, making it efficient for transmitting data over networks. Its concise syntax reduces both bandwidth usage and processing time.

2. Easy to Read and Write:

    - JSON's syntax is simple and human-readable, making it easy for developers to understand and write. It closely resembles JavaScript object notation, which is familiar to many developers.

3. Versatile Data Types:

    - JSON supports various data types, including strings, numbers, booleans, null, arrays, and objects. This versatility allows for flexible representation of complex data structures and hierarchies.


## Postman Screenshots

HTML
![HTML](https://cdn.discordapp.com/attachments/1153252018023043093/1153252041121075251/image.png)

JSON
![JSON](https://cdn.discordapp.com/attachments/1153252018023043093/1153258010714579004/image.png)

XML
![XML](https://cdn.discordapp.com/attachments/1153252018023043093/1153258106302779422/image.png)

JSON/1
![JSONID](https://cdn.discordapp.com/attachments/1153252018023043093/1153258467688194079/image.png)

XML/1
![XMLID](https://cdn.discordapp.com/attachments/1153252018023043093/1153258331666907206/image.png)