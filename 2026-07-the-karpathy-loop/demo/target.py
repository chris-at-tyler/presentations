"""Event-log analytics — the demo's train.py. THIS is the file the agent edits.

process(events) takes a list of (user_id, session_id, day, action) tuples and
returns a dict with:
  top_users:       top 10 (user, count) pairs, count desc, then user asc
  unique_sessions: number of distinct session ids
  daily_counts:    {day: event count}
  power_users:     sorted user ids with >= 100 events

Everything is fair game as long as bench.py reports correct: True.
"""


def process(events):
    # find the distinct users
    users = []
    for e in events:
        if e[0] not in users:
            users.append(e[0])

    # count events per user
    user_counts = []
    for u in users:
        count = 0
        for e in events:
            if e[0] == u:
                count += 1
        user_counts.append((u, count))

    # pick the top 10 users by count (ties broken by user id)
    top_users = []
    remaining = list(user_counts)
    for _ in range(10):
        best = None
        for uc in remaining:
            if best is None or uc[1] > best[1] or (uc[1] == best[1] and uc[0] < best[0]):
                best = uc
        top_users.append(best)
        remaining.remove(best)

    # count the distinct sessions
    sessions = []
    for e in events:
        if e[1] not in sessions:
            sessions.append(e[1])
    unique_sessions = len(sessions)

    # events per day
    daily_counts = {}
    for e in events:
        if e[2] in daily_counts:
            daily_counts[e[2]] = daily_counts[e[2]] + 1
        else:
            daily_counts[e[2]] = 1

    # users with at least 100 events
    power_users = []
    for (u, c) in user_counts:
        if c >= 100:
            power_users.append(u)
    power_users.sort()

    return {
        "top_users": top_users,
        "unique_sessions": unique_sessions,
        "daily_counts": daily_counts,
        "power_users": power_users,
    }
