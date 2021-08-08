class Puppy:
    population = 0
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Puppy.population += 1
        
    def __del__(self):
        Puppy.population -= 1
    
    def bark(self):
        print(f'왈왈! 나는{self.name}, {self.breed}(이)야')
    
    @classmethod
    def get_population(cls):
        print(f'현재 강아지 마리수: {cls.population}')
        return cls.population