from django.shortcuts import render, redirect
from datetime import date, datetime
import requests
from currency_converter import CurrencyConverter
import locale
from django.db.models import Sum, Count
from .models import *
from .forms import *
from django.core.paginator import Paginator

# Create your views here.


def index(request):

    expense_types = ExpenseType.objects.all()
    expenses = Expense.objects.all()
    expense_type_form = ExpenseTypeForm()
    expense_form = ExpenseForm()
    daily_expenses = DailyExpense.objects.all()
    
    if request.method == 'POST':
        if "expense_type_form" in request.POST:
            form = ExpenseTypeForm(request.POST)

        else:
            form = ExpenseForm(request.POST)
            expense = form.save(commit=False)
            # if(not DailyExpense.objects.filter(date=expense.date):
            if(not DailyExpense.objects.filter(date=expense.date)):
                daily_expense = DailyExpense()
                daily_expense.total = expense.cost
                # daily_expense.date = date.today() 
                daily_expense.date = expense.date 
                daily_expense.save()
            else:
                # daily_expense = DailyExpense.objects.get(date=date.today())
                daily_expense = DailyExpense.objects.get(date=expense.date)
                daily_expense.total += expense.cost
                daily_expense.save()


        if form.is_valid:
            form = form.save()
            return redirect('index')

    
            

    context = {
        'expense_types' : expense_types,
        'expense_type_form' : expense_type_form,
        'expense_form' : expense_form,
        'expenses' : expenses,
        'daily_expenses' : daily_expenses


    }

    return render(request, 'Spendings/index.html', context)


def delete_expense(request, expense_id):
    expense = Expense.objects.get(id = expense_id)
    daily_expense = DailyExpense.objects.get(date=expense.date)
    daily_expense.total -= expense.cost
    daily_expense.save()

    expense.delete()

    return redirect('data')

def registry(request):
    expense_types = ExpenseType.objects.all()
    expenses = Expense.objects.all()
    expense_type_form = ExpenseTypeForm()
    instance_expense = Expense(date=date.today())
    expense_form = ExpenseForm(instance=instance_expense)
    todays_expenses = Expense.objects.filter(date=date.today())
    last_five_expenses = Expense.objects.all().order_by('-id')[:6]

    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        expense = form.save(commit=False)
        if(not DailyExpense.objects.filter(date=expense.date)):
            daily_expense = DailyExpense()
            daily_expense.total = expense.cost
            daily_expense.date = expense.date 
            daily_expense.save()
        else:
            daily_expense = DailyExpense.objects.get(date=expense.date)
            daily_expense.total += expense.cost
            daily_expense.save()

        if form.is_valid:
            form = form.save()
            return redirect('registry')


    context = {
        'expense_types' : expense_types,
        'expense_type_form' : expense_type_form,
        'expense_form' : expense_form,
        'expenses' : expenses,
        'todays_expenses' : todays_expenses,
        'last_five_expenses' : last_five_expenses,
    }

    return render(request, 'Spendings/registry.html', context)

def create_expense_type(request):
    expense_types = ExpenseType.objects.all()
    expense_type_form = ExpenseTypeForm()

    if request.method == 'POST':
        form = ExpenseTypeForm(request.POST)


        if form.is_valid:
            form = form.save()
            return redirect('create_expense_type')

    context = {
        'expense_types' : expense_types,
        'expense_type_form' : expense_type_form
    }

    return render(request, 'Spendings/create_expense_type.html', context)

def delete_expense_type(request, id_expense_type):
    expense_type = ExpenseType.objects.get(id = id_expense_type)
    expense_type.delete()

    return redirect('create_expense_type')

def statistics(request):
    expense_types = ExpenseType.objects.all()
    current_date = datetime.now()
    daily_expenses = DailyExpense.objects.all().order_by('-date')[:10]
    todays_expenses = Expense.objects.filter(date=date.today())
    
    # BTC Price
    btc_response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    btc_response_json = btc_response.json()
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    btc_usd = round(locale.atof(btc_response_json['bpi']['USD']['rate']), 2)  

    # USD Price
    c = CurrencyConverter()
    usd_mxn = round(c.convert(1, 'USD', 'MXN'), 2)

    

    expenses = Expense.objects.all()


    month_expenses = Expense.objects.filter(date__month = current_date.month)
    month_total = Expense.objects.filter(date__month=current_date.month).aggregate(total_cost=Sum('cost')) if Expense.objects.filter(date__month=current_date.month) else 0.0
    rounded_month_total = round(month_total['total_cost'], 2) if month_total else 0
    month_expenses_per_type_data = Expense.objects.filter(date__month=current_date.month).values('type').order_by('type').annotate(Total=Sum('cost'))

    avg_cost_per_day = round(rounded_month_total/current_date.day, 2)
    exp_month_total = avg_cost_per_day*30
    extra_to_spend = round(6000-exp_month_total, 2)
    if(extra_to_spend < 0):
        extra_to_spend_color = "rgb(200, 107, 107)"
    else:
        extra_to_spend_color = "rgb(84, 163, 115)"

    all_expenses = Expense.objects.all()


    context = {
        'daily_expenses' : daily_expenses,
        'todays_expenses' : todays_expenses,
        'all_expenses' : all_expenses,
        'month_expenses' : month_expenses,
        'month_expenses_per_type_data' : month_expenses_per_type_data,
        'expense_types' : expense_types,
        'month_total_formatted': "{:,.2f}".format(rounded_month_total),
        'month_total': rounded_month_total,
        'avg_cost_per_day': "{:,.2f}".format(avg_cost_per_day),
        'exp_month_total': "{:,.2f}".format(exp_month_total),
        'extra_to_spend': extra_to_spend,
        'extra_to_spend_color': extra_to_spend_color,
        'current_day': current_date.day,
        'expenses': expenses,
        'btc_usd': "{:,.2f}".format(btc_usd),
        'usd_mxn': usd_mxn,
    }

    return render(request, 'spendings/statistics.html', context)

def data(request):
    all_expenses = Expense.objects.all().order_by('-id')
    paginator = Paginator(all_expenses, 15)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'all_expenses' : all_expenses,
        'page_obj' : page_obj,
    }

    return render(request, 'spendings/data.html', context)


def edit_expense(request, expense_pk):
    expense = Expense.objects.get(id = expense_pk)
    expense_form = ExpenseForm(instance=expense)

    if request.method == 'POST':
        expense_form = ExpenseForm(request.POST, instance=expense)
        if expense_form.is_valid:
            expense = expense_form.save()
            expense.save()

        return redirect('data')

    context = {
        'expense_form': expense_form,
    }

    return render(request, 'spendings/edit_expense.html', context)






