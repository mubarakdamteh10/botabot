from random import *
import time
from speechtext import *

a1 = "sotol"
a2 = "ช้อนทะเลทราย หรือ ดอกไม้ช้อน"
a3 = "Dasylirion Wheeleri"

a4 = "อเลกูล่าด่าง"
a5 = "Agave sp."

a6 = "กระดูกงู"

a7 = "แมมมิลาเรียต่อหัว"
a8 = "Mammillaria"

a9 = "หยกเขียว"
a10 = "Euphorbia lacteal forma cristata Haw"

a11 = "พญาไร้ใบกัมพลนี"
a12 = "Euphorbia kamponii Rauh & Petignat"

a13 = "ใบแบนยอดแดง"
a14 = "Euphorbia Enterophora"

a15 = "ใบเสมา พันธ์"
a16 = "Opuntia robusta Spineless"

a17 = "ลิ้นแม่ยายใหญ่ พันธ์"
a18 = "Sansevieria roxburghiana"

a19 = "อเลกูล่าสีเงิน"

b1 = "หัวโต หรือ แส้ม้า"
b2 = "Beaucarnea recurvata Lem"

b3 = "ใบเสมา พันธ์"
b4 = "Opuntia leucotricha"

b5 = "ว่านหางจระเข้"
b6 = "Aloe acutissima"

b7 = "ส้มเช้า"
b8 = "Euphorbia nerlifolia"

b9 = "ยูโพเบีย"

b10 = "สเตปโทเนีย"
b11 = "Stenocereus griseus"

b12 = "ใบเสมา"
b13 = "Opuntia robusta"

c1 = "พาซีโพเดียม"
c2 = "Pachypodium lamerei Drake"

c3 = "อากาเว่ปากนกแก้วเขียว"
c4 = "Agave attenuate sebsp"

c5 = "เข็มกุดันด่าง"
c6 = "Yucca alolfolia L"

c7 = "อลอยเดีย"
c8 = "Alluaudia procera Dake"

c9 = "หนามขอ"
c10 = "Ferocactus cf.herrerae J.G.Ortega"

c11 = "พาชีโพเดียมต่อยอดแคระ"
c12 = "Pachypodium sp."

d1 = "เขากวางเขียว"
d2 = "Euphorbia antiquarum L."

d3 = "เขากวางด่าง" 
d4 = "Eupharbia antiquorum L."

d5 = "ลิ้นแม่ยายใหญ่ หรือ ลิ้นมังกรพาเท็นส์"
d6 = "Sansevieria patens"

d7 = "หยกขาว"

d8 = "พญาไร้ใบ"
d9 = "Eupharbia lirucall L."

d10 = "ลิ้นแม่ยายใหญ่ พันธ์"
d11 = "Sansevieria roxburghiana"

d12 = "มงกุฎตุรกี หรือ หมวกตุรกี"
d13 = "Melocactus cf. peruvianus Vaupel"

d14 = "ลิ้นแม่ยายใหญ่ พันธ์"
d15 = "Sansevieria pearsonil N.E.Br."

A = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19]
B = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13]
C = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
D = [d1,d2,d3,d4,d5,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15]

def datazone():
    zone = [1,2,3,4]
    Azone = "A zone"
    Bzone = "B zone"
    Czone = "C zone"
    Dzone = "D zone"
    zonetell = randint(1,4)
    if zonetell == 1:
        speechtext(a1,'en')
        speechtext(a2,'th')
        speechtext(a3,'th')
        return(Azone)
    elif zonetell == 2:
        speechtext(b1,'en')
        speechtext(b2,'th')
        speechtext(b3,'th')
        return(Bzone)
    elif zonetell == 3:
        speechtext(c1,'en')
        speechtext(c2,'th')
        speechtext(c3,'th')
        return(Czone)
    elif zonetell == 4:
        speechtext(d1,'en')
        speechtext(d2,'th')
        speechtext(d3,'th')
        return(Dzone)

