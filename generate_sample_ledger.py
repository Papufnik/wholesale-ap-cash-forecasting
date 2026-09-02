import openpyxl
from datetime import date, timedelta
import os

"""
generate_sample_ledger.py -- creates a small fake operating-ledger workbook
so wholesale_ap_cash_forecast.py can be run and inspected without any real
business data. Run this once before running the main script.
"""

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(HERE, "sample_data", "operating_ledger.xlsx")


def build_sample_ledger():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Ledger"
    ws.append(["Date", "Description", "Category", "Debit", "Credit", "Balance"])
    ws.append(["", "", "", "", "", ""])

    balance = 10000.0
    d = date.today() - timedelta(days=20)
    for i in range(20):
        d = d + timedelta(days=1)
        balance += (i % 3 - 1) * 150.25
        ws.append([d, "Sample transaction", "Ops", 100.0, 0, round(balance, 2)])

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    wb.save(OUT_PATH)
    print(f"[OK] Sample ledger written -> {OUT_PATH}")


if __name__ == "__main__":
    build_sample_ledger()
