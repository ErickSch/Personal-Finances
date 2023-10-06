from django.db import models

# Create your models here.
    
class ExpenseType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

class Expense(models.Model):
    cost = models.FloatField()
    type = models.ForeignKey(ExpenseType, on_delete=models.CASCADE, blank=True)
    # date = models.DateField(auto_now_add=True)
    date = models.DateField()

    def __str__(self):
        return self.cost
    
class DailyExpense(models.Model):
    date = models.DateField()
    total = models.FloatField(default=0)

    def __str__(self):
        return self.date

