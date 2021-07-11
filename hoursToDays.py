intervals = (
    ('years', 8760),  # 24 * 365
    ('months', 720),  # 24 * 30
    ('weeks', 168),  # 24 * 7
    ('hours', 1)
)


def display_time(hours, granularity=2):
    result = []

    for name, count in intervals:
        value = hours // count
        if value:
            hours -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result)


hours = int(input("Introduzca las horas: "))
times = display_time(hours, 2)
print(times)
