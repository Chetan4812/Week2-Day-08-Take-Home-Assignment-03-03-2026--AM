def calculate_tax(annual_income):
    STANDARD_DEDUCTION = 75000

    taxable_income = max(0, annual_income - STANDARD_DEDUCTION)

    slabs = [
        (300000, 0.00),
        (700000, 0.05),
        (1000000, 0.10),
        (1200000, 0.15),
        (1500000, 0.20),
        (float('inf'), 0.30)
    ]

    previous_limit = 0
    total_tax = 0
    breakdown = []

    for limit, rate in slabs:
        if taxable_income > previous_limit:
            income_in_slab = min(taxable_income, limit) - previous_limit
            tax_for_slab = income_in_slab * rate
            total_tax += tax_for_slab

            breakdown.append({
                "slab_range": f"{previous_limit} - {limit if limit != float('inf') else 'Above'}",
                "income_in_slab": income_in_slab,
                "rate": rate,
                "tax": tax_for_slab
            })

            previous_limit = limit
        else:
            break

    effective_tax_rate = (total_tax / annual_income) * 100 if annual_income > 0 else 0

    return taxable_income, breakdown, total_tax, effective_tax_rate


if __name__ == "__main__":

    try:
        annual_income = float(input("Enter Annual Income (₹): "))

        if annual_income < 0:
            print("Income cannot be negative.")
        else:
            taxable_income, breakdown, total_tax, effective_tax_rate = calculate_tax(annual_income)

            print("\n----- TAX BREAKDOWN (New Regime FY 2024-25) -----")
            print(f"Annual Income: ₹{annual_income:,.2f}")
            print(f"Standard Deduction: ₹75,000")
            print(f"Taxable Income: ₹{taxable_income:,.2f}\n")

            for slab in breakdown:
                print(f"Slab: {slab['slab_range']}")
                print(f"  Income in Slab: ₹{slab['income_in_slab']:,.2f}")
                print(f"  Tax Rate: {slab['rate']*100}%")
                print(f"  Tax: ₹{slab['tax']:,.2f}\n")

            print("-------------------------------------------")
            print(f"Total Tax Payable: ₹{total_tax:,.2f}")
            print(f"Effective Tax Rate: {effective_tax_rate:.2f}%")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")