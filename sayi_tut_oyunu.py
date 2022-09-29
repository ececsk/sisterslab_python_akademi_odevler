#Aklından bir sayı tut oyunu
import random
randomSayi=random.randint(0,101)
counter=0
num=None

#print("tutulansayi:",randomSayi)

print("Aklımdan 0 ile 100 arasında bir sayı tuttum. Aklımdaki sayıyı bil bakalım")

while(num!=randomSayi):
  num=int(input("Tahmininizi girin:"))
  counter+=1
  
  if num>randomSayi:
    print("Tuttuğum sayı daha küçük bir sayı tekrar deneyin")
  elif num<randomSayi:
    print("Tuttuğum sayı daha büyük bir sayı tekrar deneyin ")
  

print(f"Tebrikler {counter}. denemede bildiniz.\nAklımdaki sayı: {randomSayi}")

