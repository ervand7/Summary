## API for internet-shop
`Stack: Python, Django, DRF, PostgreSQL, Pytest`
### [Описание проекта на русском языке](https://github.com/ervand7/Project-shop#1-приложение) | [Project description in English](https://github.com/ervand7/Project-shop#1-application)



#### 1) Приложение
С помощью Django разработан backend приложения для интернет-магазина. В приложении есть такие сущности, как:
* продукты
* отзывы
* заказы
* коллекции продуктов
* пользователи
* администраторы

Для разработки приложения были прописаны следующие ограничения:

| Models | Permissions | Felter requirements | 
| --- | --- | --- |
| Product: /api/v1/products/ | Только администраторы могут создавать продукты. Пользователи могут видеть все продукты. | Возможность фильтровать по: цене, содержимому из названия, содержимому из описания.
| ProductReviews: /api/v1/product-reviews/ | Только авторизованные пользователи могут оставлять отзывы о продуктах. Один пользователь может оставить только один отзыв на конкретный продукт. Пользователь может обновлять, удалять только собственные отзывы. | Возможность фильтровать отзывы по: ID пользователя, ID продукта, дате создания.
| Orders: /api/v1/orders/ | Только авторизованные пользователи могут создавать заказы. Пользователи могут видеть только свои заказы. Администраторы могут видеть все заказы. Только администраторы могут изменить статус заказа. | Возможность фильтровать заказы по: статусу, итоговой сумме, дате создания, дате обновления, продуктам из заказа.
| ProductCollections: /api/v1/product-collections/ | Только администраторы могут создавать подборки. Все пользователи могут видеть подборки.

Доступные действия для всех моделей: `retrieve, list, create, update, destroy `

#### 2) Тесты
К проекту написано (с учетом параметризаций) более 60 тестов, которые покрывают все эндпоинты приложения. В основном они валидируют различие поведений: 
* авторизованного/неавторизованного пользователя
* пользователя/администратора

#### 3) Интерфейс администратора
Интерфейс администратора создан стандартными средствами Django admin. В GUI можно:

* редактировать и просматривать подбороки
* осуществлять просмотр списка заказов пользователей, отсортированных по дате создания
* редактировать и просматривать товары
* редактировать и просматривать отзывы
* редактировать и просматривать страницу детализации заказа с просмотром списка заказанных товаров

#### 4) База данных
В качестве СУБД использован Postgresql.

База данных представлена следующей схемой:
![Bootstrap logo](https://github.com/ervand7/Project-shop/blob/master/project_shop/DB_schema.jpg?raw=true)

### Инструкция к запуску проекта:

1. Убедитесь, что у вас установлены следующие программы:
   * git, версия не ниже 2.18.0
   * Python, версия не ниже 3.8.5
   * postgres, версия не ниже 13.2
2. Склонируйте себе этот репозиторий по HTTPS:
   
   `$ git clone https://github.com/ervand7/Project-shop.git`
   
3. Откройте склонированную папку в вашем IDE . Создайте виртуальное окружение в корне склонированной папки.

    `$ python3 -m venv venv`
   
    `$ source venv/bin/activate`

    Настройте IDE таким образом, чтобы текущим Python интерпретатором был venv/bin/python. 
   
   Далее установите зависимости:

    `$ pip install -r requirements.txt`
4. Настройте базу данных:
   
   `$ psql`

   `create user super_super with password 'super_super';`

   `create database ervand_shop_project with owner super_super;`

   `\q`

   далее перейдите в файл Project-shop/project_shop/project_shop/settings.py и присвойте переменной DATABASES следующее значение:
   
   ```html
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'ervand_shop_project',
           'USER': 'super_super',
           'PASSWORD': 'super_super',
           'HOST': '127.0.0.1',
           'PORT': '5432',
       }
   }
   ````
   
5. Запустите команды для старта проекта:

    `$ python manage.py migrate`
   
    `$ python manage.py loaddata fixtures.json`

    `$ python manage.py runserver 8000`
   
6. Откройте папку "http_requests" в которой находятся файлы с http-запросами. Для исполнения этих запросов вы можете использовать следующие программы: curl, postman, HTTP Toolkit, PyCharm Professional.

### Инструкция к запуску тестов:

1. Перейдите в файл Project-shop/project_shop/project_shop/settings.py и присвойте переменной DATABASES следующее значение:
   ```html
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'ervand_shop_project',
           # 'USER': 'super_super',
           # 'PASSWORD': 'super_super',
           # 'HOST': '127.0.0.1',
           # 'PORT': '5432',
       }
   }
   ````

