# Task 2: Python String, List & Dictionary Practice

A Jupyter/Google Colab notebook with 20 beginner-level Python problems. Every solution is written with plain loops, conditionals and basic built-ins (no external libraries), to practise core logic on strings, lists and dictionaries.

## Contents

| File | Description |
|------|-------------|
| `task-2.ipynb` | Notebook with solutions to Q1–Q20 |

## Problems and Expected Output

| # | Problem | Sample input | Output |
|---|---------|--------------|--------|
| Q1 | Shortest word in a sentence | `"Python makes coding easy"` | `easy` |
| Q2 | Largest number in a list | `[12, 45, 7, 89, 23]` | `89` |
| Q3 | Smallest number in a list (loop, then `min()`/`max()` check) | `[12, 45, 7, 89, 23]` | `7` (and `7`, `89`) |
| Q4 | First longest word when ties occur | `"Python makes coding useful"` | `Python` |
| Q5 | Word with the most characters | `"Data engineering requires problem solving"` | `engineering` |
| Q6 | Count vowels | `"Education"` | `5` |
| Q7 | Count consonants | `"Python 123!"` | `5` |
| Q8 | Most frequent character | `"banana"` | `a` |
| Q9 | Least frequent character | `"success"` | `u` |
| Q10 | Characters appearing more than once | `"programming"` | `['r', 'g', 'm']` |
| Q11 | Dict: word → first character | `"python data engineering"` | `{'python': 'p', 'data': 'd', 'engineering': 'e'}` |
| Q12 | Dict: word → last character | `"python data engineering"` | `{'python': 'n', 'data': 'a', 'engineering': 'g'}` |
| Q13 | Dict: word → uppercase | `"data science python"` | `{'data': 'DATA', 'science': 'SCIENCE', 'python': 'PYTHON'}` |
| Q14 | Dict: number → square | `[2, 3, 4, 5]` | `{2: 4, 3: 9, 4: 16, 5: 25}` |
| Q15 | Dict: number → Even/Odd | `[1, 2, 3, 4, 5]` | `{1: 'Odd', 2: 'Even', 3: 'Odd', 4: 'Even', 5: 'Odd'}` |
| Q16 | Most frequent word | `"Python is easy and python powerful"` | `python` |
| Q17 | Words appearing more than once | `"data science uses data and science tools"` | `data`, `science`, `data`, `science` (one per line) |
| Q18 | First word that appears only once | `"apple banana apple mango banana orange"` | `mango` |
| Q19 | Count words longer than 4 characters | `"Python makes problem solving interesting"` | `5` |
| Q20 | Longest word that appears only once | `"Python makes coding useful Python"` | `coding` |

## Concepts Practised

- String splitting and iteration (`split()`, `lower()`, `upper()`, indexing with `[0]` and `[-1]`)
- Finding min/max with loops, and with `min()` / `max()`
- Counting with `count()` and manual counters
- Building dictionaries in loops
- Conditionals, `break`, and nested loops

## Requirements

- Python 3.8+
- Jupyter Notebook, JupyterLab, VS Code, or Google Colab
- No third-party packages

## How to Run

**Google Colab:** upload `task-2.ipynb` at [colab.research.google.com](https://colab.research.google.com) and choose *Runtime → Run all*.

**Locally:**

```bash
pip install notebook
jupyter notebook task-2.ipynb
```

Then choose *Kernel → Restart & Run All*. Each cell is independent, so cells can also be run individually.

## Known Issues / Suggested Improvements

The outputs above are what the notebook currently produces. A few cells give the right answer only for the sample input, and would fail on other data:

- **Q4**: `longest = words` assigns the whole list instead of `word`. It prints `Python` only because no word is strictly longer than the first one.
- **Q5**: the condition compares `len(words)` (the number of words) instead of `len(word)`. It works for the sample by coincidence.
- **Q8**: it recounts but never tracks the highest count, so it just prints the *last* character. `banana` happens to end in `a`.
- **Q9**: it prints the first character that appears once, which is not necessarily the *least* frequent one.
- **Q16**: it prints the first word that repeats, not the word with the highest count.
- **Q17**: duplicates are printed once per occurrence; track seen words to print each once.
- **Q18**: the line `v = "apple banana apple mango banana orange"` is duplicated.
- **Q3**: the extra unlabelled cell after it (using `min()` / `max()`) has no question heading.
