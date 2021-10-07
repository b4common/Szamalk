# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



#Creates a Quiz where u can have as many question as you like and outputs your score too!
'''
!!!Hibás!!
class Question_Maker :

    def Question_maker (self):
        score = 0
        input_1 = [int(input("How many Question r u gonna have? : "))]
        Question_List_Number = [1]
        Question_List_Number.extend(input_1)

        for x in Question_List_Number:
            question = input("Give me a Question: ")
            correct_answer_question = input("Give me the correct answer: ")
            print(question)

            answer = input("")
            if answer == correct_answer_question :
                score += 1
                print("True","Your score: ", score)
            else :
                score -= 1
                print("You are wrong!","Your score: ", score)


MyQuestion_Maker = Question_Maker()
MyQuestion_Maker.Question_maker()
'''
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

'''

'''
szam1 = int(input("Első szam: "))
szam2 = int(input("Masodik szam: "))
szam3 = int(input("Harmadik szam: "))
eredmeny = szam1+szam2+szam3 / 3
print("Szamtani közép: ",eredmeny)
'''

'''
vezetek = input("Vezetek: ")
kereszt = input("Kereszt: ")
teljes_nev = vezetek + "  " + kereszt

print("",teljes_nev )
'''

szam3 = int(input("Kérek egy számot: "))
x = [int(a) for a in str(szam3)]
print(x)