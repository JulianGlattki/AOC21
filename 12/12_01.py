file1 = open('input.txt', 'r')
lines = file1.readlines()

START_CAVE_NAME = 'start'
END_CAVE_NAME = 'end'


class CaveSystem:
    def __init__(self):
        self.caves = []
        self.paths = set()

    def add_cave_if_not_present(self, cave):
        if cave not in self.caves:
            self.caves.append(cave)

    def find_cave(self, name):
        try:
            return next(filter(lambda x: x.name == name, self.caves))
        except:
            return None

    def get_start_cave(self):
        try:
            return next(filter(lambda x: x.name == START_CAVE_NAME, self.caves))
        except:
            return None

    def find_paths(self):
        start_cave = cave_system.get_start_cave()

        self.get_paths(start_cave, [])

        return self.paths

    def get_paths(self, cave, current_path):
        current_path.append(cave)
        cave.set_visisted_if_small_cave()

        if cave.is_end():
            self.paths.add('-'.join([str(x) for x in current_path]))
            return

        unvisited_connected_caves = cave.get_connected_unvisited_caves()
        if unvisited_connected_caves is not None:
            for next_cave in unvisited_connected_caves:
                self.get_paths(next_cave, current_path.copy())

        cave.reset()


class Cave:
    def __init__(self, name):
        self.connected_caves = []
        self.name = name
        self.is_small_cave = name.islower()
        self.visited = False

    def add_connected_cave(self, connected_cave):
        if not self.is_end() and not connected_cave.is_start() and connected_cave not in self.connected_caves:
            self.connected_caves.append(connected_cave)

    def get_connected_unvisited_caves(self):
        return list(filter(lambda x: x.is_visited() is False, self.connected_caves))

    def is_visited(self):
        return self.visited

    def set_visisted_if_small_cave(self):
        if not self.is_end() and not self.is_start() and self.is_small_cave:
            self.visited = True

    def reset(self):
        self.visited = False

    def is_start(self):
        return self.name == START_CAVE_NAME

    def is_end(self):
        return self.name == END_CAVE_NAME

    def __str__(self):
        return self.name


cave_system = CaveSystem()

for line in lines:
    connected_caves = line.strip('\n').split('-')

    left_cave = cave_system.find_cave(connected_caves[0]) if cave_system.find_cave(connected_caves[0]) is not None \
        else Cave(connected_caves[0])
    right_cave = cave_system.find_cave(connected_caves[1]) if cave_system.find_cave(connected_caves[1]) is not None \
        else Cave(connected_caves[1])

    left_cave.add_connected_cave(right_cave)
    right_cave.add_connected_cave(left_cave)

    cave_system.add_cave_if_not_present(left_cave)
    cave_system.add_cave_if_not_present(right_cave)


print(len(cave_system.find_paths()))

