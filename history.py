import random

#ส่วนนำเข้า
numOfstudent = int(input("จำนวนนักเรียนทั้งห้องมีจำนวน: "))
NumOfGroup = int(input("จำนวนกลุ่มมีจำนวน: "))
numOfstudentPerGroup = numOfstudent / NumOfGroup
print("จำนวนนักเรียนต่อกลุ่มมีจำนวน:", int(numOfstudentPerGroup))

#Check จำนวนคนเกิน
Limit = False
CheckMax = (numOfstudent / NumOfGroup) - int(numOfstudentPerGroup)
if CheckMax != 0:
    CheckN = numOfstudent - int(numOfstudentPerGroup) * NumOfGroup
    print("พบจำนวนคนเกิน:", CheckN)
    Limit = True

#ตัวแปรเก็บเลขที่
studentnumber = []
for x in range(numOfstudent):
    studentnumber.append(x + 1)

#ระบบสุ่ม
AllGroup = []#ใส่ทั้งหมด แต่มีแถวตอน
Group = []#ตะกร้าใส่เลขที่
NumGroupOfRandom = 0

for p in range(int(NumOfGroup)):
    for s in range(int(numOfstudentPerGroup)):
        RandomN = int(random.choice(studentnumber))  #สุ่มค่าจากตัวแปร
        Group.append(RandomN)  #เก็บข้อมูลไปยังกลุ่ม
        studentnumber.remove(RandomN)  #ลบตัวเลขออกจากตัวแปร
    NumGroupOfRandom = NumGroupOfRandom + 1
    print("กลุ่ม ", NumGroupOfRandom, " ได้แก่เลขที่:", Group)
    AllGroup.append(Group.copy())
    Group.clear()

#หากมีคนเหลือเพราะเกิน
if Limit == True:
    print("คนที่เหลือเกินมาจากระบบสุ่ม:", studentnumber)

#เช็คข้อมูลที่เก็บไว้แต่ละกลุ่ม Output
SearchG = int(input("ต้องการเช็คกลุ่มไหน: "))
print("กลุ่มที่ ", SearchG, "ได้แก่เลขที่:", AllGroup[SearchG - 1])