class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0
        self.score = 0

    def add_question(self, question, correct_answer, options):
        self.questions.append({
            'question': question,
            'correct_answer': correct_answer,
            'options': options
        })

    def start_quiz(self):
        print("Welcome to the Quiz Game!")
        for i, question in enumerate(self.questions, start=1):
            print(f"Question {i}: {question['question']}")
            for j, option in enumerate(question['options'], start=1):
                print(f"{j}. {option}")
            
            user_answer = input("Your answer (enter the option number): ")
            if self.check_answer(i - 1, int(user_answer)):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is: {question['correct_answer']}\n")
        
        print(f"Quiz Completed! Your score is: {self.score}/{len(self.questions)}")

    def check_answer(self, question_index, user_choice):
        return self.questions[question_index]['correct_answer'] == self.questions[question_index]['options'][user_choice - 1]


# Example usage:
quiz = Quiz()
quiz.add_question("What is the capital of France?", "Paris", ["London", "Berlin", "Paris", "Madrid"])
quiz.add_question("Which planet is known as the Red Planet?", "Mars", ["Mars", "Venus", "Earth", "Jupiter"])
quiz.add_question("What is the largest mammal on Earth?", "Blue Whale", ["Giraffe", "Elephant", "Blue Whale", "Kangaroo"])

quiz.start_quiz()
