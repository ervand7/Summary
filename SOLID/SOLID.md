Материал составлени из статей следующих авторов:

https://gist.github.com/pavel-loginov-dev

https://github.com/heykarimoff
# S.O.L.I.D принципы с примерами на Python

<details>
<summary>Примечания</summary>

* Под клиентами подразумеваются программные сущности, использующие другие программные сущности.

* Этот файл является переводом статьи с сайта medium.com пользователя DeeKey, ссылка в завершении файла.
</details>


SOLID — это мнемоническая аббревиатура для набора принципов проектирования, созданных для разработки программного обеспечения при помощи объектно-ориентированных языков. Принципы **SOLID** направленны на содействие разработки более простого, надежного и обновляемого кода. Каждая буква в аббревиатуре **SOLID** соответствует одному принципу разработки.

При правильной реализации это делает ваш код более **расширяемым, логичным и легким для чтения**.



Для понимания **SOLID** принципов, вы должны хорошо понимать как, используются интерфейсы.

Я попытаюсь объяснить принципы **SOLID** на примере Python в как можно более простой форме, чтобы даже новички смогли разобраться. Чтобы было очень легко взять представленные примеры и применить их на Python.



Рассмотрим каждый принцип один за другим:

## 1. Single Responsibility Principle<br>  (Принцип единственной обязанности)

Принцип единственной обязанности требует того, чтобы **один класс выполнял только одну работу**. Таким образом, если у класса есть более одной работы, он становится зависимым. Изменение поведения одной работы класса приводит к изменению в другой.

```python
# Below is Given a class which has two responsibilities 
class  User:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    def save(self, user: User):
        pass
```

Мы имеем класс User, который ответственен за две работы — свойства пользователя и управление базой данных. Если в приложении будет изменен функционал управления базой данных для пользователя, тогда классы использующие свойства класса User тоже придется доработать и перекомпилировать, чтобы компенсировать новые изменения. Это как домино эффект, уроните одну кость, и она уронит все за ней следом.

Мы же просто разделим класс. Мы создадим ещё один класс, который возьмет на себя одну ответственность — управление базой данных пользователя.

```python
class User:
    def __init__(self, name: str):
            self.name = name
    
    def get_name(self):
        pass


class UserDB:
    def get_user(self, id) -> User:
        pass

    def save(self, user: User):
        pass
```

