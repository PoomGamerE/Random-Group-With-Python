import random
'''
สำคัญ! นี่คือโค้ดที่ค่อนข้างสมบูรณ์ของการสุ่มกลุ่ม
โปรดอย่าเผลอลบเพื่อกันความผิดพลาดที่จะเกิดขึ้นด้วยครับ
Update: Verion นี้มีการยัดคนเกินเข้ากลุ่มแล้ว และ 
ระบบเช็คคนเกินด้วยหารเอาเศษ แทนระบบ เช็คค่าไม่เท่ากับ 0'''

#ส่วนนำเข้า
numOfstudent = int(input("จำนวนนักเรียนทั้งห้องมีจำนวน: "))
NumOfGroup = int(input("จำนวนกลุ่มมีจำนวน: "))
numOfstudentPerGroup = numOfstudent / NumOfGroup
print("จำนวนนักเรียนต่อกลุ่มมีจำนวน:", int(numOfstudentPerGroup))

#ตัวแปรเก็บเลขที่
studentnumber = []
for x in range(numOfstudent):
    studentnumber.append(x + 1)

#ตัวแปรของระบบสุ่ม
AllGroup = []  #ใส่ทั้งหมด แต่มีแถวตอน
Group = []  #ตะกร้าใส่เลขที่
NumGroupOfRandom = 0

#ระบบสุ่ม
for p in range(int(NumOfGroup)):
    for s in range(int(numOfstudentPerGroup)):
        RandomN = int(random.choice(studentnumber))  #สุ่มค่าจากตัวแปร
        Group.append(RandomN)  #เก็บข้อมูลไปยังกลุ่ม
        studentnumber.remove(RandomN)  #ลบตัวเลขออกจากตัวแปร
    NumGroupOfRandom = NumGroupOfRandom + 1
    AllGroup.append(Group.copy())
    Group.clear()

#Check จำนวนคนเกิน
Limit = True
CheckMax = numOfstudent % NumOfGroup

if CheckMax == 0:
    Limit = False

#ระบบสุ่ม (กรณีที่มีคนเกิน)
if Limit == True:
    OverStudent = numOfstudent % NumOfGroup  #จำนวนคนที่เกิน
    print("จำนวนคนเกินที่จะถูกบังคับเข้ากลุ่ม:", OverStudent)

    for Count in range(int(OverStudent)):
        RandomN = int(random.choice(studentnumber))  #สุ่มค่าจากตัวแปร
        AllGroup[Count].append(RandomN)  #เก็บข้อมูลไปยังกลุ่ม
        studentnumber.remove(RandomN)  #ลบตัวเลขออกจากตัวแปร

#แสดงคนที่อยู่ในแต่ละกลุ่ม
for y in range(int(NumOfGroup)):
    print("กลุ่ม ", y + 1, "(", len(AllGroup[y]), "คน) ได้แก่เลขที่:",
          AllGroup[y])

#เช็คข้อมูลที่เก็บไว้แต่ละกลุ่ม Output
SearchG = int(input("ต้องการเช็คกลุ่มไหน: "))
print("กลุ่ม ", SearchG, "(", len(AllGroup[SearchG - 1]), "คน) ได้แก่เลขที่:",
      AllGroup[SearchG - 1])
