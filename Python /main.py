import dataclasses 
from dataclasses import dataclass
import struct
import random

random.seed(1)
TYPE_A = 1
CLASS_IN = 1

@dataclass
class DNSheader :
    id : int 
    flags : int =0
    num_questions: int =0  
    num_answers : int =0 
    num_authorities : int =0 
    num_additions : int =0 
    
    def header_to_bytes(self):
        fields = dataclasses.astuple(self)
        return struct.pack("!HHHHHH" , *fields)
    
@dataclass    
class DNSQuestions:
    name:bytes
    type_ : int
    class_ : int   
    
    def questions_to_bytes(self):
        return self.name + struct.pack("!HH" , self.type_ , self.class_ )   
    

 
def encode_dns_name(domain_name):
    encoded = b""
    for part in domain_name.encode("ascii").split(b"."):
        encoded += bytes([len(part)])+part
    return encoded + b"\x00"

print(encode_dns_name("google.com")    )
 
def build_query(domain_name , record_type) : 
    name = encode_dns_name(domain_name)
    id = random.randint(0 , 65535)
    RecursionDesired = 1<<8
    header = DNSheader(id,flags=RecursionDesired , num_questions=1)
    question = DNSQuestions(name=name , type_=record_type , class_=CLASS_IN)
    return header.header_to_bytes()+ question.questions_to_bytes()  

print(build_query("example.com", TYPE_A))