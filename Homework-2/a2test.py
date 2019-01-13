# ANSHUMAN SINGH
# 2017025
# Section A - Group 2

import gvb
from a2 import *

gvb.tile1=0;gvb.tile2=0;gvb.tile3=0;gvb.tile4=0;gvb.tile5=0;gvb.tile6=0;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0

# TEST cases should cover the different boundary cases.

# TEST CASES for the Validmove() function
gvb.tile1=0;gvb.tile2=0;gvb.tile3=0;gvb.tile4=0;gvb.tile5=0;gvb.tile6=0;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0
gvb.tile1=0;gvb.tile2=2;gvb.tile3=0;gvb.tile4=1;gvb.tile5=0;gvb.tile6=1;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0
assert(validmove(1)==True),"Validmove returned wrong in First Test Case of Validmove"
gvb.tile1=0;gvb.tile2=0;gvb.tile3=0;gvb.tile4=0;gvb.tile5=1;gvb.tile6=0;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0
assert(validmove(5)==False),"Validmove returned wrong in Second Test Case of Validmove"
gvb.tile1=0;gvb.tile2=0;gvb.tile3=2;gvb.tile4=0;gvb.tile5=0;gvb.tile6=0;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0
assert(validmove(3)==False),"Validmove returned wrong in Third Test Case of Validmove"
gvb.tile1=0;gvb.tile2=0;gvb.tile3=0;gvb.tile4=0;gvb.tile5=0;gvb.tile6=0;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0
assert(validmove(9)==True),"Validmove returned wrong in Fourth Test Case of Validmove"
gvb.tile1=0;gvb.tile2=0;gvb.tile3=0;gvb.tile4=0;gvb.tile5=0;gvb.tile6=0;gvb.tile7=1;gvb.tile8=0;gvb.tile9=0
assert(validmove(7)==False),"Validmove returned wrong in Fifth Test Case of Validmove"

print("Ran 5 Test Cases for validmove() function")
print("All OK")
print(" ")

#TEST CASES for the win() function
gvb.tile1=0;gvb.tile2=0;gvb.tile3=0;gvb.tile4=0;gvb.tile5=0;gvb.tile6=0;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0
gvb.tile1=5;gvb.tile2=5;gvb.tile3=5;gvb.tile4=0;gvb.tile5=2;gvb.tile6=1;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0
assert(win()==False),"Win function failed test cases in the the test case 1"
gvb.tile1=0;gvb.tile2=0;gvb.tile3=1;gvb.tile4=0;gvb.tile5=0;gvb.tile6=1;gvb.tile7=0;gvb.tile8=0;gvb.tile9=1
assert(win()==True),"Win function failed test cases in the the test case 2"
gvb.tile1=1;gvb.tile2=2;gvb.tile3=1;gvb.tile4=2;gvb.tile5=1;gvb.tile6=2;gvb.tile7=2;gvb.tile8=1;gvb.tile9=2
assert(win()==False),"Win function failed test cases in the the test case 3"
gvb.tile1=1;gvb.tile2=0;gvb.tile3=0;gvb.tile4=1;gvb.tile5=0;gvb.tile6=0;gvb.tile7=1;gvb.tile8=0;gvb.tile9=0
assert(win()==True),"Win function failed test cases in the the test case 4"
gvb.tile1=0;gvb.tile2=0;gvb.tile3=2;gvb.tile4=0;gvb.tile5=2;gvb.tile6=0;gvb.tile7=2;gvb.tile8=0;gvb.tile9=0
assert(win()==True),"Win function failed test cases in the the test case 5"

print("Ran 5 Test Cases for win() function")
print("All OK")
print(" ")

#TEST CASES for the takeNaiveMove() function
gvb.tile1=0;gvb.tile2=0;gvb.tile3=0;gvb.tile4=0;gvb.tile5=0;gvb.tile6=0;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0
gvb.tile1=1;gvb.tile2=1;gvb.tile3=2;gvb.tile4=1;gvb.tile5=2;gvb.tile6=0;gvb.tile7=1;gvb.tile8=2;gvb.tile9=2
assert(takeNaiveMove() == 6),"takeNaiveMove() function failed its FIRST Test Case"
gvb.tile1=1;gvb.tile2=1;gvb.tile3=0;gvb.tile4=0;gvb.tile5=0;gvb.tile6=0;gvb.tile7=1;gvb.tile8=1;gvb.tile9=1
assert(3<=takeNaiveMove()<=6),"takeNaiveMove() function failed its SECOND Test Case"
gvb.tile1=0;gvb.tile2=0;gvb.tile3=0;gvb.tile4=0;gvb.tile5=0;gvb.tile6=0;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0
assert(0<=takeNaiveMove()<=9),"takeNaiveMove() function failed its THIRD Test Case"
gvb.tile1=0;gvb.tile2=0;gvb.tile3=0;gvb.tile4=1;gvb.tile5=2;gvb.tile6=1;gvb.tile7=2;gvb.tile8=1;gvb.tile9=1
assert(1<=takeNaiveMove()<=3),"takeNaiveMove() function failed its FOURTH Test Case"
gvb.tile1=1;gvb.tile2=1;gvb.tile3=1;gvb.tile4=1;gvb.tile5=2;gvb.tile6=1;gvb.tile7=2;gvb.tile8=2;gvb.tile9=0
assert(takeNaiveMove() == 9),"takeNaiveMove() function failed its FIFTH Test Case"

