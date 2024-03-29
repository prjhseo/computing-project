#my_answer
price=int(input("물건의 가격을 입력하세요: "))
pay=int(input("지불한 가격을 입력하세요: "))

diff=pay-price
print("당신이 거슬러 받을 돈은 ",diff,"원입니다")

print("방법 1")
a=[1000,500,100,50]
for i in a:
  if(diff/i>=1):
    print(i,"원",diff//i,"개")
    diff%=i

print("\n방법 2")
diff=pay-price
if(diff/1000>=1):
  print("1000원",diff//1000,"개")
  diff=diff%1000
if(diff/500>=1):
  print("500원",diff//500,"개")
  diff=diff%500
if(diff/100>=1):
  print("100원",diff//100,"개")
  diff=diff%100
if(diff/50>=1):
  print("50원",diff//50,"개")
  diff=diff%50


