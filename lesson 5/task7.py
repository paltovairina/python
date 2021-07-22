import json

firm_inform_list = []
average_profit_list = []
profit_dict = {}
average_profit_dict = {}
with open("firms_info.txt", "r", encoding="UTF=8") as firm_info:
    for line in firm_info:
        firm_inform = line.split()
        firm_name = firm_inform[0]
        firm_proceeds = firm_inform[2]
        firm_proceeds = float(firm_proceeds)
        firm_costs = firm_inform[3]
        firm_costs = float(firm_costs)
        firm_profit = firm_proceeds - firm_costs
        profit_dict.update({firm_name: firm_profit})
        if firm_profit > 0:
            average_profit_list.append(firm_profit)
    average_profit = sum(average_profit_list) / len(average_profit_list)
    average_profit_dict = {"average_profit": average_profit}
firm_inform_list = [profit_dict, average_profit_dict]
with open("firm_info.json", "w") as f:
    json.dump(firm_inform_list, f)
