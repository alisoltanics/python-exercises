A metaclass in Python is a class of a class that defines how a class behaves. 


First watch this: https://www.youtube.com/watch?v=NAQEj-c2CI8




The main use case for a metaclass is creating an API. A typical example of this is the Django ORM. It allows you to define something like this:

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

But if you do this:

person = Person(name='bob', age='35')
print(person.age)
It won't return an IntegerField object. It will return an int, and can even take it directly from the database.

This is possible because models.Model defines __metaclass__ and it uses some magic that will turn the Person you just defined with simple statements into a complex hook to a database field.

#########################################################################################################################################################
The type class is even the metaclass for the built-in object class, which is the base class for all the classes in Python. As type itself is a class, what is the metaclass of the type class? The type class is a metaclass of itself!
#########################################################################################################################################################

#https://stackoverflow.com/a/6581949/6173668
