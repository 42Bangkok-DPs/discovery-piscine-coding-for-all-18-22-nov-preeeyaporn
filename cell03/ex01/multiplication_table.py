def ตารางสูตรคูณ(จำนวน):
  for i in range(1, 11):
    ผลลัพธ์ = จำนวน * i
    print(f"{จำนวน} x {i} = {ผลลัพธ์}")
num = int(input("ป้อนจำนวนที่ต้องการสร้างตารางสูตรคูณ: "))
ตารางสูตรคูณ(num)