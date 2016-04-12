class Robot:
    """Represents a robot, with a name."""

    
    # A class variable, counting the number of robots
    population = 0   # a default value

    
    __curse = 'Darn!'



    
    def __init__(self, name):
        #Initializes the data
        self.name = name
        print('(Initializing {0})'.format(self.name))
        # When this person is created, the robot # adds to the population in the global class, not the instance
        Robot.population += 1

        

    def getCurse(self):
        return self.__curse
        
            
    def sayHi(self):
        print('Greetings, my masters call me {0}'.format(self.name))
        
    def howMany():
        print('We have {0:d} robots.'.format(Robot.population))
        
    def __del__(self):
        # another intrinsic, we can delete instances!
        print('{0} is being destroyed!'.format(self.name))
        print(self.__curse, "I don't want to die...")
        Robot.population -= 1
        if Robot.population == 0:
            print('{0} was the last one.'.format(self.name))
        else:
            print('There are still {0:d} robots working.'.format(Robot.population))



