import dataclasses 
from dataclasses import dataclass
import struct
import random
import socket
import difflib

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

query  = build_query("www.google.com" , 1)
# builds a UDP socket 
sock = socket.socket(socket.AF_INET6 , socket.SOCK_DGRAM) 

sock.sendto(query , ("8.8.8.8" , 53))
response , _ = sock.recvfrom(1024)

print(response)
Sample_answer = b' O\x81\x80\x00\x01\x00\x01\x00\x00\x00\x00\x03www\x07example\x03com\x00\x00\x01\x00\x01\xc0\x0c\x00\x01\x00\x01\x00\x00Q\xb6\x00\x04]\xb8\xd8"'

similarity_score = difflib.SequenceMatcher(None, response, Sample_answer).ratio()
if(similarity_score >= 0.6 ):
    print("Similar")
else:
    print("Not Similar")    