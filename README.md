# ProgFeed Dataset — LLM-generated Feedback in Introductory Programming

This repository accompanies the paper *"A Classroom Study of LLM-generated
Feedback Intervention in Introductory Programming"* (ProgFeed). It contains the
de-identified student programming submissions and a consolidated analysis table
from a classroom study run in an introductory CS course (CS110), Fall 2025.

## What's here

| Path | Description |
|------|-------------|
| `all_labs/` | Per-submission student code and autograder results, organized by lab and anonymized student ID. |
| `all_submissions_consolidated.csv` | One row per graded function/test per submission, with the assigned feedback condition and the feedback actually delivered. |
| `autograders/` | Per-lab autograder code: tests, feedback-generation logic, LLM prompts, problem descriptions (`*_desc.txt`), and example submissions. |
| `DATA_DICTIONARY.md` | Field-level documentation for the CSV and the per-submission files. |
| `LICENSE` | CC BY 4.0. |

The `autograders/` directory documents how submissions were graded and how the
test-case / natural-language feedback was generated (`feedback_generation.py`,
`openaiprompt*` files). Problem statements are included as `*_desc.txt`. All
personal data has been removed: consent records, submission metadata, deployment
scripts/tokens, and build artifacts are excluded, and any names/emails/Spire IDs
in code or example submissions are redacted. The feedback code reads the LLM API
key from the `OPENAI_API_KEY` environment variable (no keys are included).

## Study design (brief)

Students submitted lab assignments to an autograder. On a failing submission, the
autograder could attach LLM-generated feedback. Three conditions:

- **`tc`** — test-case feedback (a failing input + expected output)
- **`nl`** — natural-language feedback (an explanation of the error)
- **`no_feedback`** — control (autograder result only)

Condition assignment varied by lab:

- **lab02** — `tc` for all submissions
- **lab03** — `nl` for all submissions
- **lab05, lab06, lab07, lab09** — randomized per the lab's own assignment (0 = no_feedback, 1 = tc, 2 = nl)
- **all other labs** (lab00, lab01, lab10, lab11, pre-labs) — `no_feedback`

## Important caveats

- **Feedback delivery vs. assignment.** `ai_feedback_type` is the *assigned*
  condition; `ai_feedback_text` is what was *actually delivered*. Feedback is only
  generated on a **failing** submission, so most rows in `tc`/`nl` conditions have
  no feedback text (the student passed, or the attempt did not trigger generation).
  **Use `ai_feedback_text` (non-empty) as the ground truth for whether feedback was
  shown.**
- **lab10 and lab11 delivered zero feedback.** The lab10 autograder shipped without
  the feedback-generation code, and lab11 was not an intervention lab. Both are
  labeled `no_feedback`. Do not treat them as intervention labs.
- **Consenters only.** Only data from students who consented to research use is
  included. Non-consenting students, instructors, and TAs are excluded.

## Anonymization

- Student emails replaced with stable `student_XXXX` IDs.
- Names, emails, and Spire IDs removed from code headers, metadata, and all text.
- Submission metadata fields (name/email/id/sid/sections) redacted.
- The repository was scanned to confirm zero remaining emails, names, or Spire IDs.

## Citation

If you use this dataset, please cite the ProgFeed paper. A full citation will be
added here on publication.

## License

[CC BY 4.0](LICENSE) — free to share and adapt with attribution.
