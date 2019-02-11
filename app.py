from flask import Flask, jsonify, request

from model.expense import Expense, ExpenseSchema
from model.income import Income, IncomeSchema
from model.transaction_type import TransactionType


app = Flask(__name__)

transactions = [
  Income('Salary', 5000),
  Income('Dividends', 200),
  Expense('pizza', 50),
  Expense('Rock Concert', 100)
]

@app.route('/incomes')
def get_incomes():
    schema = IncomeSchema(many=True)
    incomes = schema.dump(
        filter(lambda t: t.type == TransactionType.INCOME, transactions)
    )
    return jsonify(incomes.data)

@app.route('/incomes', methods=['POST'])
def add_incomes():
    income = IncomeSchema().load(request.get_json())
    transactions.append(income)
    return '', 204

@app.route('/expense')
def get_expenses():
    schema = ExpenseSchema(many=True)
    expenses = schema.dump(
        filter(lambda t: t.type == TransactionType.EXPENSE, transactions)
    )
    return jsonify(expenses.data)

@app.route('/expense', methods=['POST'])
def add_expenses():
    expense = ExpenseSchema().load(request.get_json())
    transactions.append(expense)
    return '', 204
