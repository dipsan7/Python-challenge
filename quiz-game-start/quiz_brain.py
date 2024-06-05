class QuizBrain:
     def __init__(self,q_list):
          self.question_number=0
          self.question_list=q_list
          self.score=0
     def still_has_question(self):
          return self.question_number<len(self.question_list)
               
     def next_question(self):
          current_question=self.question_list[self.question_number]
          self.question_number +=1
          user_ans=input(f"Q.{self.question_number}:{current_question.text}(True/False)")
          self.check_answer(user_ans,current_question.answer)
     def check_answer(self,user_ans,correct_answer):
          if user_ans==correct_answer:
               self.score +=1
               print("you got it right")
               
               
          else:
               print("you are wrong")
          print(f"the current ans is {correct_answer}")
          print(f"your current score is {self.score}/{self.question_number}")
          print("/n")
              

        
     
     

