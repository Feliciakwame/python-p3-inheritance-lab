#!/usr/bin/env python

from user import User

class Student(User):
    knowledge=[]
    def __init__(self,first_name,last_name):
        
        super().__init__(first_name,last_name,)
    
    def learn(self,new_knowledge):
        if isinstance(new_knowledge,str):
            self.knowledge.append(new_knowledge)
        else:
            return "Please enter a string"
        