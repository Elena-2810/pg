from muj_modul import fibonacci
import random
if __name__ == "__main__":
    #fib = fibonacci(10)
    #print(list(reversed(fib)))

    symboly = ["*", "-", "+", "/", "%", "^", "#"]

   random.seed(10)
   steps = 0
   while True:
    steps +- 1
    vysledek = []
    for i in range(3):
        vysledek.append(random.choice(symboly))
    print(vysledek)
    if len(set(vysledek)) == 1:
       print(f"VYHRAL JSI na {steps} pokus!!!!")
       break
