# Data Dictionary

## `all_submissions_consolidated.csv`

One row per graded function/test, per submission. 17,385 rows, 215 students.

| Column | Type | Description |
|--------|------|-------------|
| `student_id` | string | Anonymized student ID (`student_0001`…`student_0215`); matches the `all_labs/` directory names. |
| `lab` | string | Lab identifier (`lab00`…`lab11`, `pre-labXX`). |
| `submission_timestamp` | string | Submission datetime (`YYYY-MM-DD-HH-MM-SS`); matches the submission directory name. |
| `exp_group` | int | Assigned condition group: `0` = no_feedback, `1` = tc, `2` = nl. Empty when unassigned. |
| `consented` | bool | Whether the student consented to research use (always `True` in this public set). |
| `age_18_plus` | bool | Whether the student reported being 18 or older. |
| `test_name` | string | Autograder test name. |
| `score` | float | Points earned on the test. |
| `max_score` | float | Maximum points for the test. |
| `status` | string | `passed` or `failed`. |
| `testcase_mask` | JSON array | Per-test-case pass(1)/fail(0) mask, when available. |
| `ai_feedback_type` | string | **Assigned** feedback condition: `tc`, `nl`, or `no_feedback`. |
| `ai_feedback_text` | string | Feedback **actually delivered** to the student (empty if none). Ground truth for delivery. |
| `source_file` | string | Submitted file the graded function came from. |
| `function_name` | string | Function evaluated (empty for whole-file problems). |
| `code_snippet` | string | The student's code for that function/file (anonymized). |
| `function_changed` | bool | Whether the function changed vs. the student's previous submission in the lab (empty on first submission). |

### Condition / delivery notes
- `ai_feedback_type` = assigned arm; `ai_feedback_text` = what was shown.
- Feedback is generated only on **failing** submissions, so a `tc`/`nl` row with
  empty `ai_feedback_text` simply means feedback was not triggered for that row.
- A `no_feedback` row never carries feedback text (verified: 0 exceptions).

## `all_labs/` per-submission files

```
all_labs/<lab>/<student_id>/<submission_timestamp>/
```

| File | Description |
|------|-------------|
| `*.py` (and similarly named code files) | The student's submitted source, with author/email/Spire-ID headers redacted. |
| `results.json` | Gradescope-style autograder output: per-test name, score, max_score, status, and `output` (which includes any delivered AI feedback after the `🤖 AI Feedback for you` marker). |
| `submission_metadata_pruned.json` | Submission metadata with all personal fields (`name`, `email`, `id`, `sid`, `sections`) redacted; `student_id` injected. |

## `surveys/entry_survey.csv`

Entry (pre-course) survey, consenting students only, keyed by `student_id`
(n = 182). Timestamp, email, name, and Spire ID removed.

| Column | Description |
|--------|-------------|
| `student_id` | Anonymized student ID (joins to `all_labs/` and the consolidated CSV). |
| `Age (in years)` | Self-reported age. |
| `Which best describes your gender identity?` | Self-reported gender identity. |
| `How many semesters have you been studying at UMass?` | Self-reported semesters enrolled (incl. current). |
| `How do you feel about your existing programming skill…` | Self-rated prior programming experience. |
| `How confident are you in solving mathematical problems?` | Self-rated math confidence (Likert). |
| `Which high school courses have you taken… related to computer programming?` | Free-text list of prior CS coursework. |

## `surveys/exit_survey.csv`

Exit (post-course) survey, consenting students only, keyed by `student_id`
(n = 37). Same PII columns removed.

| Column | Description |
|--------|-------------|
| `student_id` | Anonymized student ID. |
| `How many times have you encountered a generated feedback?` | Self-reported exposure to feedback. |
| `How helpful were the feedback?` | Perceived helpfulness (Likert). |
| `How much did you learn from the course because of the feedback?` | Perceived learning gain (Likert). |
| `Any comments on how we can improve the feedback?` | Free-text comments. |
