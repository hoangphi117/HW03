# SUS Questionnaire (System Usability Scale)

**Standard 10-item Likert scale (1 = Strongly Disagree → 5 = Strongly Agree)**

After the participant completes the task, hand them this form or share the
digital version. Instruct: "Hãy trả lời 10 câu sau dựa trên trải nghiệm vừa
rồi của bạn. Không có câu trả lời đúng hay sai."

---

| No. | Statement (English) | Câu hỏi (Tiếng Việt) | 1 | 2 | 3 | 4 | 5 |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---:|
| 1 | I think that I would like to use this system frequently. | Tôi nghĩ tôi muốn sử dụng hệ thống này thường xuyên. | | | | | |
| 2 | I found the system unnecessarily complex. | Tôi thấy hệ thống này phức tạp không cần thiết. | | | | | |
| 3 | I thought the system was easy to use. | Tôi thấy hệ thống này dễ sử dụng. | | | | | |
| 4 | I think that I would need the support of a technical person to use this system. | Tôi nghĩ mình cần hỗ trợ kỹ thuật để sử dụng hệ thống này. | | | | | |
| 5 | I found the various functions in this system were well integrated. | Tôi thấy các chức năng trong hệ thống được tích hợp tốt. | | | | | |
| 6 | I thought there was too much inconsistency in this system. | Tôi thấy hệ thống này có quá nhiều sự mâu thuẫn. | | | | | |
| 7 | I would imagine that most people would learn to use this system very quickly. | Tôi nghĩ hầu hết mọi người sẽ học cách dùng hệ thống này rất nhanh. | | | | | |
| 8 | I found the system very cumbersome to use. | Tôi thấy hệ thống này rất bất tiện khi sử dụng. | | | | | |
| 9 | I felt very confident using the system. | Tôi cảm thấy rất tự tin khi sử dụng hệ thống. | | | | | |
| 10 | I needed to learn a lot of things before I could get going with this system. | Tôi phải học nhiều thứ trước khi có thể sử dụng được hệ thống này. | | | | | |

---

## Scoring Formula

```
For ODD-numbered questions  (1, 3, 5, 7, 9): contribution = raw_score - 1
For EVEN-numbered questions (2, 4, 6, 8, 10): contribution = 5 - raw_score

SUS Score = sum_of_contributions × 2.5
```

**Range: 0 – 100**

| Score Range | Adjective Rating | Grade |
|:---:|:---:|:---:|
| ≥ 85.5 | Excellent | A |
| 72.5 – 85.4 | Good | B |
| 52.5 – 72.4 | OK | C |
| 38.0 – 52.4 | Poor | D |
| < 38.0 | Awful | F |

---

## Spreadsheet Formula (Excel / Google Sheets)

Assuming raw scores are in columns B2:K2 (Q1 to Q10):

```excel
=((B2-1)+(5-C2)+(D2-1)+(5-E2)+(F2-1)+(5-G2)+(H2-1)+(5-I2)+(J2-1)+(5-K2))*2.5
```

