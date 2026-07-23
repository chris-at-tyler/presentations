# Feature Plan: Campsite Waitlist

## Goal

When a campsite is fully booked for a date range, visitors can join a waitlist.
If a reservation is cancelled, we notify the waitlist so the spot gets filled
instead of sitting empty.

## Approach

- Add a `waitlist_entries` table: `site_id`, `user_id`, `date_range`, `created_at`
- Show a **Join Waitlist** button on the site detail page when the site is sold out
- When a reservation is cancelled, notify the first person on the waitlist by email
- The email contains a link they can use to claim the spot

## Out of scope

- Payment flow changes
- Mobile app (web only for v1)
