def calculate_risk(income: float, expenses: float):
    risk = 0
    explanation = []

    if income < 0:
        risk += 50
        explanation.append("No Income Detected, risk inc.")

    # calculate savings rate and adjust risk based on it
    if income > 0:
        savings_rate = (income - abs(expenses)) / income
    else:
        savings_rate = 0
    
    # low savings rate means high risk (money will run out)
    if savings_rate < 0.1:
        risk += 30
        explanation.append("Low savings rate")
    
    # moderate savings rate means moderate risk (some buffer but could be better)
    elif savings_rate < 0.2:
        risk += 15
        explanation.append("Moderate savings rate")

    # high savings rate means low risk (good buffer)
    if expenses > income:
        risk += 20
        explanation.append("Expenses exceed income")

    risk = min(risk, 100)

    if risk < 30:
        level = "Low"
    elif risk < 60:
        level = "Medium"
    else:
        level = "High"

    # joins the explanation list into a single string separated by commas and returns the risk score, level, and explanation
    return risk, level, ", ".join(explanation)