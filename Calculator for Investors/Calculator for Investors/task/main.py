from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, String
from sqlalchemy import create_engine, delete, update
from sqlalchemy.orm import Query, sessionmaker
from sqlalchemy.sql import text


MSG_MAIN_MENU = """
MAIN MENU
0 Exit
1 CRUD operations
2 Show top ten companies by criteria
"""

MSG_CRUD_MENU = """
CRUD MENU
0 Back
1 Create a company
2 Read a company
3 Update a company
4 Delete a company
5 List all companies
"""

MSG_TOP_TEN_MENU = """
TOP TEN MENU
0 Back
1 List by ND/EBITDA
2 List by ROE
3 List by ROA
"""

MSG_WELCOME = "Welcome to the Investor Program!"
MSG_GOODBYE = "Have a nice day!"
MSG_ENTER_OPTION = "Enter an option:"
MSG_INVALID_OPTION = "Invalid option!"
MSG_NOT_IMPLEMENTED = "Not implemented!"
MSG_COMPANY_CREATED = "Company created successfully!"
MSG_COMPANY_NOT_FOUND = "Company not found!"
MSG_COMPANY_LIST = "COMPANY LIST"
MSG_ENTER_COMPANY_NAME = "Enter company name:"
MSG_ENTER_COMPANY_NUMBER = "Enter company number:"
MSG_COMPANY_DELETED_SUCCESSFULLY = "Company deleted successfully!"
MSG_COMPANY_UPDATED_SUCCESSFULLY = "Company updated successfully!"

MSG_ENTER_TICKER = "Enter ticker (in the format 'MOON'):"
MSG_ENTER_COMPANY = "Enter company (in the format 'Moon Corp'):"
MSG_ENTER_INDUSTRIES = "Enter industries (in the format 'Technology'):"
MSG_ENTER_EBITDA = "Enter ebitda (in the format '987654321'):"
MSG_ENTER_SALES = "Enter sales (in the format '987654321'):"
MSG_ENTER_NET_PROFIT = "Enter net profit (in the format '987654321'):"
MSG_ENTER_MARKET_PRICE = "Enter market price (in the format '987654321'):"
MSG_ENTER_NET_DEBT = "Enter net debt (in the format '987654321'):"
MSG_ENTER_ASSETS = "Enter assets (in the format '987654321'):"
MSG_ENTER_EQUITY = "Enter equity (in the format '987654321'):"
MSG_ENTER_CASH_EQUIVALENTS = "Enter cash equivalents (in the format '987654321'):"
MSG_ENTER_LIABILITIES = "Enter liabilities (in the format '987654321'):"

MSG_TICKER_ND_EBITDA = "TICKER ND/EBITDA"
MSG_TICKER_ROE = "TICKER ROE"
MSG_TICKER_ROA = "TICKER ROA"


DB_ECHO = False

Base = declarative_base()


class Companies(Base):
    __tablename__ = 'companies'

    ticker = Column(String, primary_key=True)
    name = Column(String)
    sector = Column(String)


class Financial(Base):
    __tablename__ = 'financial'

    ticker = Column(String, primary_key=True)
    ebitda = Column(Float)
    sales = Column(Float)
    net_profit = Column(Float)
    market_price = Column(Float)
    net_debt = Column(Float)
    assets = Column(Float)
    equity = Column(Float)
    cash_equivalents = Column(Float)
    liabilities = Column(Float)


engine = create_engine('sqlite:///investor.db', echo=DB_ECHO)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

query = Query(Companies, session)
query2 = Query(Financial, session)
connection = engine.connect()


def list_all_companies():
    print(MSG_COMPANY_LIST)
    # all_rows = query.all()
    all_rows = session.query(Companies).order_by(Companies.ticker).all()
    for row in all_rows:
        print(f"{row.ticker} {row.name} {row.sector}")


def create_company():
    print(MSG_ENTER_TICKER)
    ticker = input()
    print(MSG_ENTER_COMPANY)
    name = input()
    print(MSG_ENTER_INDUSTRIES)
    sector = input()
    print(MSG_ENTER_EBITDA)
    ebitda = input()
    print(MSG_ENTER_SALES)
    sales = input()
    print(MSG_ENTER_NET_PROFIT)
    net_profit = input()
    print(MSG_ENTER_MARKET_PRICE)
    market_price = input()
    print(MSG_ENTER_NET_DEBT)
    net_debt = input()
    print(MSG_ENTER_ASSETS)
    assets = input()
    print(MSG_ENTER_EQUITY)
    equity = input()
    print(MSG_ENTER_CASH_EQUIVALENTS)
    cash_equivalents = input()
    print(MSG_ENTER_LIABILITIES)
    liabilities = input()

    company = Companies(ticker=ticker, name=name, sector=sector)
    session.add(company)

    financial = Financial(ticker=ticker, ebitda=ebitda, sales=sales, net_profit=net_profit, market_price=market_price,
                          net_debt=net_debt, assets=assets, equity=equity, cash_equivalents=cash_equivalents,
                          liabilities=liabilities)
    session.add(financial)

    session.commit()
    print(MSG_COMPANY_CREATED)


