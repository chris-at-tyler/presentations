"""Fixed benchmark harness — the demo's prepare.py. DO NOT MODIFY.

Builds a deterministic event-log workload, verifies target.process() against
a reference implementation (so the metric can't be gamed), then times it.

Run:  python3 bench.py
Key output lines:  bench_ms: <float>   correct: <bool>
"""

import random
import time
from collections import Counter

import target

# ── Fixed workload ──────────────────────────────────────────────────────────
N_EVENTS = 12_000
N_USERS = 250
N_SESSIONS = 1_500
N_DAYS = 30
ACTIONS = ["view", "click", "search", "book", "cancel", "review"]
REPS = 3


def build_events():
    rng = random.Random(42)
    # zipf-ish user popularity so top_users is meaningful
    weights = [1.0 / (i + 1) ** 0.7 for i in range(N_USERS)]
    users = [f"user{i:04d}" for i in range(N_USERS)]
    events = []
    for _ in range(N_EVENTS):
        u = rng.choices(users, weights=weights, k=1)[0]
        s = f"sess{rng.randrange(N_SESSIONS):05d}"
        d = f"2026-06-{rng.randrange(1, N_DAYS + 1):02d}"
        a = rng.choice(ACTIONS)
        events.append((u, s, d, a))
    return events


def reference(events):
    """Straightforward correct implementation — ground truth, not fast."""
    counts = Counter(e[0] for e in events)
    top_users = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:10]
    unique_sessions = len({e[1] for e in events})
    daily_counts = dict(Counter(e[2] for e in events))
    power_users = sorted(u for u, c in counts.items() if c >= 100)
    return {
        "top_users": top_users,
        "unique_sessions": unique_sessions,
        "daily_counts": daily_counts,
        "power_users": power_users,
    }


def normalize(result):
    return (
        [tuple(x) for x in result["top_users"]],
        result["unique_sessions"],
        dict(result["daily_counts"]),
        list(result["power_users"]),
    )


def main():
    events = build_events()
    expected = normalize(reference(events))

    got = normalize(target.process(list(events)))
    correct = got == expected

    best = float("inf")
    if correct:
        for _ in range(REPS):
            t0 = time.perf_counter()
            target.process(list(events))
            best = min(best, (time.perf_counter() - t0) * 1000)

    print("---")
    print(f"bench_ms: {best:.3f}" if correct else "bench_ms: 0.000")
    print(f"correct: {correct}")
    print(f"n_events: {len(events)}")
    print(f"reps: {REPS}")


if __name__ == "__main__":
    main()
