'''
3. You're working on some stock-prediction software.
The function you're writing accepts an array of
predicted prices for a particular stock.
The function you're writing accepts an array
of predicted prices for a particular stock
over the course of time.

For example, this array of seven prices:

[10, 7, 5, 8, 11, 2, 6]

predicts that a given stock will have these prices
over the next seven days.

your function should calcute the greatest profit that could be made from a
single 'buy' transaction followed by a single 'sell' transaction.

The solution is O(N)
'''
def max_profit(A):
    current_smallest_stock = float('inf')
    largest_profit = -float('inf')
    for x in A:
        largest_profit = max(largest_profit, x - current_smallest_stock)
        current_smallest_stock = min(current_smallest_stock, x)
    return largest_profit

