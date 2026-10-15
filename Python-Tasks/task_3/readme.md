# Task 3 – Python Coding & Problem-Solving

Solutions to 15 Python problems on strings, lists and dictionaries, written as reusable functions and tested in a script and a Jupyter notebook.

## Folder Structure

```
YourName_Task3_Python/
├── solutions.py            # 15 solution functions (Q1–Q15)
├── main.py                 # imports the functions and runs test cases
└── problem_solving.ipynb   # pseudocode, code, expected output, extra tests
```

## Requirements

- Python 3.8 or later
- Visual Studio Code (with the Python and Jupyter extensions for the notebook)

No third-party libraries are needed to run `solutions.py` or `main.py`.

## How to Run

**Script (VS Code terminal):**

```bash
python main.py
```

Each question prints the given example (`Q1`) and one extra test (`Q1b`).

**Notebook:** open `problem_solving.ipynb` in VS Code, select a Python kernel, and choose **Run All**.

## Questions Covered

| Q  | Function               | Task                                              |
|----|------------------------|---------------------------------------------------|
| 1  | `word_frequency`       | Frequency of each word in a sentence              |
| 2  | `char_frequency`       | Frequency of each character in a word             |
| 3  | `first_non_repeating`  | First non-repeating character                     |
| 4  | `are_anagrams`         | Check whether two strings are anagrams            |
| 5  | `first_repeating`      | First repeating character                         |
| 6  | `move_zeros`           | Move all zeros to the end of a list               |
| 7  | `second_highest`       | Second highest distinct number                    |
| 8  | `remove_duplicates`    | Remove duplicates, keeping original order         |
| 9  | `missing_number`       | Missing number from 1 to N                        |
| 10 | `two_sum_pair`         | First pair whose sum equals a target              |
| 11 | `closest_to_zero`      | Number closest to zero (positive wins ties)       |
| 12 | `common_elements`      | Common elements of two lists                      |
| 13 | `rotate_right`         | Rotate a list right by K positions                |
| 14 | `max_consecutive_sum`  | Maximum sum of two consecutive elements           |
| 15 | `all_pairs`            | All unique pairs whose sum equals a target        |

## Approach Notes

- **Q1–Q5:** dictionaries and sets give counts and "seen" checks in a single pass.
- **Q6–Q8, Q12:** order is preserved by scanning left to right and using a set for membership.
- **Q9:** the missing number is the sum of 1..N, `N(N+1)/2`, minus the sum of the list.
- **Q10:** scans left to right and returns the pair whose second element appears earliest.
- **Q11:** compares absolute values and returns the positive number on a tie.
- **Q13:** uses `K % len(list)`, so K larger than the list length works.
- **Q15:** stores each pair sorted in a set to remove duplicates, then returns the pairs sorted by first element.

## Edge Cases Handled

- No valid answer returns `None` (Q3, Q5, Q7) or `[]` (Q10, Q15).
- Empty list and `K = 0` in Q13.
- Repeated values forming a pair, such as `[3, 3, 3]` with target 6 in Q15.

## Submission

Compress the folder into `Task3_Python.zip` and upload it through the LMS.
