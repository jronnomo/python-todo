import json

with open("../files/questions.json") as file:
    questions = file.read()

data = json.loads(questions)

score = 0
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index+1, alternative)
    answer = int(input("What is your answer?: "))
    question["user_answer"] = answer

score = 0
for index, question in enumerate(data):
    if question["correct_answer"] == question["user_answer"]:
        score = score + 1
        result = "Correct answer"
    else:
        message = "Incorrect! The correct answer is " + str(question["correct_answer"])
        print(message)

print(f"{score}/2")