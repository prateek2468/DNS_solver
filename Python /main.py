import dataclasses 
from dataclasses import dataclass
import struct

# @dataclass
# class DNSheader :
#     id : int 
#     flags : int 
#     num_questions: int 
#     num_answers : int 
#     num_authorities : int
#     num_additions : int 
    
#     def header_to_bytes(self):
#         fields = dataclass.astuple(self)
#         return struct.pack("!HHHHHH" , *fields)
    
# @dataclass    
# class DNSQuestions:
#     name:bytes
#     type_ : int
#     class_ : int   
    
#     def questions_to_bytes(self):
#         return self.name + struct.pack("!HH" , self.type_ , self.class_ )   
    
byte = struct.pack("iii" , 10 , 20 , 30 )
print(struct.calcsize('H'))
print(byte) 
    

    
            
        
                