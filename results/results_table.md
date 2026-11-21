# Results table

Filled with real measured numbers only (see `baseline_results.csv`).

| Configuration | Correct verdicts | Correct refusals |
|---|---:|---:|
| Gemini alone (baseline) | 18/24 | 4/4 |
| Full system | Not measured yet | Not measured yet |
| Without Decide (ablation) | Not measured yet | Not measured yet |

## Notes

- **Baseline source**: `results/baseline_results.csv` (24 cases, old gold labels). Wrong verdicts recorded in that file: cases 1, 2, 5, 6, 7, 16.
- **Data consistency fixes applied** (Habib, to be validated with Jaafar): `O05` now includes `python`; `O06` note clarified; CV skill tokens normalized (`databases`, `frontend_framework`, `backend`) where supported by CV text; eval case 7 gold updated to `not suited [python, powerbi]`. An internal consistency audit now reports **24/24** cases consistent.
- **Baseline caveat**: `baseline_results.csv` was not rewritten (measured artifact). Under the updated gold labels, case 7 would become correct, so rerunning/evaluating baseline against the updated eval set would give **19/24** verdicts and **4/4** refusals. Re-run baseline to confirm before reporting.
- **Full system / ablation**: fill only after real notebook runs on the same frozen `data/eval_set.json`.
