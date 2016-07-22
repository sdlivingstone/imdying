# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 13:39:34 2016
PokemonGO
object oriented programming/creation of objects with different properties and 
@author: student
"""
from random import randint
class Pokemon:
    #pokemon trait
    def __init__(self,oriName,oriType,orihp):
        self.name = oriName        
        self.type = oriType
        self.hp = orihp
        self.cp = randint(1,600)
        self.moves = OriMoves
vee = Pokemon("Eevee", "Normal",5)

def battle(self,myMove,opponent,opponentMove):
    print(self.name+"USED" +myMove+"!!!")
    opponent.hp -=(self.move[myMove] * self.cp)
    print(opponent.name + "HAS" + str(opponent.hp)+ "HP LEFT!!!")
    if opponent.hp <=0
        print(opponent.name + "DIED!!!")
        print("YOU WIN!!!")
        return
    print(opponent.name + "USED" + opponentMove + "!!!")




eevee_moves = {"Swift":10, "Dig":20}    
vee = Pokemon("Evee","Normal",5)
squirtle_moves = {"Squirt": 40, "Water Gun":100}
squats = Pokemon("Squirtle". "Water Gun":100)   
    
    
    
    
    
    
    
    
    
    
    
    print(vee.cp)