def calculate_pre_assessment(balanceSheetData, business):
    # Fetch the balance sheet data for the business using an API call
    business_id = business['data'][0]['id']
    balance_sheet_data = balanceSheetData  # Replace with your API call logic

    loan_amount = float(business['data'][0]['loan_amount'])

    if len(balance_sheet_data) < 12:
        return 20  # Default value

    profit_or_loss_values = [float(record['profit_or_loss']) for record in balance_sheet_data]
    assets_values = [float(record['assets_value']) for record in balance_sheet_data]

    average_profit_or_loss = sum(profit_or_loss_values) / len(profit_or_loss_values)
    average_assets_value = sum(assets_values) / len(assets_values)

    if average_profit_or_loss > 0:
        return 60  # Favorable assessment

    if average_assets_value > loan_amount:
        return 100  # Highly favorable assessment

    return 20  # Default value