Распространённым решением этой проблемы является применение шаблона проектирования Фасад. Ознакомиться с паттерном Фасад вы можете [здесь](https://medium.com/@andreaspoyias/design-patterns-a-quick-guide-to-facade-pattern-16e3d2f1bfb6). User класс был бы фасадом для управления базой данных пользователя и управления свойствами пользователя.



## 2. Open-Closed Principle <br> (Принцип открытости/закрытости)

Программные сущности (**классы, модули, функции**) должны быть **открыты для расширения, но не модификации**.

Давайте представим, что у вас есть магазин, и вы даете скидку в 20% для ваших любимых покупателей используя класс Discount. Если бы вы решаете удвоить 20-ти процентную скидку для VIP клиентов, вы могли бы изменить класс следующим образом:

```python
class Discount:
  def __init__(self, customer, price):
      self.customer = customer
      self.price = price
  def give_discount(self):
      if self.customer == 'fav':
          return self.price * 0.2
      if self.customer == 'vip':
          return self.price * 0.4
```

Но нет, это нарушает OCP. OCP запрещает это. Например, если мы хотим дать новую скидку для другого типа покупателей, то это требует добавления новой логики. Чтобы следовать OCP, мы добавим новый класс, который будет расширять Discount. И в этом новом классе реализуем требуемую логику:

```python
class Discount:
    def __init__(self, customer, price):
      self.customer = customer
      self.price = price
    def get_discount(self):
      return self.price * 0.2

class VIPDiscount(Discount):
    def get_discount(self):
      return super().get_discount() * 2
```

Если вы решите дать скидку супер VIP пользователям, то это будет выглядеть так:

```python
class SuperVIPDiscount(VIPDiscount):
    def get_discount(self):
      return super().get_discount() * 2
```

Расширяйте, но не модифицируйте.



## 3. Liskov Substitution Principle<br> (Принцип подстановки Лисков)

Главная идея, стоящая за Liskov Substitution Principle в том, что **для любого класса клиент должен иметь возможность использовать любой подкласс базового класса, не замечая разницы между ними**, и следовательно, без каких-либо изменений поведения программы при выполнении. Это означает, что клиент полностью изолирован и не подозревает об изменениях в иерархии классов.

*Более формально:
Пусть **q(x)** является свойством, верным относительно объектов **x** некоторого типа **T**. Тогда **q(y)** также должно быть верным для объектов **y** типа **S**, где **S** является подтипом типа **T**.*

Проще говоря, это значит, что подкласс, дочерний класс должны соответствовать их родительскому классу или супер классу.

```python
"""
Liskov Substitution Principle

A sub-class must be substitutable for its super-class.  The aim of this
principle is to ascertain that a sub-class can assume the place of its
super-class without errors.  If the code finds itself checking the type of class
then, it must have violated this principle.

Let’s use our Animal example.
"""

def animal_leg_count(animals: list):
    for animal in animals:
        if isinstance(animal, Lion):
            print(lion_leg_count(animal))
        elif isinstance(animal, Mouse):
            print(mouse_leg_count(animal))
        elif isinstance(animal, Pigeon):
            print(pigeon_leg_count(animal))
        
animal_leg_count(animals)

"""
To make this function follow the LSP principle, we will follow this LSP
requirements postulated by Steve Fenton:

If the super-class (Animal) has a method that accepts a super-class type
(Animal) parameter.  Its sub-class(Pigeon) should accept as argument a
super-class type (Animal type) or sub-class type(Pigeon type).  If the
super-class returns a super-class type (Animal).  Its sub-class should return a
super-class type (Animal type) or sub-class type(Pigeon).  Now, we can
re-implement animal_leg_count function:
"""

def animal_leg_count(animals: list):
    for animal in animals:
        print(animal.leg_count())
        
animal_leg_count(animals)

"""
The animal_leg_count function cares less the type of Animal passed, it just
calls the leg_count method.  All it knows is that the parameter must be of an
Animal type, either the Animal class or its sub-class.

The Animal class now have to implement/define a leg_count method.  And its
sub-classes have to implement the leg_count method:
"""

class Animal:
    def leg_count(self):
        pass


class Lion(Animal):
    def leg_count(self):
        pass


"""
When it’s passed to the animal_leg_count function, it returns the number of legs
a lion has.

You see, the animal_leg_count doesn’t need to know the type of Animal to return
its leg count, it just calls the leg_count method of the Animal type because by
contract a sub-class of Animal class must implement the leg_count function.
"""
```


LSP это основа хорошего объектно-ориентированного проектирования программного обеспечения, потому что он следует одному из базовых принципов ООП — полиморфизму. Речь о том, чтобы создавать правильные иерархии, такие, что классы, производные от базового являлись полиморфными для их родителя по отношению к методам их интерфейсов. Ещё интересно отметить, как этот принцип относится к примеру предыдущего принципа. Если мы пытаемся расширить класс новым несовместимым классом, то все сломается. Взаимодействие с клиентом будет нарушено, и как результат, такое расширение будет невозможно (или, для того чтобы сделать это возможным, нам пришлось бы нарушить другой принцип и модифицировать код клиента, который должен быть закрыт для модификации, такое крайне нежелательно и неприемлемо).

Тщательное обдумывание новых классов в соответствии с LSP помогает нам расширять иерархию классов правильно. Также, LSP способствует OCP.



# 4. Interface Segregation Principle<br> (Принцип разделения интерфейсов)

Создавайте тонкие интерфейсы, которые ориентированы на клиента. **Клиенты не должны зависеть от интерфейсов, которые они не используют**. Этот принцип устраняет недостатки реализации больших интерфейсов.

Чтобы полностью проиллюстрировать это, мы возьмем классический пример, потому что он очень показательный и легок для понимания. Классический пример:

```python
class IShape:
    def draw(self):
        raise NotImplementedError

class Circle(IShape):
    def draw(self):
        pass

class Square(IShape):
    def draw(self):
        pass

class Rectangle(IShape):
    def draw(self):
        pass
```

Еще один приятный трюк заключается в том, что в нашей бизнес-логике отдельный класс может реализовать несколько интерфейсов, если необходимо. Таким образом, мы можем предоставить единую реализацию для всех общих методов между интерфейсами. Сегрегированные интерфейсы заставляют нас больше думать о нашем коде с точки зрения клиента, что приведет нас к меньшей зависимости и более легкому тестированию. Таким образом, мы не только сделали наш код лучше для клиента, но также это облегчило нам понимание, тестирование и реализацию кода для нас самих.



## 5. Dependecy Inversion Principle<br>  (Принцип инверсии зависимостей)

**Зависимость должна быть от абстракций, а не от конкретики**. Модули верхних уровней не должны зависеть от модулей нижних уровней. Классы и верхних, и нижних уровней должны зависеть от одних и тех же абстракций. Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций.

Наступает момент в разработке, когда наше приложение в основном состоит из модулей. Когда такое происходит, нам необходимо улучшать код используя внедрение зависимостей. Функционирование компонентов высокого уровня зависит от компонентов низкого уровня. Для создания определенного поведения вы можете использовать наследование или интерфейсы.

```python
class AuthenticationForUser():
  def __init__(self, connector:Connector):
		self.connection = connector.connect()
	
	def authenticate(self, credentials):
		pass
	def is_authenticated(self):
		pass	
	def last_login(self):
		pass

class AnonymousAuth(AuthenticationForUser):
	pass

class GithubAuth(AuthenticationForUser):
	def last_login(self):
		pass

class FacebookAuth(AuthenticationForUser):
	pass

class Permissions()
	def __init__(self, auth: AuthenticationForUser)
		self.auth = auth
		
	def has_permissions():
		pass
		
class IsLoggedInPermissions (Permissions):
	def last_login():
		return auth.last_log
```



Больше можно прочитать:

* [Solid Python](https://www.researchgate.net/publication/323935872_SOLID_Python_SOLID_principles_applied_to_a_dynamic_programming_language)
* [Clean Code](https://www.amazon.com/Clean-Code-Python-Refactor-legacy/dp/1788835832)



### Источники:

1. [S.O.L.I.D Principles explained in Python with examples](https://levelup.gitconnected.com/s-o-l-i-d-principles-explained-in-python-with-examples-83b2b43bdcde)
2. [Принципы SOLID](https://metanit.com/sharp/patterns/5.1.php)
3. [Принцип подстановки Барбары Лисков](https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF_%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B8_%D0%91%D0%B0%D1%80%D0%B1%D0%B0%D1%80%D1%8B_%D0%9B%D0%B8%D1%81%D0%BA%D0%BE%D0%B2)
4. [Принцип разделения интерфейса](https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF_%D1%80%D0%B0%D0%B7%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F_%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%D0%B0)
5. [Принцип инверсии зависимостей](https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF_%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%B8_%D0%B7%D0%B0%D0%B2%D0%B8%D1%81%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D0%B5%D0%B9)


