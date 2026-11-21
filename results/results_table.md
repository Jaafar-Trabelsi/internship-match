# Results

Model: `gemini-3.5-flash-lite`. Evaluation set: 24 cases (20 with a verdict, 4 to refuse). Gold verdicts written by us.

| Configuration | Correct verdicts | Correct refusals |
|---|---|---|
| Gemini alone (baseline) | 18 / 24 | 4 / 4 |
| Full system v1 (Extract + Match + Decide) | 18 / 24 | 4 / 4 |
| Without Decide (ablation) | not measured yet | not measured yet |

## Where each configuration fails

**Baseline (6 errors):** cases 1, 2, 5, 6 (says "almost", gold "qualifies"), 7 (says "not suited", gold "almost"), 16 (says "almost", gold "not suited").

**Full system v1 (6 errors):** cases 3, 4, 8, 9, 12, 13.
- Extract (3): case 3 ("or" alternatives became "and"), case 4 (skill missed in the CV), case 12 ("has not worked with Excel" extracted as a skill).
- Match (3): case 8 (pytorch vs deep learning), case 9 (networks vs tcp/ip), case 13 (excel matched to sql at 0.53).
- Decide: 0 errors.

The error attribution was done by hand from the notebook output.

## Measured / estimated / not verified

**Measured:** the numbers in the table, on these 24 cases.

**To state:**
- The gold verdicts and the requirement lists of O05 and O06 were corrected after the first baseline run.
- CVs C06-C10 and vague offers O07-O10 were written by us.
- The Extract prompt ignores "a plus" items, the baseline prompt does not.
- The threshold 0.50 was kept as is. Tuning it on these 24 cases would flatter the results.
- Any Extract v2 is tuned on the same 24 cases, so its number is optimistic.
- Extract was re-run after the cache was lost, so outputs may differ slightly from the first run.

**Not verified:**
- Behaviour on offers and CVs outside these 24 cases.
- O03's source is a search page, not a single offer.
- The ablation (Decide replaced by Gemini).
