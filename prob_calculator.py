import copy
import random
# Consider using the modules imported above.

class Hat:

#ATRIBUTES

    def __init__(self, **kwargs):
        self.contents = []
        for key,value in kwargs.items():
            if value > 0:
                for number in range(value):
                    self.contents.append(key)
        self.copyOfContents = copy.deepcopy(self.contents)
      
#METHODS

    def draw(self, ball_number):
        draw_pile = []
        
        if ball_number >= len(self.contents):
            
            for number in range(len(self.contents)):
                random_index = random.randint(0, (len(self.contents) -1))
                pop = self.contents.pop(random_index)
                draw_pile.append(pop)
             
        else:
            for number in range(ball_number):
                random_index = random.randint(0, (len(self.contents)-1))
                pop = self.contents.pop(random_index)
                draw_pile.append(pop)
              
        if ball_number >= len(self.contents):
            self.contents = self.copyOfContents.copy() 
          
        return draw_pile

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    occurences = 0
    
    for i in range(num_experiments):
        a_chance = hat.draw(num_balls_drawn)
        a_dic_chance = dict()
    
        for ball in a_chance:
            a_dic_chance[ball] = a_dic_chance.get(ball, 0) + 1
    
     #FIRST CHECK  
    
        def check_keys(expected_balls, a_dic_chance):
            for key in expected_balls.keys():
                if key in a_dic_chance:
                    continue
                else:
                    return False
            return True
        
        first_check = check_keys(expected_balls, a_dic_chance)
        if first_check != True:
            continue 
    
     #SECOND CHECK
    
        def check_values(expected_balls, a_dic_chance):
            
            for key in expected_balls.keys():
                if expected_balls[key] <= a_dic_chance[key]:
                    continue    
                else:
                    return False
            return True
        
        second_check = check_values(expected_balls, a_dic_chance)

        if second_check:
            occurences += 1 

    probability = occurences / num_experiments
    print(probability)
    return probability
