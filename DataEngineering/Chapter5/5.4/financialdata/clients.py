from sqlalchemy import (
    create_engine,
    engine,
)


def get_mysql_financialdata_conn() -> engine.base.Connection:
    """
    user: root
    password: test
    host: localhost
    port: 3306
    database: financialdata
    如果有實體 IP，以上設定可以自行更改
    """
    address = "mysql+pymysql://root:test@localhost:3306/FinancialData"
    engine = create_engine(address)
    connect = engine.connect()
    return connect

def get_postgre_financialdata_conn() -> engine.base.Connection:
    """
    user: postgres
    password: 123456
    host: localhost
    port: 5432
    database: financialdata
    如果有實體 IP，以上設定可以自行更改
    """
    address = "postgresql://postgres:123456@localhost:5432/FinancialData"
    engine = create_engine(address)
    connect = engine.connect()
    return connect
