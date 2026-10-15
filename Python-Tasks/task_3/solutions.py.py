"""Task 3 - Python Coding & Problem-Solving: all 15 solutions."""


# Q1. Frequency of each word in a sentence
def word_frequency(sentence):
    freq = {}
    for word in sentence.split():
        freq[word] = freq.get(word, 0) + 1
    return freq


# Q2. Frequency of each character in a word
def char_frequency(word):
    freq = {}
    for ch in word:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


# Q3. First non-repeating character
def first_non_repeating(word):
    freq = char_frequency(word)
    for ch in word:
        if freq[ch] == 1:
            return ch
    return None


# Q4. Check whether two strings are anagrams
def are_anagrams(s1, s2):
    return char_frequency(s1) == char_frequency(s2)


# Q5. First repeating character (earliest second occurrence)
def first_repeating(text):
    seen = set()
    for ch in text:
        if ch in seen:
            return ch
        seen.add(ch)
    return None


# Q6. Move all zeros to the end, keeping order of non-zeros
def move_zeros(nums):
    non_zeros = [x for x in nums if x != 0]
    return non_zeros + [0] * (len(nums) - len(non_zeros))


# Q7. Second highest distinct number
def second_highest(nums):
    distinct = set(nums)
    if len(distinct) < 2:
        return None
    distinct.remove(max(distinct))
    return max(distinct)


# Q8. Remove duplicates preserving first-occurrence order
def remove_duplicates(nums):
    seen = set()
    result = []
    for x in nums:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


# Q9. Missing number from 1 to N
def missing_number(nums, n):
    return n * (n + 1) // 2 - sum(nums)


# Q10. First pair summing to target (second element found earliest)
def two_sum_pair(nums, target):
    for j in range(len(nums)):
        for i in range(j):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
    return []


# Q11. Number closest to zero (tie -> positive)
def closest_to_zero(nums):
    best = nums[0]
    for x in nums[1:]:
        if abs(x) < abs(best) or (abs(x) == abs(best) and x > best):
            best = x
    return best


# Q12. Common elements, unique, order of first list
def common_elements(list1, list2):
    in_second = set(list2)
    result = []
    for x in list1:
        if x in in_second and x not in result:
            result.append(x)
    return result


# Q13. Rotate list right by K positions
def rotate_right(nums, k):
    if not nums:
        return []
    k %= len(nums)
    if k == 0:
        return nums[:]
    return nums[-k:] + nums[:-k]


# Q14. Maximum sum of two consecutive elements
def max_consecutive_sum(nums):
    best = nums[0] + nums[1]
    for i in range(1, len(nums) - 1):
        best = max(best, nums[i] + nums[i + 1])
    return best


# Q15. All unique pairs summing to target
def all_pairs(nums, target):
    pairs = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.add(tuple(sorted((nums[i], nums[j]))))
    return [list(p) for p in sorted(pairs)]
