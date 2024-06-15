import pandas as pd
from dataclasses import dataclass, field


TRADE_BAR_PROPERTIES = ["time", "open", "high", "low", "close", "volume"]

DEFAULT_MARKET_DATA_ID = 55
DEFAULT_CONTRACT_ID = 44

CREATE_BID_ASK_DATA = """
CREATE TABLE IF NOT EXISTS bid_ask_data
  (
     timestamp DATETIME,
     symbol STRING,
     bid_price REAL,
     ask_price REAL,
     bid_size INTEGER,
     ask_size INTEGER
  )"""

CREATE_ORDER_STATUS = """
CREATE TABLE IF NOT EXISTS order_status
  (
     timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
     order_id INTEGER,
     client_id INTEGER,
     status STRING,
     filled REAL,
     remaining REAL,
     last_fill_price REAL,
     avg_fill_price REAL
  )"""

CREATE_OPEN_ORDERS = """
CREATE TABLE IF NOT EXISTS open_orders
  (
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    order_id INTEGER,
    symbol STRING,
    sec_type STRING,
    exhange STRING,
    action STRING,
    order_type STRING,
    quantity INTEGER,
    status STRING
  )"""

CREATE_TRADES = """
CREATE TABLE IF NOT EXISTS trades
  (
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    request_id INTEGER,
    order_id INTEGER,
    execution_id INTEGER,
    symbol STRING,
    sec_type STRING,
    currency STRING,
    quantity INTEGER,
    last_liquidity REAL
  )"""

CREATE_END_OF_DAY = """
CREATE TABLE IF NOT EXISTS end_of_day
  (
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    account_code STRING,
    available_funds REAL,
    buying_power REAL,
    cash_balance REAL,
    cushion REAL,
    equity_with_loan_value REAL,
    excess_liquidity REAL,
    gross_position_value REAL,
    init_margin_req REAL,
    maint_margin_req REAL,
    money_market_fund_value REAL,
    net_liquidation REAL,
    realized_pnl REAL,
    reg_t_equity REAL,
    reg_t_margin REAL,
    sma REAL,
    unrealized_pnl REAL
  )"""

END_OF_DAY_FIELDS = [
    "AccountCode",
    "AvailableFunds",
    "BuyingPower",
    "CashBalance",
    "Cushion",
    "EquityWithLoanValue",
    "ExcessLiquidity",
    "GrossPositionValue",
    "InitMarginReq",
    "MaintMarginReq",
    "MoneyMarketFundValue",
    "NetLiquidation",
    "RealizedPnL",
    "RegTEquity",
    "RegTMargin",
    "SMA",
    "UnrealizedPnL",
]


@dataclass
class Tick:
    time: int
    bid_price: float
    ask_price: float
    bid_size: int
    ask_size: int
    timestamp_: pd.Timestamp = field(init=False)

    def __post_init__(self):
        self.timestamp_ = pd.to_datetime(self.time, unit="s")
        self.bid_price = float(self.bid_price)
        self.ask_price = float(self.ask_price)
        self.bid_size = int(self.bid_size)
        self.ask_size = int(self.ask_size)
