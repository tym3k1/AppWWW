# API zadądzania wydatkami
Tymoteusz Łuczko <3 Piotr Dondalski


class Budget(models.Model):
    month = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

class Expense(models.Model):
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

class SavingGoal(models.Model):
    name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField()

class SavingProgress(models.Model):
    saving_goal = models.ForeignKey(SavingGoal, on_delete=models.CASCADE)
    amount_saved = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
Budget przechowuje informacje o miesięcznym budżecie.
ExpenseCategory pozwala na definiowanie kategorii wydatków w ramach budżetu.
Expense przechowuje konkretne wydatki w określonej kategorii.
SavingGoal reprezentuje cele oszczędnościowe, które mają określony cel oszczędnościowy i termin.
SavingProgress śledzi postępy w osiąganiu celów oszczędnościowych w czasie.
