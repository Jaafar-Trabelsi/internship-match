# Limits and honesty (Habib - Block 5 draft)

## Limits of the evaluation set

- **Small size**: 24 CV-offer pairs only; not enough to claim general performance across all internship domains.
- **Synthetic CVs**: CVs were written by us, not collected from real students. They are cleaner and shorter than real CVs.
- **Simplified offers**: offers are short summaries/copies and do not cover the full diversity of real postings (languages, seniority, soft skills, location constraints, legal requirements).
- **Narrow domain**: mostly IT internships with a small set of explicit skills; results do not transfer to non-IT fields.
- **Labeling convention sensitivity**: verdicts depend on requirement conventions (e.g., O05/O06). Small convention changes can change gold labels.
- **No inter-annotator process recorded**: verdicts were written by the team, but the repo does not yet document a formal disagreement-resolution process.
- **No statistical confidence**: with 24 cases, differences between configurations should be interpreted cautiously.

## Measured / Estimated / Not verified

### Measured

- Gemini alone (baseline) on 24 cases in `results/baseline_results.csv`: **18/24 correct verdicts**, **4/4 correct refusals**.
- Wrong baseline cases: 1, 2, 5, 6, 7, 16.

### Estimated

- The claim target "at least 7 out of 10 CV-offer pairs" is plausible for the full system, but **not measured yet** in this repo.
- The Decide rule/ablation impact is expected to matter on borderline cases, but **not measured yet**.

### Not verified

- Full system performance (Extract + Match + Decide + Explain) on the same eval set.
- Ablation performance without the Decide step.
- Whether the system correctly names missing requirements in its generated explanations (only verdict/refusal correctness is recorded in the baseline CSV).
- Robustness to noisier real CVs, longer offers, multilingual offers, or ambiguous requirements.
- End-to-end reproducibility from an empty runtime with cached/non-cached Gemini calls (to be verified before defence).

## Reporting note

Any number added to the report or demo must come from a real run saved in `results/`. Do not fill the full-system/ablation cells until measured.
