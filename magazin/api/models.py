from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TovarGroup(models.Model):
    title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Tovar(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    count = models.IntegerField()
    tovargroup = models.ForeignKey(TovarGroup, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Customer(models.Model):
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.fullname


class Seller(models.Model):
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.fullname


class Sale(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    tovar = models.ForeignKey(Tovar, on_delete=models.PROTECT)
    finalprice = models.FloatField()
    date = models.DateField()
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.tovar} + {self.customer}"
