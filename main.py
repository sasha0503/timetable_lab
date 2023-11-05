import json

from CSP import CSP
from genetic_alg import genetic_algorithm, evaluate_population, get_max_score, groups_hours, subjects_raw

if __name__ == '__main__':
    full_score = get_max_score()

    while True:
        try:
            best_score = 0
            while best_score != full_score:
                population_test = genetic_algorithm(128, 10)
                best_score, average_score, best_schedule = evaluate_population(population_test)

            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
            periods = list(range(1, 7))

            all_classes = [(day, period) for day in days for period in periods]

            variables = []
            for (group, hours), teachers in zip(groups_hours.items(), best_schedule):
                for hour, teacher in zip(hours, teachers):
                    for i in range(hour):
                        variables.append((group, teacher, i))

            Domains = {var: all_classes for var in variables}

            constraints = {}
            for var in variables:
                constraints[var] = [var2 for var2 in variables if
                                    var2 != var and (var[0] == var2[0] or var[1] == var2[1])]

            csp = CSP(variables, Domains, constraints)
            res = csp.solve()

            break
        except RecursionError:
            pass

    print("Found!")

    res_inv = {}
    for k, v in res.items():
        if v not in res_inv:
            res_inv[v] = [k]
        else:
            res_inv[v].append(k)

    groups_str = [group for group in groups_hours]

    for day in days:
        print(day)
        for period in periods:
            print(period, end=": ")
            if (day, period) in res_inv:
                for group, teacher, i in res_inv[(day, period)]:
                    teachers_list = best_schedule[list(groups_hours.keys()).index(group)]
                    indices = [j for j in range(len(teachers_list)) if teachers_list[j] == teacher]
                    subject = [subj for j, subj in enumerate(subjects_raw) if j in indices]
                    subject = ', '.join(subject)
                    print(f"{group} {subject} ({teacher})", end=" ")
            print()
        print()
