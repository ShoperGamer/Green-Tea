x = int(input("น้ำ(ลบ.ซม): "))
y = int(input("น้ำตาล(กรัม):"))

countwater = x // 250 #น้ำทำชาเขียว 250 ลบ.ซม. / 1 ขวด (สามารถปรับได้)
countsugar = y // 15 #น้ำตาล 15 กรัม  / 1 ขวด (สามารถปรับได้)

max = min(countwater,countsugar) #max ค่ามากสุด min ค่าน้อยสุด

print("จำนวนชาเขียวสูงสุด :",max,"ขวด") #แสดงค่าของ max

if x > max*250: #น้ำเหลือแสดงข้อความ water
  print("water")
