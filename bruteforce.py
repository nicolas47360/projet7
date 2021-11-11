import itertools
import csv


def profit(datas):
    benefice = 0
    for action in datas:
        action['price'] = float(action['price'])
        action['profit'] = float(action['profit'])
        benefice += action['price'] * action['profit']/100
    return benefice


def price_actions(datas):
    action_sum = 0
    for action in datas:
        action_sum += float((action['price']))
    return action_sum


def combinations(datas):
    all_combinations = []
    for i in range(len(datas)):
        for combination in itertools.combinations(datas, i):
            if price_actions(combination) <= 500:
                all_combinations.append(combination)
    return all_combinations


def profits_combinations(datas):
    bests_profits = []
    best_combination = combinations(datas)
    for combination in best_combination:
        bests_profits.append(
            {'actions': combination,
             'price': price_actions(combination),
             'profit': profit(combination)})
    best = sorted(bests_profits, key=lambda x: x["profit"], reverse=True)
    return best[0]


def results(datas):
    best = profits_combinations(datas)
    print(f"Le profit est de: {best['profit']} \n"
          f"Le total des actions achetées est de : {best['price']} \n"
          f"L'ensemble des actions sont: \n"
          f"{best['actions']}")



def read_csv(csv_data):
    with open(csv_data, newline='') as isfile:
        reader = csv.DictReader(isfile)
        datas = []
        for row in reader:
            datas.append(row)
    return datas


if __name__ == '__main__':
    data = read_csv("action.csv")
    results(data)





