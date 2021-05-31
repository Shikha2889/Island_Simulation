import random


def populate_island(red_hawk_cnt, snake_cnt, puma_cnt, shuffle_population=False):
    animals_in_island = (["red_hawks"] * red_hawk_cnt) + (["snake"] * snake_cnt) + (["puma"] * puma_cnt)
    if shuffle_population:
        random.shuffle(animals_in_island)
    return animals_in_island


def get_random_animals_index_from_island(populated_island):
    return random.sample(range(len(populated_island)), 2)


def get_animals_from_index_positions(animals, *index_positions):
    return {animals[idx]: idx for idx in index_positions}


def remove_dead_animal(current_animals, indexes_positions):
    indexes_positions = {indexes_positions}

    return [i for j, i in enumerate(current_animals) if j not in indexes_positions]


def get_survived_animal_from_the_selection(selected_animals, dead_animal):
    return list(set(selected_animals) - set(dead_animal))[0]


animal_populations = [[10, 10, 10], [10, 9, 10], [10, 8, 10], [10, 7, 10], [10, 6, 10], [10, 5, 10], [10, 4, 10],
                      [10, 3, 10], [10, 2, 10], [10, 1, 10]]  # populations of red hawk, snake and puma
DEATH_STRATEGY = {("red_hawks", "snake"): "snake", ("snake", "red_hawks"): "snake",
                  ("snake", "puma"): "puma", ("puma", "snake"): "puma", ("puma", "red_hawks"): "red_hawks",
                  ("red_hawks", "puma"): "red_hawks"}

experiment_cnt = 300000
for red_hawks_population, snake_population, puma_population in animal_populations:
    animals_in_island = populate_island(red_hawks_population, snake_population, puma_population,
                                        shuffle_population=True)
    red_hawks_counter = 0
    snake_counter = 0
    puma_counter = 0
    animal_population_cnt = len(animals_in_island)
    animal_counter = {'red_hawks': 0, 'snake': 0, 'puma': 0}
    for _ in range(experiment_cnt):
        while True:

            if len(animals_in_island) == 1 or len(set(animals_in_island)) == 1:  # only one animal survived
                break

            animal_index1, animal_index2 = get_random_animals_index_from_island(
                animals_in_island)  # randomly selecting two animals from the island
            animals = get_animals_from_index_positions(animals_in_island, animal_index1, animal_index2)
            if len(animals.keys()) == 1:  # both selected animals are same, then do nothing
                animal_counter[list(animals.keys())[0]] += 1
                continue
            animals_in_island = remove_dead_animal(animals_in_island, animals[
                DEATH_STRATEGY[tuple(animals)]])  # remove the animal which is dead from the island
            survived_animal = get_survived_animal_from_the_selection(tuple(animals), DEATH_STRATEGY[tuple(animals)])
            animal_counter[survived_animal] += 1

    print(
        f"""For the given population of {red_hawks_population},{snake_population},{puma_population} only {animal_counter} survived""")