2. Настройте вашу IDE таким образом, чтобы активным тест раннером был pytest.

3. Запустите тесты с помощью фреймворка pytest. Если вы хотите использовать дебаг в тестах, то рекомендуется использовать параметр `-s` для корректного исполнения потока.
4. для проверки покрытия проекта тестами введите в терминале комманду:

   `pytest --cov-report=html --cov=app`

---
---

#### 1) Application

A backend of application for an online store has been developed using Django. The application has such entities as:
* products
* reviews
* orders
* product collections
* users
* administrators

For the development of the application, the following restrictions were prescribed:

| Models | Permissions | Felter requirements | 
| --- | --- | --- |
| Product: /api/v1/products/ | Only admins can create products. All users can watch. | The ability to filter products by: price, content from the title, content from the description.
| ProductReviews: /api/v1/product-reviews/ | Only authorized users can leave a review about the product. One user cannot leave more than one review for the same product. The user can update and delete only his own review. | The ability to filter review by: user ID, product ID, creation date.
| Orders: /api/v1/orders/ | Only authorized users can create orders. Users can only see their orders. Admins can see all orders. Only admins can change order status. | The ability to filter orders by: status, the total amount, creation date, update date, products from positions.
| ProductCollections: /api/v1/product-collections/ | Only admins can create collections. All other users can only watch collections.

Available actions for all models: `retrieve, list, create, update, destroy `

#### 2) Tests
More than 60 tests have been written for the project (taking into account parameterizations), which cover all endpoints of the application. They basically validate a difference in behavior:
* authorized / unauthorized user
* user / administrator

#### 3) Admin interface
The admin interface is created using standard Django admin tools. In the GUI, you can:

* edit and view selections
* view a list of user orders sorted by creation date
* edit and view products
* edit and view reviews
* edit and view the order detail page with viewing the list of ordered products

#### 4) Data base
Postgresql is used as a DBMS.

DB schema is:
![Bootstrap logo](https://github.com/ervand7/Project-shop/blob/master/project_shop/DB_schema.jpg?raw=true)

### Instructions for launching the project:

1. Make sure you have the following programs installed:
   * git, version 2.18.0 or higher
   * Python, version 3.8.5 or later
   * postgres, version 13.2 or later
2. Clone this repository to yourself over HTTPS:
   
   `$ git clone https://github.com/ervand7/Project-shop.git`

3. Open the cloned folder in your IDE. Create a virtual environment in the root of the cloned folder.

    `$ python3 -m venv venv`
   
    `$ source venv/bin/activate`

Configure the IDE so that the current Python interpreter is venv / bin / python.
   
   Next, install the dependencies:

    `$ pip install -r requirements.txt`
4. Set up the database:
   
   `$ psql`

   `create user super_super with password 'super_super';`

   `create database ervand_shop_project with owner super_super;`

   `\q`

then go to the Project-shop / project_shop / project_shop / settings.py file and assign the following value to the DATABASES variable:
   
   ```html
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'ervand_shop_project',
           'USER': 'super_super',
           'PASSWORD': 'super_super',
           'HOST': '127.0.0.1',
           'PORT': '5432',
       }
   }
   ````
      
5. Run the commands to start the project:

    `$ python manage.py migrate`
   
    `$ python manage.py loaddata fixtures.json`

    `$ python manage.py runserver 8000`
   
6. Open the "http_requests" folder, which contains the files with http requests. You can use the following programs to execute these requests: curl, postman, HTTP Toolkit, PyCharm Professional.

### Instructions for running tests:

1. Go to the Project-shop / project_shop / project_shop / settings.py file and assign the following value to the DATABASES variable:
   ```html
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'ervand_shop_project',
           # 'USER': 'super_super',
           # 'PASSWORD': 'super_super',
           # 'HOST': '127.0.0.1',
           # 'PORT': '5432',
       }
   }
   ````

2. Configure your IDE so that pytest is the active test runner.

3. Run the tests using the pytest framework. If you want to use debugging in tests, it is recommended to use the `-s` parameter for correct execution of the stream.
4. To check the coverage of the project with tests, enter the command in the terminal:

   `pytest --cov-report=html --cov=app`
