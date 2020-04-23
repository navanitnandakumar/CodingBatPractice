# 👨‍💻 CodingBat-Practice 👨‍💻

This repo consists of all the programs that I did in https://codingbat.com

# Python

1.Warmup1 - Sleep_in : 
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.   sleep_in(False, False) → True sleep_in(True, False) → False sleep_in(False, True) → True

2.Warmup1 - Monkey_trouble :
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.   monkey_trouble(True, True) → True monkey_trouble(False, False) → True monkey_trouble(True, False) → False

3.Warmup1 - Sum_double :
Given two int values, return their sum. Unless the two values are the same, then return double their sum.   sum_double(1, 2) → 3 sum_double(3, 2) → 5 sum_double(2, 2) → 8

4.Warmup1 - diff_21 :
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.   diff21(19) → 2 diff21(10) → 11 diff21(21) → 0

5.Warmup1 - Parrot_trouble :
We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False

6.Warmup1 - Makes10 :
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True

7.Warmup1 - Near_hundred :
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False

8.Warmup1 - Pos_neg :
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.
pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True

9.Warmup1 - not_string :
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.
not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'

10.Warmup1 - Missing_char :
Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'

11.Warmup1 - front_back :
Given a string, return a new string where the first and last chars have been exchanged.
front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'

12.Warmup1 - front3 :
Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'

13.Warmup2 - String_times :
Given a string and a non-negative int n, return a larger string that is n copies of the original string.
string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'

14.Warmup2 - Front_times :
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'

15.Warmup2 - String_bits :
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'

16.Warmup2 - String_splosion :
Given a non-empty string like "Code" return a string like "CCoCodCode".
string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'

17.Warmup2 - last2 :
Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2

18.Warmup2 - Array_count9 :
Given an array of ints, return the number of 9's in the array.
array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3

19.Warmup2 - Array_front9 :
Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False

20.Warmup2 - Array123 :
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
