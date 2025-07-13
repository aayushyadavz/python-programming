letter = ''' 
       Dear <|Name|>,
       You are selected!
       <|Date|>
       '''

print(letter.replace("<|Name|>", "Ayush").replace("<|Date|>", "24/03/2006"))