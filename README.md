<details>
<summary> Assignment 2 </summary>

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

</details>
<details>
<summary> Assignment 3 </summary>

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

</details>

<details>
<summary> Assignment 4 </summary>

# Assignment 4

## Step by step explanation 

#### 1. Create a registration form and function

- In `views.py`, add imports for `redirect`, `UserCreationForm`, and `messages`. Then, create a new function called `register`

    ```
    def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
    ```
- In `urls.py`, import the register function and add the path url to `urlpatterns`.



#### 2. Create a login function

- In `views.py`, add imports for `authenticate` and `login`. Then, create a new function called `login_user.`

    ```
    def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
    ```

- Create a new file called `login.html` inside main/templates. Then import the login_user function and add the path url.

- In `views.py`, in context, we add `'last_login': request.COOKIES['last_login'],` so that it can show the last log in data.

#### 3. Create a logout function

- In `views.py` add an import for `logout`. Then, create a new function called `logout_user` that deletes the cookie from the last login.

    ```
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    ```

- In `main.html`, add a logout button, and import `logout` and add the path in `urls.py`.

#### 4. Restricting access to the main page if the user is not logged in

- In `views.py`, import `login_required` and add `@login_required(login_url='/login')`  to restrict access to the main page if the user is not logged in. 

#### 5. Connect the `Product` model to the `user` Model.

- In `models.py`, import user and add this code in the `Product` class so that each product belongs to a specific user.

    ```
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ```

- Modify the `create_product` function so that it sets the `user` field to the `User` associated with the currently logged-in user:
    
    ```
    def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    ```

- Modify the `show_main` function:
    ```
    def show_main(request):
        products = Product.objects.filter(user=request.user)
    ```

- Also, modify ``name`` into `'name': request.user.username` in `context`. Save all changes and run the migrations for the model. And make sure you create an account if you havent already.

#### 6. Create an Increment, Decrement, and Delete Button

    ```
    if request.method == 'POST':
        if 'increment' in request.POST:
            product_id = request.POST.get('increment')
            product = products.get(id=product_id)
            product.amount += 1
            product.save()
            return HttpResponseRedirect(reverse('main:show_main'))
        elif 'decrement' in request.POST:
            product_id = request.POST.get('decrement')
            product= products.get(id=product_id)
            product.amount -= 1
            product.save()
            return HttpResponseRedirect(reverse('main:show_main'))
        elif 'delete' in request.POST:
            product_id = request.POST.get('delete')
            product = products.get(id=product_id)
            product.delete()
            return HttpResponseRedirect(reverse('main:show_main'))
    ```

- In `main.html` Create a button to increment, decrement, and delete an item. It first checks if the key `increment`, `decrement`, and `delete` is present in the POST request. 

- If `increment` is in the POST request, it retrieves the `product_id` from the POST data, fetches the corresponding product from the database based on the ID, increments the `amount` attribute of the product by 1, saves the product to update the database, and then redirects the user to a specific URL using HttpResponseRedirect.

- If `decrement` is in the POST request, it follows a similar process to handle product decrement. It retrieves the `product_id`, fetches the corresponding product, decrements the `amount` attribute by 1, saves the product, and redirects the user.

- If `delete` is in the POST request, it retrieves the `product_id`, fetches the corresponding product, deletes the product from the database, and redirects the user.

## `UserCreationForm` in Django

Django `UserCreationForm` is used for creating a new user that can use our web application. The advantage is that is simplifies user registration. UserCreationForm simplifies the process of creating a user registration form. It provides a ready-to-use form class, saving developers time and effort in creating a registration form from scratch. And it is

## Differences between authorization and authentication

Authentication is the process of verifying the identity of a user, ensuring that the user is who they claim to be. In a Django application, authentication involves mechanisms such as username and password validation, token-based authentication, social login, etc. It is the initial step where a user provides credentials (e.g., username and password) to gain access to the system. Successful authentication grants the user an identity within the system, which is then used for further interactions.

Authorization, on the other hand, is the process of determining what actions or resources a user is allowed to access or perform within the application. It defines permissions and restrictions on what authenticated users can do. In a Django application, authorization is often implemented using roles, groups, or permissions.

## Cookies and how Django use cookies

Cookies are small pieces of data that a website can store on a user's browser. They are typically used to track and manage user sessions, remember user preferences, and provide a personalized browsing experience.

In Django, the framework provides built-in support for handling sessions using cookies. Django uses a middleware component called the "session middleware" to manage user sessions. This middleware is responsible for setting and reading the session cookie in each HTTP request. When a user logs in or a session is created for any reason, Django sets a session cookie in the user's browser. This cookie contains a session ID, which is a unique identifier for the session.

## Are cookies safe? Is there any potential risks?

