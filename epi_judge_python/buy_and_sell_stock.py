from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    minimum_price, profit = float('inf'), 0
    for price in prices:
        max_profit_sell_today = price - minimum_price
        profit = max(max_profit_sell_today, profit)
        minimum_price = min(price, minimum_price)
    return profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
