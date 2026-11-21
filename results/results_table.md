# Results

Model: `gemini-3.5-flash-lite`. Evaluation set: 24 cases (20 with a verdict, 4 to refuse). Gold verdicts written by us. All numbers measured, one run each unless stated.

| Configuration | Correct verdicts | Correct refusals |
|---|---|---|
| Gemini alone (baseline) | 18 / 24 | 4 / 4 |
| Full system v1, run 1 | 18 / 24 | 4 / 4 |
| Full system v1, run 2 (same code, Extract re-run) | 16 / 24 | 4 / 4 |
| Full system v2 (Extract v2 + Match + Decide) | 18 / 24 | 4 / 4 |
| Without Decide (ablation, on v2) | 21 / 24 | 4 / 4 |

On the 20 cases with a verdict: baseline 14/20, v2 14/20, ablation 17/20.

## Where each configuration fails

**Baseline (6 errors):** cases 1, 2, 5, 6 (says "almost", gold "qualifies"), 7 (says "not suited", gold "almost"), 16 (says "almost", gold "not suited").

**Full system v1, run 1 (6 errors):** cases 3, 4, 8, 9, 12, 13. By hand: Extract 3 (case 3 "or" became "and"; case 4 REST APIs missed in the CV; case 12 "has not worked with Excel" extracted as a skill), Match 3 (case 8 pytorch vs deep learning; case 9 networks vs tcp/ip; case 13 excel matched to sql at 0.53).

**Full system v1, run 2 (8 errors):** cases 3, 4, 6, 7, 8, 9, 12, 13. Gemini's Extract changed between runs (O04 gained "infrastructure as code" and "automation", O05 gained python and sql), so cases 6 and 7 became wrong. Extract is non-deterministic: about 2 cases of variation.

**Full system v2 (6 errors):** cases 8, 9, 10, 12, 13, 14. All six are Match errors (scores from the notebook):
- 8: deep learning -> machine learning 0.68 (false match)
- 9: networks -> cybersecurity 0.43 (false miss)
- 10: next.js -> javascript 0.51 (false match)
- 12 and 13: excel -> sql 0.53 (false match)
- 14: javascript -> html 0.63 and react/angular/vue.js -> java 0.61 (false matches)
Extract errors: 0. Decide errors: 0. v2 fixed cases 3, 4, 6, 7 compared with v1 run 2.

**Without Decide (3 errors):** cases 9, 13, 14. Gemini, given the scores, corrected cases 8, 10 and 12.

**Explain (checked on 3 cases only: 1, 10, 21):** case 1 and the fixed refusal sentence are fine. Case 10 repeats the wrong Match result ("qualifies", gold "almost").

## What the figures say

- The fixed threshold 0.50 did not help on this set: the ablation, where Gemini decides from the scores, is 3 cases better than the rule (21 vs 18).
- v2 equals the baseline (18/24). The value of the pipeline here is the error analysis: all remaining v2 errors come from the embedding Match step.
- The difference of 3 cases is of the same order as the run-to-run variation we saw in Extract (18 vs 16), so it is not a strong result.

## Measured / estimated / not verified

**Measured:** the numbers in the table, on these 24 cases, model gemini-3.5-flash-lite.

**To state:**
- The gold verdicts and the requirement lists of O05 and O06 were corrected after the first baseline run.
- Cases 2, 3, 7 and 11 have gold verdicts based on judgment (databases covered by SQL; "or" alternatives), not on exact name matching. Habib must confirm them.
- CVs C06-C10 and vague offers O07-O10 were written by us.
- The Extract prompt ignores "a plus" items, the baseline prompt does not.
- The Extract v2 prompts were written after seeing the v1 failures on the same 24 cases, so v2 and the ablation are optimistic.
- Extract is non-deterministic (18 vs 16). The cache was lost once and Extract re-run.
- The threshold 0.50 was kept as is. Tuning it on these 24 cases would flatter the results.
- Error attribution (Extract / Match / Decide) was done by hand.
- The ablation was run on v2 only. Gemini sees the scores and the verdict definitions (including the counting), but not the 0.50 threshold.
- One run per configuration, except v1 (two runs).

**Not verified:**
- Behaviour on offers and CVs outside these 24 cases.
- O03's source is a search page, not a single offer.
- Whether the Explain text is correct beyond the 3 demo cases.