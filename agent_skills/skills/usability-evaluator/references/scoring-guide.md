# Scoring Guide — SUS & UEQ-S

## SUS Scoring (System Usability Scale)

### Individual Score Formula

```
score_q_odd  = raw - 1          (questions 1, 3, 5, 7, 9)
score_q_even = 5 - raw          (questions 2, 4, 6, 8, 10)
SUS_score    = sum(scores) × 2.5
```

### Group Summary Table Template

| Participant | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 | SUS |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| P-01 | | | | | | | | | | | |
| P-02 | | | | | | | | | | | |
| P-03 | | | | | | | | | | | |
| P-04 | | | | | | | | | | | |
| P-05 | | | | | | | | | | | |
| P-06 | | | | | | | | | | | |
| P-07 | | | | | | | | | | | |
| **Mean** | | | | | | | | | | | **??.?** |
| **Std Dev** | | | | | | | | | | | **??.?** |
| **Min** | | | | | | | | | | | **??.?** |
| **Max** | | | | | | | | | | | **??.?** |

### Interpretation

| Mean SUS | Adjective | Percentile (approx) | Recommendation |
|:---:|:---:|:---:|:---|
| ≥ 85.5 | Excellent | Top 10% | Maintain; minor improvements only |
| 72.5–85.4 | Good | Top 25% | Address high-severity issues |
| 52.5–72.4 | OK | Above avg | Prioritize top 3 pain points |
| 38–52.4 | Poor | Below avg | Redesign key flows |
| < 38 | Awful | Bottom 15% | Major UX overhaul needed |

---

## UEQ-S Scoring (User Experience Questionnaire Short)

### 8 Bi-polar Items (1–7 Likert scale)

Recode: `transformed = raw - 4`  → range: −3 (negative) to +3 (positive)

| Item | Negative Pole | Positive Pole | Dimension |
|:---:|:---|:---|:---:|
| 1 | Obstructive | Supportive | PQ |
| 2 | Complicated | Easy | PQ |
| 3 | Inefficient | Efficient | PQ |
| 4 | Confusing | Clear | PQ |
| 5 | Boring | Exciting | HQ |
| 6 | Not interesting | Interesting | HQ |
| 7 | Conventional | Inventive | HQ |
| 8 | Usual | Leading edge | HQ |

### Dimension Scores

```
PQ (Pragmatic Quality) = mean of items 1–4 (transformed)
HQ (Hedonic Quality)   = mean of items 5–8 (transformed)
Overall UX             = mean(PQ, HQ)
```

### Benchmarks (from UEQ dataset, N = 468 products)

| Score | Benchmark |
|:---:|:---|
| > 1.5 | Excellent |
| 0.8 – 1.5 | Good |
| 0.5 – 0.8 | Above average |
| -0.5 – 0.5 | Average |
| < -0.5 | Below average |

