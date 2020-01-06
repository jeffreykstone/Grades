# Author: Jeff Stone (934256195)
# Date: 1/5/2020
# Description:  This program calculates how many quiz questions can be dropped and still receive an A in CS 161.
# This program assumes 100% performance on assignments, which are worth 70% of grade.
# Quizzes are worth 30% of grade.
# An A requires 93%, A- = 90%, B+ = 87%, B = 83%, B- = 80%, C+ = 77%, C = 73%, C- = 70%, etc.
# Thus Quiz(.3)+Assignments(.7) = 1 or (.3Q + .7A) / (.3 + .7) = 100
# Since we need 93 for an A and 100(.7) = 70, we need a 23 out of 30 on the quizzes to get an A.
# There are a total of 224 points possible on the quizzes (8 quizzes, each with 7 problems valued at 7 points/question).

a = (23 / 30) * 224
a_minus = (20 / 30) * 224
b_plus = (17 / 30) * 224
b = (13 / 30) * 224
b_minus = (10 / 30) * 224
c_plus = (7 / 30) * 224
c = (3 / 30) * 224
c_minus = (0 / 30) * 224

print("You can miss ", 224 - a, "total points on the quizzes and receive an A grade.")
print("You can miss ", 224 - a_minus, "total points on the quizzes and receive a grade of A-.")
print("You can miss ", 224 - b_plus, "total points on the quizzes and receive a grade of B+.")
print("You can miss ", 224 - b, "total points on the quizzes and receive a B grade.")
print("You can miss ", 224 - b_minus, "total points on the quizzes and receive a grade of B-.")
print("You can miss ", 224 - c_plus, "total points on the quizzes and receive a grade of C+.")
print("You can miss ", 224 - c, "total points on the quizzes and receive a C grade.")
print("You can miss ", 224 - c_minus, "total points on the quizzes and receive an C- grade.")




