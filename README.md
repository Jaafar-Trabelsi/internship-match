# Internship Match

Does this student qualify for this internship? Input: a CV and the text of an offer. Output: a verdict (**qualifies / almost / not suited**), the list of missing requirements, or a **refusal** when the offer is too vague.

AI course project, 4th year, ESIN - UIR.
Team: **Jaafar Trabelsi** and **Mohammed El Habib Sefiani**.

## Pipeline (4 chained steps)

| Step | What it does | Model |
|---|---|---|
| 1. Extract | offer text -> list of requirements | Gemini (LLM) |
| 2. Match | requirements + CV skills -> similarity score per requirement | `paraphrase-multilingual-MiniLM-L12-v2` (embeddings, no LLM) |
| 3. Decide | score < 0.50 = missing; 0 missing = qualifies, 1 = almost, 2+ = not suited, no requirements = refuse | rule, no LLM |
| 4. Explain | verdict + missing items -> short answer | Gemini (LLM) |

Gemini is used through its API (`gemini-3.5-flash-lite`, free tier). We do not build a language model.

## The claim

For students looking for internships, the system gives the correct verdict on at least 7 out of 10 CV-offer pairs, names the missing requirements, and refuses when the offer gives too little information.

## Evaluation

- 24 CV-offer pairs in `data/eval_set.json`, gold verdicts written by us, including 4 vague offers to refuse.
- Baseline: Gemini alone on the raw CV and raw offer.
- Ablation: the full system without the Decide step (Gemini decides from the scores).
- Results: see `results/results_table.md`.

## Repository

```
data/       offers.json (10 offers), cvs.json (10 synthetic CVs), eval_set.json (24 cases)
notebook/   internship_match.ipynb  (the system + baseline + ablation)
results/    results_table.md, baseline_results.csv, full_system_results.csv,
            full_system_v1_rerun_results.csv, full_system_v2_results.csv, ablation_results.csv
docs/       project documents, charter (annex_A_charter.docx), final report
slides/     presentation (optional)
```

## How to run (Google Colab)

1. Open `notebook/internship_match.ipynb` in Colab.
2. Add your Gemini API key in Colab **Secrets** under the name `GEMINI_API_KEY`, with notebook access on. Never commit the key.
3. Run the notebook from the top, cell by cell (not "Run all"). The notebook clones this repo to get the data.
4. Every Gemini call is cached in `gemini_cache.json` (not committed). A re-run costs no quota. Download the cache before closing the session.

Free tier: about 15 requests per minute. A full run of Extract v2 + the ablation is around 50 real calls (about 13 s each).

## Demo (10 min, live in the notebook)

1. A covered case: the system lists the requirements and says "qualifies".
2. A case picked by the jury from `data/eval_set.json`, run live.
3. A vague offer: the system refuses instead of guessing.

## Data

- 6 public IT internship offers, summarised by hand (source URL in `data/offers.json`), plus 4 vague offers written by us.
- 10 synthetic CVs written by us. No real personal data.

## Status

Measured on 24 cases: baseline 18/24, full system v2 18/24, ablation 21/24. Report in progress. See `results/results_table.md` for all numbers, the failed cases and the limits of the evaluation.