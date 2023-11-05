import random
from copy import deepcopy
from dataclasses import dataclass


# -------------- define dataclasses ----------------------

@dataclass
class Teacher:
    name: str
    max_hours: int
    classes: list


@dataclass
class Group:
    id: str
    hours: list
    teachers: list


# -------------- create groups and teachers --------------

# hours and teachers go in order: [english, history, math, science, literature, arts]

groups_hours = {
    "1A": [2, 5, 2, 0, 6, 3],
    "1B": [4, 2, 0, 0, 3, 3],
    "1C": [2, 0, 2, 3, 2, 2],
    "1D": [0, 0, 2, 5, 0, 1],
}

teachers = [
    Teacher("bob", 7, ["english", "history"]),
    Teacher("alice", 7, ["english", "history", "arts"]),
    Teacher("victor", 5, ["math", "science"]),
    Teacher("jane", 11, ["arts", "literature"]),
    Teacher("james", 7, ["literature"]),
    Teacher("john", 8, ["english"]),
    Teacher("sarah", 4, ["math", "science"]),
    Teacher("mike", 14, ["math"]),
    Teacher("sam", 4, ["science"]),
]

# ----------- create helpful data structures -------------

subjects_raw = ["english", "history", "math", "science", "literature", "arts"]
subjects2teachers = {}

for subject in subjects_raw:
    subjects2teachers[subject] = []
    for teacher in teachers:
        if subject in teacher.classes:
            subjects2teachers[subject].append(teacher.name)


def create_schedule():
    schedule = []
    for _ in range(len(groups_hours)):
        teachers_for_group = []
        for subject_teachers in subjects2teachers.values():
            teachers_for_group.append(random.choice(subject_teachers))
        schedule.append(teachers_for_group)
    return schedule


def evaluate(schedule):
    teacher_hours = {teacher.name: teacher.max_hours for teacher in teachers}
    score = 0
    for i, group in enumerate(groups_hours):
        group = Group(group, groups_hours[group], schedule[i])
        for group_teacher, hours in zip(group.teachers, group.hours):
            if hours > teacher_hours[group_teacher]:
                score += teacher_hours[group_teacher]
                teacher_hours[group_teacher] = 0
            else:
                score += hours
                teacher_hours[group_teacher] -= hours

    return score


def create_population(population_size=16):
    population = []
    for _ in range(population_size):
        schedule = create_schedule()
        population.append(schedule)
    return population


def competition(population):
    new_population = []
    for i in range(0, len(population) // 2):
        schedule1 = population[i]
        schedule2 = population[i + 1]
        score1 = evaluate(schedule1)
        score2 = evaluate(schedule2)
        if score1 > score2:
            new_population.append(schedule1)
        else:
            new_population.append(schedule2)
    return new_population


def crossover(population):
    schedule_half = len(population[0]) // 2
    for i in range(0, len(population), 2):
        schedule1 = population[i]
        schedule2 = population[i + 1]
        population.append(schedule1[:schedule_half] + schedule2[schedule_half:])
        population.append(schedule2[:schedule_half] + schedule1[schedule_half:])
    return population


def mutation(population, mutation_rate=0.1):
    local_population = deepcopy(population)
    for schedule in local_population:
        for group in schedule:
            for i in range(len(group)):
                if random.random() < mutation_rate:
                    group[i] = random.choice(subjects2teachers[subjects_raw[i]])
    return local_population


def generic_step(population):
    local_best_score, local_average, local_best_schedule = evaluate_population(population)
    # print(f"## best score: {evaluate(local_best_schedule)}")
    population = competition(population)
    population = crossover(population)
    population = mutation(population, 0)
    if local_best_schedule != population[0]:
        population.insert(0, local_best_schedule)
    return population


def genetic_algorithm(population_size, generations):
    population = create_population(population_size)
    for _ in range(generations):
        population = generic_step(population)
    return population


def get_max_score():
    max_score = 0
    for hours in groups_hours.values():
        for hour in hours:
            max_score += hour
    return max_score


def evaluate_population(population):
    scores = []
    for schedule in population:
        scores.append(evaluate(schedule))
    return max(scores), sum(scores) / len(scores), population[scores.index(max(scores))]


def print_schedule(schedule):
    for i, group in enumerate(groups_hours):
        group = Group(group, groups_hours[group], schedule[i])
        print(f"group {group.id}:")
        for subj, teacher in zip(subjects_raw, group.teachers):
            print(f"\t{subj}: {teacher}")


if __name__ == '__main__':
    print(f"best score: {get_max_score()}")

    population_test = genetic_algorithm(128, 100)
    population_simple = create_population(128)

    best_score, average_score, best_schedule = evaluate_population(population_test)
    best_score_simple, average_score_simple, best_schedule_simple = evaluate_population(population_simple)

    print_schedule(best_schedule)

    print("-----genetic algorithm-----")
    print(f"@@@@ average score: {average_score}")
    print(f"@@@@ best score: {best_score}")

    print("-----simple population-----")
    print(f"@@@@ average score: {average_score_simple}")
    print(f"@@@@ best score: {best_score_simple}")
