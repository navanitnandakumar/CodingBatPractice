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

21.Warmup2 - String_match :
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0

22.String1 - Hello_name :
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'

23.String1 - Make_abba :
Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
make_abba('Hi', 'Bye') → 'HiByeByeHi'
make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
make_abba('What', 'Up') → 'WhatUpUpWhat'

24.String1 - Make_tags :
The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
make_tags('i', 'Yay') → '<i>Yay</i>'
make_tags('i', 'Hello') → '<i>Hello</i>'
make_tags('cite', 'Yay') → '<cite>Yay</cite>'

25.String1 - Make_out_word :
Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".
make_out_word('<<>>', 'Yay') → '<<Yay>>'
make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
make_out_word('[[]]', 'word') → '[[word]]'
  
26.String1 - Extra_end :
Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
extra_end('Hello') → 'lololo'
extra_end('ab') → 'ababab'
extra_end('Hi') → 'HiHiHi'

27.String1 - First_two :
Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".
first_two('Hello') → 'He'
first_two('abcdefg') → 'ab'
first_two('ab') → 'ab'

28.String1 - First_half :
Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'

29.String1 - Without_end :
Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.
without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin'

30.String1 - Combo_string :
Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).
combo_string('Hello', 'hi') → 'hiHellohi'
combo_string('hi', 'Hello') → 'hiHellohi'
combo_string('aaa', 'b') → 'baaab'

31.String1 - Non_start :
Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.
non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava'

32.String1 - Left2 :
Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.
left2('Hello') → 'lloHe'
left2('java') → 'vaja'
left2('Hi') → 'Hi'

33.String2 - Double_char :
Given a string, return a string where for every char in the original, there are two chars.
double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'

34.String2 - Count_hi :
Return the number of times that the string "hi" appears anywhere in the given string.
count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2

35.String2 - Cat_dog :
Return True if the string "cat" and "dog" appear the same number of times in the given string.
cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True

36.String2 - Count_code :
Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2

37.String2 - End_other :
Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.
end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True

38.String2 - xyz_there :
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True

39.List1 - First_last6 :
Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.
first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False
