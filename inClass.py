def main():
    # Stock transaction details
    shares_purchased = 1000
    purchase_price = 32.87
    purchase_commission = 0.02  # 2%

    shares_sold = 1000
    selling_price = 33.92
    selling_commission = 0.02  # 2%

    # Calculations
    amount_paid = shares_purchased * purchase_price
    purchase_commission = amount_paid * purchase_commission

    amount_sold = shares_sold * selling_price
    selling_commission = amount_sold * selling_commission

    net_profit = amount_sold - selling_commission - (amount_paid + purchase_commission)

    # Output results
    print("Amount of money Joe paid for the stock: ${:.2f}".format(amount_paid))
    print("Commission Joe paid his broker when buying the stock: ${:.2f}".format(purchase_commission))
    print("Amount Joe sold the stock for: ${:.2f}".format(amount_sold))
    print("Commission Joe paid his broker when selling the stock: ${:.2f}".format(selling_commission))
    print("Net profit (or loss if negative): ${:.2f}".format(net_profit))



main()
