# wholesale-ap-cash-forecasting

Turns a wholesale vendor's open invoice schedule into a real, forward-looking cash-need calendar — how much has to be in the bank, and by when, to cover every outstanding order — built for and used in production at a seasonal retail business I run the finance/ops function for.

## The problem

The business orders inventory from a wholesale marketplace on net terms. The marketplace's own dashboard shows a running total owed, but no reliable per-order charge date. An earlier internal tracker just estimated every due date as "order date + 60 days" — a guess that turned out to be wrong on a large share of real orders. Actual charge dates ranged anywhere from 60 to 119+ days out, depending on ship date and the vendor's own billing cycle. The gap wasn't cosmetic: it produced false "overdue" alarms that didn't match the vendor's actual records, which is worse than no forecast at all if it teaches you to ignore the warnings.

## What it does

Once each order's real charge date is available, this script rolls every outstanding obligation into a daily and weekly cash-need calendar, with a running cumulative reserve total so it's clear not just what's due this week, but how much needs to be set aside in total to stay covered through the rest of the season. Orders with no fixed charge date — some are billed automatically to a card with no date shown anywhere — are never assigned a guessed date; they're carried separately as a standing reserve on top of the dated schedule, because a guessed date is exactly the mistake this tool exists to fix. Current operating cash is read live from the business's own ledger export, not hand-entered, so the forecast reflects where the account actually stands.

## My role

I identified that the "order date + 60 days" assumption was producing false alarms by checking it against the vendor's real per-order data, specified the daily/weekly/undated-reserve structure this script builds, and directed the AI-assisted implementation — then used it myself to plan real cash needs for a real ordering season.

## Stack

Python, openpyxl (reads the live operating ledger), json (vendor schedule export). generate_sample_ledger.py builds a synthetic ledger so the script runs standalone with no real business data.

Business name and dollar figures have been genericized for this public repo. Logic and structure are unchanged from what runs in production.
