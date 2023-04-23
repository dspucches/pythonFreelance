from question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",  # question_prompt[0], answer is "a"
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",  # question_prompt[1], answer is "c"
    "What color are Strawberries\n(a) Yellow\n(b) Red\n(c) Green\n\n",  # question_prompt[2], answer is "b"
]

questions = [
    Question(question_prompts[0], "a"),  # 'prompt' from Class 'question' is the index, 'answer' is the string 'a'
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]


def run_test(questions):  # questions is stored in the function as a parameter, giving the function the questions data
    score = 0  # increment score variable
    for question in questions: # for the question in questions
        answer = input(question.prompt)  # input for your answer gets stored in question.prompt - which is in the
        # Class 'question' and variable self.prompt
        if answer == question.answer:  # if the answer is correct...
            score += 1  # add one point
    print("You answered " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)
