# Дан список размеров(длина, ширина) эллипсов
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# Напишите функцию find_farthest_orbit(list_of_orbits),
# которая находит площадь самого большого эллипса и возвращает кортеж с его размерами.
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b – длины и ширина осей эллипса
# - Площадь кругов учитывать не нужно, т.е если у эллипса a == b, то это круг.
# При решении задачи используйте списочные выражения.
# Гарантируется, что самый большой эллипс всего один.

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
#
# s = lambda cur_tuple: cur_tuple[0] * cur_tuple[1]
#
# max_s = s(orbits[0])
# find_tuple = orbits[0]
#
# for cur_orbit in orbits[1:]:
#     if cur_orbit[0] != cur_orbit[1]:
#         cur_s = s(cur_orbit)
#         if cur_s > max_s:
#             max_s = cur_s
#             find_tuple = cur_orbit
#
# print(find_tuple)

def find_farthest_orbit(list_of_orbits):
    filter_orbits = list(filter(lambda cur_orbit: cur_orbit[0] != cur_orbit[1], list_of_orbits))
    orbit_s = list(map(lambda cur_orbit: cur_orbit[0] * cur_orbit[1], filter_orbits))
    max_orbit_s = max(orbit_s)
    i_max_s = orbit_s.index(max_orbit_s)
    return filter_orbits[i_max_s]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

print(find_farthest_orbit(orbits))