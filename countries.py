class India(): 
    def capital(self): 
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is the most spoken language in India")
    def type(self): 
        print("India is a developing country")
class South_Korea(): 
    def capital(self): 
        print("Seoul is the capital of South Korea")
    def language(self): 
        print("Korean is the most spoken language of South Korea")
    def type(self): 
        print("Korea is a developed country")
obj_India = India()
obj_SK = South_Korea()
for country in (obj_India, obj_SK): 
    country.capital()
    country.language()
    country.type()
    
