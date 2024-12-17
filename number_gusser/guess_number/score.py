class UserScore:
    dict = {}   
    @classmethod
    def addScore(cls, name, score=0):
        if name in cls.dict:
            cls.dict[name] += score
        else:
            cls.dict[name] = score
                
    @classmethod
    def finalScore(cls, name):
        return cls.dict.get(name, 0)  # Use get method to handle names not in dict
