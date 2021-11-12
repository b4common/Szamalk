# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#A Simple loop for exercise
#fruits = ["apple", "banana", "cherry"]
#for x in fruits:
 #   print(x)
  #  if x == "banana":
   #     break


#Reverse a string.
#def reverse(x):
 #   return x[::-1]

#mytext = reverse("Reverse this string")
#print(mytext)


#Converts the input to Kg or Lbs.

#weight = int(input("Give me a weight: "))
#measurement = input("Kg or Lbs: ? ")
#if measurement == "Kg":
 #   converted = weight / 0.45
  #  print("Your weight in lbs: ", converted)

#elif measurement == "Lbs":
 #   converted = weight * 0.45
  #  print("Your weight in kgs: ", converted)

'''

# Működő , helyes változat!
def Question_maker ():
    input_2 = int(input("How many question? : "))
    i = 1
    x = 0
    y = 0
    score = 0
    Questions = []
    Correct_Answers = []
    while i <= input_2:
        question = input("Give me a Question: ")
        correct_answer_question = input("Give me the correct answer: ")
        Questions.append(question) , Correct_Answers.append(correct_answer_question)
        i += 1
    while x < len(Questions):
        print(Questions[y])
        answer = input("Answer: ")
        if answer == Correct_Answers[y] :
            print("Helyes !")
            score += 1
        else :
            print("Helytelen!")
            score -= 1
        x += 1
        y += 1
    print("Your score: ", score)
Question_maker()


#This is a Elevator Simulator!
# Loops through as many times as many user is set to.
user = [1,2]
current_floor = [0]
NumberOfFloors = [1, 2, 3, 4, 5, 6, 7]
for x in user :
    selected_floor = int(input("Please select a floor between 1-7: "))
    indice = [floors]
    selected_element = []
    for index in indice:
        selected_element.append(NumberOfFloors[index-1])
        print("You arrived at floor:",selected_element)
    if current_floor == 0 or current_floor[-1] == floors:
        print("Already here")
    current_floor.append(floors)
'''

'''
import math
def Checking(i):
    i = input("Válasszon: ")
    try:
        y = math.floor(float(i))
        return y
    except :
        print("Helytelen tipus!!!")


while (True) :
    szöveg1 = 'Ön a'
    szöveg2 = 'kerület, terület számítását választotta,'
    print('Mit szeretne ?')
    print('-----------')
    print('  Négyzet kerülete, területe --> 1')
    print('  Téglalap kerülete, területe --> 2')
    print('  Rombusz kerülete, területe --> 3')
    print('  Kör kerülete, területe --> 4')
    print("  Kilépés --> 5")
    i = 0
    helyes_valasz = Checking(i)

    if helyes_valasz > 5 :
        print('Nem választotta egyik lehetőséget sem !!!')
    if helyes_valasz == 5:
        print("Ön kilépett a programból!")
        break
    while (helyes_valasz != None) :
        if helyes_valasz == 1:
            # print('Ön a négyzet kerület, terület számítását választotta,')
            print(szöveg1, 'négyzet', szöveg2)
            a = float(input('Adja meg a négyzet oldalát: '))
            K = 4 * a
            T = a ** 2
            print('A négyzet kerülete:', K, 'területe:', T)
            break
        elif helyes_valasz == 2:
            # print('Ön a téglalap kerület, terület számítását választotta,')
            print(szöveg1, 'téglalap', szöveg2)
            a = float(input('Adja meg a téglalap egyik oldalát: '))
            b = float(input('Adja meg a téglalap másik oldalát: '))
            K = 2 * (a + b)
            T = a * b
            print('A téglalap kerülete:', K, 'területe:', T)
            break
        elif helyes_valasz == 3:
            # print('Ön a rombusz kerület, terület számítását választotta,')
            print(szöveg1, 'rombusz', szöveg2)
            a = float(input('Adja meg a rombusz oldalát: '))
            alfa = float(input('Adja meg a bezárt szöget: '))
            K = 4 * a
            T = a ** 2 * (math.sin(alfa * 0.017453292519943))
            print('A rombusz kerülete:', K, 'területe:', round(T, 4))
            break
        elif helyes_valasz == 4:
            # print('Ön a kör kerület, terület számítását választotta,')
            print(szöveg1, 'kör', szöveg2)
            r = float(input('Adja meg a kör sugarát: '))
            K = 2 * r * math.pi
            T = r ** 2 * math.pi
            print('A kör kerülete:', round(K, 4), 'területe:', round(T, 4))
            break
        elif helyes_valasz < 0:
            print("Negatív szám , nem elfogadható!!")
            break


'''

'''
---2021.10.14---
Given a string s, find the length of the longest substring without repeating characters.
class Solution(object):
    def lengthOfLongestSubstring(s: str) -> int:
        left = 0
        right = 0
        max_len = 0
        d = {}
        while left < len(s):
            if s[left] in d and d[s[left]] >= right:
                right = d[s[left]] + 1
            max_len = max(max_len, left - right +1)
            d[s[left]] = left
            left += 1
        print(max_len)
        return max_len


megoldás = Solution
megoldás.lengthOfLongestSubstring("wkevwkkk")
'''


'''
#Brute Force approach
def twoSum():
    nums = [9,2,3,6,11]
    target = 9
    left = 0
    right = 1
    for i in range(len(nums)):
        sum = nums[left] + nums[right]
        if sum == target :
            print(left,right)
            break
        else :
            left += 1
            right += 1

twoSum()

#Cleaner Approach
nums = [9,2,3,6,11]
target = 9
def two_2_Sum ():
    for right in range(len(nums)):
        for left in range(right + 1, len(nums)):
            if nums[left] == target - nums[right]:
                return [left, right]
                
                

#Hash table approach
def twoSum(self,nums,target):
    hash_table = {}
    for i in range (len(nums)):
        complemment = target -nums[i]
        if complemment not in hash_table:
            hash_table[nums[i]]
        else:
            return [hash_table[complemment],i]
            
            
            
def nagyobbSzam ():
    a = int(input("Kérek Egy számot: "))
    b = int(input("Kérek Egy másik számot: "))
    if a > b :
        print(a)
    else:
        print(b)

nagyobbSzam()


my_string = input("Kérek egy stringet: ")
s = my_string.split()
print(s)            
            
'''

#<---------------------LeetCode Problems------------------------->
'''
#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
#The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
s = [1,2,3,4]
a = ''.join(map(str, s))
b = int(a) + 1
c = str(b)
print( list(map(int, c)))

#2
#Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
#A word is a maximal substring consisting of non-space characters only.
#Egysoros megoldás
return len(s.strip().split(' ')[-1])


#3
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 hash_table = dict()
        for i in range(len(nums)):
            num = nums[i]
            complemment = target - nums[i]
            if num in hash_table:
                return [hash_table[num], i]
            else:
               hash_table[complemment] = i
               
               
#4
#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

nums = [1,3,4,6,9]
target = 6
left = 0
right = len(nums) - 1
while left <= right:
 # checking middle position
    idx = (left + right) // 2
    num = nums[idx]
    if num == target:
        print(idx)
    # halving the range
    if num < target:
        left = idx + 1
    else:
        right = idx - 1
    # target not  found
    print(left)

