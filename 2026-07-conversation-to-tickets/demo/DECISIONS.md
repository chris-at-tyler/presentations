# Campsite Waitlist — Shared Understanding

Output of the grilling session from Part 1 ("Finding Your Unknowns"). Every
decision below was put to the product owner and settled — nothing here is
assumed.

## The feature

When a campsite is fully booked for a date range, visitors can join a
waitlist. When a reservation is cancelled, the waitlist fills the freed spot.

## Settled decisions

- **Ordering:** strict FIFO. One person notified at a time — never a blast to
  the whole list (first-click races produce angry campers).
- **Hold window:** the notified person has **4 hours flat** to claim before
  the offer moves to the next in line. No business-hours logic in v1.
- **Date matching:** **exact date-range match only** for v1. Partial-overlap
  matching (splitting stays) is explicitly backlogged.
- **Payment:** none at claim time. In this park system **campers pay at
  check-in** — a domain rule, not an oversight. Claiming converts the freed
  spot into a normal unpaid reservation.
- **Notification channel:** email, containing a claim link. The link expires
  when the hold window does.
- **Access:** an account is required to join a waitlist. Max **3 active
  waitlist entries** per user (anti-scalping).
- **Season close:** open waitlist entries for dates past the site's season
  close are expired nightly.

## Context

Greenfield: the reservations system exists; the waitlist service, its
storage, API, and notification flow are all new. Web only for v1 — no mobile
app changes. Payments code is untouched (see payment decision above).
