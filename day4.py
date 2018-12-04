import sys
import re

extract_re = re.compile(r"\[(\d{4}\-\d{2}\-\d{2} \d{2}:(\d{2}))\] (\D+) #?(\d*)")
id_re = re.compile("#(\d+).*")


def get_data(line):
    match = extract_re.match(line)
    return match.groups()


def main(filename):
    lines = []
    with open(filename, "r") as fp:
        for line in fp:
            time, minutes, event, guard_id = get_data(line)
            lines.append((time, minutes, event, guard_id))
    sorted_lines = sorted(lines, key=lambda x: x[0])
    guards = {}
    sleep_time = 0
    wake_time = 0
    current_guard = None
    for item in sorted_lines:
        time, minutes, event, guard_id = item
        if event == "Guard":
            current_guard = guard_id
            if current_guard not in guards:
                guards[current_guard] = [0] * 60
        elif event == "falls":
            sleep_time = int(minutes)
        else:
            wake_time = int(minutes)
            for hour in range(sleep_time, wake_time):
                guards[current_guard][hour] += 1

    max_sleep = 0
    minute_count = 0
    sleepiest_guard = None
    sleepiest_minute = None
    sleepiest_minute_guard = None
    for guard, sleep_times in guards.items():
        for minute, count in enumerate(sleep_times):
            if count > minute_count:
                minute_count = count
                sleepiest_minute = minute
                sleepiest_minute_guard = guard
        total_time = sum(sleep_times)
        if total_time > max_sleep:
            sleepiest_guard = guard
            max_sleep = total_time

    times = guards[sleepiest_guard]
    sleepiest_hour = times.index(max(times))
    print(
        "part 1",
        "guard",
        sleepiest_guard,
        "hour",
        sleepiest_hour,
        "multiple",
        int(sleepiest_guard) * sleepiest_hour,
    )

    print(
        "part2",
        "guard",
        sleepiest_minute_guard,
        "minute",
        sleepiest_minute,
        "multiple",
        int(sleepiest_minute_guard) * int(sleepiest_minute),
    )


if __name__ == "__main__":
    main(sys.argv[1])