print("Ran 5 Test Cases for takeNaiveMove() function")
print("All OK")
print(" ")

#TEST CASES for the takeStrategicMove() function
gvb.tile1=0;gvb.tile2=0;gvb.tile3=0;gvb.tile4=0;gvb.tile5=0;gvb.tile6=0;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0
gvb.tile1=1;gvb.tile2=1;gvb.tile3=0;gvb.tile4=0;gvb.tile5=0;gvb.tile6=0;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0
assert(takeStrategicMove()==3),"takeStrategicMove() function failed test case 1"
gvb.tile1=0;gvb.tile2=0;gvb.tile3=0;gvb.tile4=0;gvb.tile5=0;gvb.tile6=0;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0
gvb.tile1=0;gvb.tile2=0;gvb.tile3=0;gvb.tile4=0;gvb.tile5=0;gvb.tile6=0;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0
assert(takeStrategicMove()==5),"takeStrategicMove() function failed test case 2"
gvb.tile1=0;gvb.tile2=0;gvb.tile3=0;gvb.tile4=0;gvb.tile5=0;gvb.tile6=0;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0
gvb.tile1=0;gvb.tile2=0;gvb.tile3=0;gvb.tile4=0;gvb.tile5=1;gvb.tile6=0;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0
assert(takeStrategicMove()==3 or takeStrategicMove()==1 or takeStrategicMove()==7 or takeStrategicMove()==9),"takeStrategicMove() function failed test case 3"
gvb.tile1=0;gvb.tile2=0;gvb.tile3=0;gvb.tile4=0;gvb.tile5=0;gvb.tile6=0;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0
gvb.tile1=1;gvb.tile2=1;gvb.tile3=0;gvb.tile4=1;gvb.tile5=1;gvb.tile6=0;gvb.tile7=1;gvb.tile8=2;gvb.tile9=2
assert(takeStrategicMove()==3),"takeStrategicMove() function failed test case 4"
gvb.tile1=0;gvb.tile2=0;gvb.tile3=0;gvb.tile4=0;gvb.tile5=0;gvb.tile6=0;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0
gvb.tile1=1;gvb.tile2=1;gvb.tile3=0;gvb.tile4=1;gvb.tile5=2;gvb.tile6=1;gvb.tile7=0;gvb.tile8=2;gvb.tile9=2
assert(takeStrategicMove()==3),"takeStrategicMove() function failed test case 5"

print("Ran 5 Test Cases for takeStrategicMove() function")
print("All OK")
print(" ")

#TEST CASES for the validBoard() function
gvb.tile1=0;gvb.tile2=0;gvb.tile3=0;gvb.tile4=0;gvb.tile5=0;gvb.tile6=0;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0
gvb.tick1=1;gvb.tick2=0
assert(validBoard()==True),"validBoard() failed the test case 1"
gvb.tick1=0;gvb.tick2=0
assert(validBoard()==True),"validBoard() failed the test case 2"
gvb.tick1=1;gvb.tick2=2
assert(validBoard()==False),"validBoard() failed the test case 3"

print("Ran all the Test Cases for validboard() function")
print("All OK")
print(" ")


#TEST CASES for the game(gametype=1) function

gvb.tile1=0;gvb.tile2=0;gvb.tile3=0;gvb.tile4=0;gvb.tile5=0;gvb.tile6=0;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0

assert(0<=game(1)<=2),"game(1) function failed its test cases"
assert(0<=game(2)<=2),"game(2) function failed its test cases"
assert(0<=game(3)<=2),"game(3) function failed its test cases"

print("Ran all the Test Cases for game function")
print("All OK")
print(" ")

#TEST CASES for the game1(n) function

gvb.tile1=0;gvb.tile2=0;gvb.tile3=0;gvb.tile4=0;gvb.tile5=0;gvb.tile6=0;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0

assert(0<game1(10)<1),"TEST CASE failed for game1(n) function for test case 1"
assert(0.30<=game1(100)<=0.70),"TEST CASE failed for game1(n) function for test case 2"
assert(0.400<=game1(1000)<0.600),"TEST CASE failed for game1(n) function for test case 3"

print("Ran all the Test Cases for game1(n) function")
print("All OK")
print(" ")

#TEST CASES for the game2(n) function

gvb.tile1=0;gvb.tile2=0;gvb.tile3=0;gvb.tile4=0;gvb.tile5=0;gvb.tile6=0;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0

assert(0<=game2(10)<=1),"TEST CASE failed for game2(n) function for test case 1"
assert(0<=game2(100)<=0.10),"TEST CASE failed for game2(n) function for test case 2"
assert(0<=game2(1000)<0.100),"TEST CASE failed for game2(n) function for test case 3"

print("Ran all the Test Cases for game2(n) function")
print("All OK")
print(" ")

#TEST CASES for the game3(n) function

gvb.tile1=0;gvb.tile2=0;gvb.tile3=0;gvb.tile4=0;gvb.tile5=0;gvb.tile6=0;gvb.tile7=0;gvb.tile8=0;gvb.tile9=0

assert(game3(10)==0),"TEST CASE failed for game3(n) function for test case 1"
assert(game3(100)==0),"TEST CASE failed for game3(n) function for test case 2"
assert(game3(1000)==0),"TEST CASE failed for game3(n) function for test case 3"

print("Ran all the Test Cases for game3(n) function")
print("All OK")
print(" ")

print("Ran all the test cases given")
print("Code is OK")