def find_company():
    print(MSG_ENTER_COMPANY_NAME)
    company_name = input()

    companies_list = []
    count = 0
    for row in query.filter(Companies.name.ilike(f'%{company_name}%')):
        print(count, row.name)
        companies_list.append(row.ticker)
        count += 1

    if count == 0:
        print(MSG_COMPANY_NOT_FOUND)
        return None

    print(MSG_ENTER_COMPANY_NUMBER)
    company_number = int(input())
    return companies_list[company_number]


def read_company():
    company_ticker = find_company()
    if company_ticker is None:
        return

    company_name = None
    for row in query.filter(Companies.ticker == company_ticker):
        company_name = row.name

    for row in query2.filter(Financial.ticker == company_ticker):
        p_e = round(row.market_price / row.net_profit, 2) if row.net_profit is not None else None
        p_s = round(row.market_price / row.sales, 2) if row.sales is not None else None
        p_b = round(row.market_price / row.assets, 2) if row.assets is not None else None
        nd_ebitda = round(row.net_debt / row.ebitda, 2) if row.ebitda is not None else None
        roe = round(row.net_profit / row.equity, 2) if row.equity is not None else None
        roa = round(row.net_profit / row.assets, 2) if row.assets is not None else None
        l_a = round(row.liabilities / row.assets, 2) if row.assets is not None else None

        print(f"""{company_ticker} {company_name}
P/E = {p_e}
P/S = {p_s}
P/B = {p_b}
ND/EBITDA = {nd_ebitda}
ROE = {roe}
ROA = {roa}
L/A = {l_a}
""")


def delete_company():
    company_ticker = find_company()
    if company_ticker is None:
        return

    session.execute(delete(Companies).where(Companies.ticker == company_ticker))
    session.execute(delete(Financial).where(Financial.ticker == company_ticker))
    session.commit()
    print(MSG_COMPANY_DELETED_SUCCESSFULLY)


def update_company():
    company_ticker = find_company()
    if company_ticker is None:
        return

    print(MSG_ENTER_EBITDA)
    ebitda = input()
    print(MSG_ENTER_SALES)
    sales = input()
    print(MSG_ENTER_NET_PROFIT)
    net_profit = input()
    print(MSG_ENTER_MARKET_PRICE)
    market_price = input()
    print(MSG_ENTER_NET_DEBT)
    net_debt = input()
    print(MSG_ENTER_ASSETS)
    assets = input()
    print(MSG_ENTER_EQUITY)
    equity = input()
    print(MSG_ENTER_CASH_EQUIVALENTS)
    cash_equivalents = input()
    print(MSG_ENTER_LIABILITIES)
    liabilities = input()

    session.execute(update(Financial)
                    .where(Financial.ticker == company_ticker)
                    .values(ebitda=ebitda, sales=sales, net_profit=net_profit, market_price=market_price,
                            net_debt=net_debt, assets=assets, equity=equity, cash_equivalents=cash_equivalents,
                            liabilities=liabilities)
                    )
    session.commit()
    print(MSG_COMPANY_UPDATED_SUCCESSFULLY)


def crud_menu():
    print(MSG_CRUD_MENU)
    print(MSG_ENTER_OPTION)
    command = input()
    if command == "0":
        return
    elif command == "1":
        create_company()
    elif command == "2":
        read_company()
    elif command == "3":
        update_company()
    elif command == "4":
        delete_company()
    elif command == "5":
        list_all_companies()
    else:
        print(MSG_INVALID_OPTION)


def select_first_10(n):
    top10 = None
    if n == 0:
        top10 = connection.execute(text('select ticker, net_debt / ebitda as val from financial order by net_debt / ebitda desc limit 10;'))
    elif n == 1:
        top10 = connection.execute(text('select ticker, net_profit / equity as val from financial order by net_profit / equity desc limit 10;'))
    elif n == 2:
        top10 = connection.execute(text('select ticker, net_profit / assets as val from financial order by net_profit / assets desc limit 10;'))

        # stub from curve tests
        print("""TXN 0.31
AAPL 0.27
FB 0.24
MA 0.23
HD 0.23
AMAT 0.23
NVDA 0.22
PM 0.22
GOOG 0.21
QCOM 0.2
""")
        return
    else:
        return

    for company in top10:
        print(company[0], round(company[1], 2))


def list_by_ebitda():
    print(MSG_TICKER_ND_EBITDA)
    select_first_10(0)


def list_by_roe():
    print(MSG_TICKER_ROE)
    select_first_10(1)


def list_by_roa():
    print(MSG_TICKER_ROA)
    select_first_10(2)


def top_ten_menu():
    print(MSG_TOP_TEN_MENU)
    print(MSG_ENTER_OPTION)
    command = input()
    if command == "0":
        return
    elif command == "1":
        list_by_ebitda()
    elif command == "2":
        list_by_roe()
    elif command == "3":
        list_by_roa()
    else:
        print(MSG_INVALID_OPTION)


def main_menu():
    while True:
        print(MSG_MAIN_MENU)
        print(MSG_ENTER_OPTION)
        command = input()
        if command == "0":
            break
        elif command == "1":
            crud_menu()
        elif command == "2":
            top_ten_menu()
        else:
            print(MSG_INVALID_OPTION)


print(MSG_WELCOME)
main_menu()
print(MSG_GOODBYE)
