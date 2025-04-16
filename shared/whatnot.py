from collections import defaultdict

source_log = """100 1000 A
200 1100 A
200 1200 B
100 1200 B
100 1300 C
200 1400 A
300 1500 B
300 1550 B"""

log_lines = source_log.split("\n")

logs = []
for line in log_lines:
    parts = line.split(" ")
    log = {
        "user": parts[0],
        "time": int(parts[1]),
        "name": parts[2],
    }
    logs.append(log)


def time_field(item):
    return item["time"]


logs = sorted(logs, key=time_field)

user_paths = []

users = list(set([log["user"] for log in logs]))
users.sort()
for user in users:

    def user_field(item):
        return item["user"] == user

    user_logs = list(filter(user_field, logs))

    user_path = [user_log["name"] for user_log in user_logs]
    user_paths.append(user_path)

output_values = {}
tree = defaultdict()
longest_path = max(user_paths, key=len)
for index, _ in enumerate(user_paths):

    def get_nth_event(path):
        element = path[index]
        return element

    current_events = [get_nth_event(user_path) for user_path in user_paths]
    for current_event in current_events:
        tree[current_event] = tree[current_event] + 1
