import csv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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

with open(r"C:\work\hyperskill.org\python\SQL with Python\csv\companies.csv") as companies:
    file_reader = csv.reader(companies, delimiter=",")
    count = 0
    for line in file_reader:
        if count == 0:
            count += 1
        else:
            company = Companies(ticker=line[0], name=line[1], sector=line[2])
            session.add(company)
            count += 1

session.commit()

with open(r"C:\work\hyperskill.org\python\SQL with Python\csv\financial.csv") as financial:
    file_reader = csv.reader(financial, delimiter=",")
    count = 0
    for line in file_reader:
        if count == 0:
            count += 1
        else:
            for i in range(10):
                if line[i] == "":
                    line[i] = None

            financial_ = Financial(ticker=line[0], ebitda=line[1], sales=line[2], net_profit=line[3],
                                   market_price=line[4], net_debt=line[5], assets=line[6], equity=line[7],
                                   cash_equivalents=line[8], liabilities=line[9])
            session.add(financial_)
            count += 1

session.commit()

print("Database created successfully!")