Cookies are a fundamental component of web applications and play a crucial role in enabling various functionalities and enhancing user experience. However, they do present certain security and privacy risks that developers and users should be aware of. 

Attackers can modify cookies (cookie tampering) to manipulate application behavior or gain unauthorized access to certain features or information. If an attacker gains access to a user's session cookie (e.g., through theft, interception), they can impersonate the user by using that cookie to authenticate themselves to the web application. This is known as session hijacking.

## Information of the logged-in user
![Display1](https://cdn.discordapp.com/attachments/1153252018023043093/1156378038326542427/image.png?ex=6514c078&is=65136ef8&hm=ab14945ad1dc7b522ac9e34286f8701ae2439efcb5b051ac0b0154e1d1e19450&)

![Display2](https://cdn.discordapp.com/attachments/1153252018023043093/1156379153931702302/image.png?ex=6514c182&is=65137002&hm=ebde3a266343fa8d8bf4e35ab739bffaa7e033134d6c7d02cc787c3ee11acbbd&)

</details>

<details>
<summary> Assignment 5 </summary>

# Assignment 5

## CSS Element Selectors and Usage

- Class Selector (.classname): Used to apply styles to HTML elements with a specific class attribute. It's versatile and commonly used for styling multiple elements.
- ID Selector (#id): Targets a unique HTML element based on its ID attribute. Typically, it's used when you need to style a specific element uniquely.
- Element Selector (elementname): Targets all instances of a specific HTML element. It's useful when you want to style a particular HTML element across your webpage.

## HTML5 Tags

- `<header>`: Represents a group of introductory or navigational aids, often containing logos, headings, navigation menus, etc.

- `<nav>`: Defines a set of navigation links within the document.

- `<section>`: Represents a thematic grouping of content, typically with a heading.

- `<article>`: Represents an independent piece of content within a document.

- `<aside>`: Defines content related to the main content, such as sidebars.

- `<footer>`: Represents a footer for a document or a section, often containing authorship information, copyright, links to related documents, etc.

## Differences Between Margin and Padding

**Margin** is the space outside the border of an element. Margins create space between the element's border and surrounding elements.**Padding** is the space between the element's content and its border. Padding adds space within the element, separating its content from the border.

## Differences Between Tailwind and Bootstrap

Tailwind is focused on providing low-level utility classes that you can combine to build custom designs efficiently. And it is Highly customizable, allowing for configuration of styles and the generation of a tailored build to reduce unused styles. 

Meanwhile Bootstrap provides pre-designed, styled components that you can use directly, which can speed up development.  It offers a wide range of pre-built components and responsive grid system, making it easy to create complex layouts.

 - When to use Bootstrap :
 When you need a robust set of pre-designed components. And If you're a beginner or prefer a more guided, component-focused approach.
 Projects where customization isn't a top priority.

 - When to use Tailwind :
 When you want a highly customizable design system and have CSS knowledge. And If you prefer a utility-first approach and enjoy creating custom designs. Projects where optimization and reduction of unused styles are important.

 ## Step by step

 - Customize `main.html`

 ```
 {% extends 'base.html' %}

{% block content %}
<style>
    body {
        background-color: #212529;
        color: #ffffff;
    }

    .highlighted-item {
        background-color: #FFD700; /* Yellow background color */
        color: #000000; /* Black text color */
    }

    .container {
        padding: 20px;
    }

    th, td {
        padding: 10px;
        border: 1px solid #ffffff;
    }

    th {
        background-color: #343a40;
    }

    table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 20px;
    }

    table tr:nth-child(even) {
        background-color: #454d55;
    }

     
     .modal-content {
        background-color: #000;
        color: #fff;
    }

    .modal-header {
        border-bottom: 1px solid #343a40;
    }

</style>

<nav class="navbar navbar-dark bg-dark border-bottom">
    <div class="container">
        <a class="navbar-brand" href="#">B-Inventory | Welcome {{ name }}!</a>
        <form class="d-flex">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
    </div>
</nav>

<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Product</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form id="form" onsubmit="return false;">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label for="name" class="col-form-label">Name:</label>
                        <input type="text" class="form-control" id="name" name="name">
                    </div>
                    <div class="mb-3">
                        <label for="amount" class="col-form-label">Amount:</label>
                        <input type="number" class="form-control" id="amount" name="amount">
                    </div>
                    <div class="mb-3">
                        <label for="price" class="col-form-label">Price:</label>
                        <input type="number" class="form-control" id="price" name="price">
                    </div>
                    <div class="mb-3">
                        <label for="description" class="col-form-label">Description:</label>
                        <textarea class="form-control" id="description" name="description"></textarea>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Product</button>
            </div>
        </div>
    </div>
</div>

<div class="container mt-4 text-light">
    <h1>B-Inventory</h1>

    <div class="mb-3">
        <p>You have added {{ product_count }} Items in the inventory!</p>
    </div>

    <table id="product_table"></table>

    <br />

    <h5>Last login session: {{ last_login }}</h5>

    <a href="{% url 'main:logout' %}" class="btn btn-danger">Logout</a>

    <a href="{% url 'main:create_product' %}" class="btn btn-primary">Add New Item</a>

</div>
 ```

 - Customize `register.html`
 ```
 {% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}

<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">
                    <h1>Register</h1>
                </div>
                <div class="card-body">
                    <form method="POST">
                        {% csrf_token %}
                        {{ form.as_p }}
                        <div class="text-center">
                            <button type="submit" class="btn btn-primary">Register</button>
                        </div>
                    </form>

                    {% if messages %}
                        <ul class="mt-3">
                            {% for message in messages %}
                                <li>{{ message }}</li>
                            {% endfor %}
                        </ul>
                    {% endif %}
                </div>
            </div>
        </div>
    </div>
</div>

{% endblock content %}

 ```

 - Customize `login.html`

 ```
 {% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}
<style>
    body {
        background-color: #333; /* Dark gray color */
        color: #fff; /* Text color set to white */
        padding: 50px;
    }
    .container {
        max-width: 400px;
        margin: 0 auto;
    }
    .card {
        background-color: #444; /* Darker gray for the card */
        border: 1px solid #555;
        border-radius: 10px;
    }
    .card-header {
        background-color: #333; /* Adjusted to match body background */
        padding: 20px;
        border-bottom: 1px solid #555;
        color: #fff; /* Text color set to white */
    }
    .card-body {
        padding: 20px;
    }
    .form-group input {
        width: 100%;
        padding: 10px;
        margin-bottom: 10px;
        border: 1px solid #555;
        border-radius: 5px;
    }
    .btn {
        width: 100%;
        padding: 10px;
    }
</style>

<div class="container">
    <div class="card">
        <div class="card-header">
            <h1>Login</h1>
        </div>
        <div class="card-body">
            <form method="POST" action="">
                {% csrf_token %}
                <div class="form-group">
                    <label for="username" style="color: #fff;">Username:</label>
                    <input type="text" name="username" id="username" placeholder="Username" class="form-control">
                </div>
                <div class="form-group">
                    <label for="password" style="color: #fff;">Password:</label>
                    <input type="password" name="password" id="password" placeholder="Password" class="form-control">
                </div>
                <button type="submit" class="btn btn-primary">Login</button>
            </form>

            {% if messages %}
                <ul style="color: #fff;">
                    {% for message in messages %}
                        <li>{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}

            <p style="color: #fff;">Don't have an account yet? <a href="{% url 'main:register' %}" style="color: #fff;">Register Now</a></p>
        </div>
    </div>
</div>

{% endblock content %}

 ```

 - Customize `create_product.html`
 ```
 {% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}
<style>
    body {
        background-color: #333; /* Dark gray color */
        color: #fff; /* Text color set to white */
        padding: 50px;
    }
    .container {
        max-width: 400px;
        margin: 0 auto;
    }
    .card {
        background-color: #444; /* Darker gray for the card */
        border: 1px solid #555;
        border-radius: 10px;
    }
    .card-header {
        background-color: #333; /* Adjusted to match body background */
        padding: 20px;
        border-bottom: 1px solid #555;
        color: #fff; /* Text color set to white */
    }
    .card-body {
        padding: 20px;
    }
    .form-group input {
        width: 100%;
        padding: 10px;
        margin-bottom: 10px;
        border: 1px solid #555;
        border-radius: 5px;
    }
    .btn {
        width: 100%;
        padding: 10px;
    }
</style>

<div class="container">
    <div class="card">
        <div class="card-header">
            <h1>Login</h1>
        </div>
        <div class="card-body">
            <form method="POST" action="">
                {% csrf_token %}
                <div class="form-group">
                    <label for="username" style="color: #fff;">Username:</label>
                    <input type="text" name="username" id="username" placeholder="Username" class="form-control">
                </div>
                <div class="form-group">
                    <label for="password" style="color: #fff;">Password:</label>
                    <input type="password" name="password" id="password" placeholder="Password" class="form-control">
                </div>
                <button type="submit" class="btn btn-primary">Login</button>
            </form>

            {% if messages %}
                <ul style="color: #fff;">
                    {% for message in messages %}
                        <li>{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}

            <p style="color: #fff;">Don't have an account yet? <a href="{% url 'main:register' %}" style="color: #fff;">Register Now</a></p>
        </div>
    </div>
</div>

{% endblock content %}

 ```
 
 - Customize `edit_product.html`
 ```
 {% extends 'base.html' %}

{% load static %}

{% block content %}

<div class="container bg-light p-4">
    <h1 class="mt-4">Edit Product</h1>

    <form method="POST">
        {% csrf_token %}
        <div class="form-group">
            {{ form.as_p }}
        </div>
        <button type="submit" class="btn btn-primary">Edit Product</button>
    </form>
</div>

{% endblock %}

 ```
 </details>

 <details>

 # Assignment 6

 ## Differences between asynchronous programming and synchronous programming

 In synchronous programming, tasks are executed one after the other in a sequential manner. Each task must complete before the program moves on to the next task. If a task takes a long time to complete, the entire program is blocked or "waits" for that task to finish. This can lead to inefficiencies, especially when dealing with I/O operations or tasks that involve waiting for external events. 

 In asynchronous programming, tasks are started but not necessarily completed immediately. The program doesn't wait for a task to finish before moving on to the next one. Instead, it can execute other tasks or continue with other operations while the initial tasks are being processed in the background. Callbacks or promises are often used to handle the eventual results of these asynchronous tasks.

 ## Event-Driven Programming Paradigm

 Event-driven programming paradigm is a programming paradigm where the flow of a program is determined by events that occur during its execution. One of the implementation in this assignment is when we try to add new item and update the display of books without refreshing the page. in code document.getElementById("button_add").onclick = addProduct;, document.getElementById("button_add")try to get the ID button_add, which is the button inside the form. .onclick is an event handler that specifies what should happen when the button is clicked. addProduct is a JavaScript function defined earlier in the code that is responsible for making an asynchronous request to add a new book to the collection and refreshing the display of books.

 ## Implementation of asynchronous programming in AJAX

 Asynchronous programming in AJAX allows web applications to make HTTP requests to a server and receive data without blocking the main execution thread of the browser. This enables web pages to remain responsive and update their content dynamically without requiring full page reloads.

 ## The implementation of AJAX is done using the Fetch API rather than the jQuery library. Compare the two technologies and write down your opinion which technology is better to use

 The Fetch API is a modern standard and is built into the browser, making it a part of the JavaScript language itself. It's a part of the Web API standard and is designed to be consistent, intuitive, and compatible with modern development practices. jQuery AJAX provides an abstraction over XMLHttpRequest, offering better cross-browser compatibility, especially for older browsers.

 If you're working on a modern web application and prefer to use the latest web standards, the Fetch API is the recommended choice. It aligns well with modern JavaScript practices and is a part of the standard web platform.
 In summary, the Fetch API is generally preferred for its modern standards, simplicity, and alignment with modern JavaScript practices, while jQuery AJAX might still be useful in certain situations where cross-browser compatibility and a simplified syntax are essential.

## Step By Step Explanation

1. Create a new function inside `views.py` called `get_product_json` to return data as JSON

```
def get_product_json(request):
product_item = Item.objects.filter(user=request.user)
return HttpResponse(serializers.serialize('json', product_item))
```

Then, create the routing in `urls.py`

2. Create New Function inside `views.py` to Add Product using AJAX

First we import from `django.views.decorators.csrf` import csrf_exempt in views.py, then we create new function add_product_ajax:

```
@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        amount = request.POST.get("amount")
        user = request.user

        new_product = Product(name=name, amount=amount, price=price, description=description, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```

create the routing in `urls.py`

4. Show the Product using fetch API

Delete the existing div to show the data and replace it with . Then put <script> tag block at the bottom of the code( before {% endblock content %}) and create a async function:

```
async function getProducts() {
    return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
}
```

Still inside the <scripts> tag block called refreshProduct() we create new async function to show the item and refresh the items data asynchronously as following :

```
async function refreshProducts() {
        document.getElementById("product_table").innerHTML = ""
        const products = await getProducts()
        let htmlString = `<tr>
            <th>Name</th>
            <th>amount</th>
            <th>Price</th>
            <th>Description</th>
            <th>Date Added</th>
        </tr>`
        products.forEach((item) => {
            htmlString += `\n<tr>
            <td>${item.fields.name}</td>
            <td>${item.fields.amount}</td>
            <td>${item.fields.price}</td>
            <td>${item.fields.description}</td>
            <td>${item.fields.date_added}</td>
        </tr>` 
        })
        
        document.getElementById("product_table").innerHTML = htmlString
    }

    refreshProducts()


```

6. Create a JS Function to add a product

inside the <script> tag block we add a function to add an item using AJAX like the following:

```
function addProduct() {
        fetch("{% url 'main:add_product_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        }).then(refreshProducts);

        document.getElementById("form").reset();
        return false;
```

Then we set the addProduct() function as as the onclick function of the modal's "Add Book" button:

```
document.getElementById("button_add").onclick = addProduct
```

</details>
