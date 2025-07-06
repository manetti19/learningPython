
# Write code below 💖
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

q1 = input("Q1) Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk\n")
if q1 == "1" or q1 == "Dawn" or q1 == "dawn":
  Gryffindor += 1
  Ravenclaw += 1
elif q1 == "2" or q1 == "Dusk" or q1 == "dusk":
  Hufflepuff += 1
  Slytherin +=1
else:
  print("Wrong input.")

print("Gryffindor =", Gryffindor, "Ravenclaw =", Ravenclaw, "Hufflepuff =", Hufflepuff, "Slytherin =", Slytherin)

q2 = input("Q2) When I’m dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\n")
if q2 == "1" or q1 == "Good" or q1 == "good":
  Hufflepuff += 2
elif q2 == "2" or q1 == "Great" or q1 == "great":
  Slytherin +=2
elif q2 == "3" or q1 == "Wise" or q1 == "wise":
  Ravenclaw += 2
elif q2 == "4" or q1 == "Bold" or q1 == "bold":
  Gryffindor += 2
else:
  print("Wrong input.")

print("Gryffindor =", Gryffindor, "Ravenclaw =", Ravenclaw, "Hufflepuff =", Hufflepuff, "Slytherin =", Slytherin)

q3 = input("Q3) Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\n")
if q3 == "1" or q1 == "violin":
  Slytherin +=4
elif q3 == "2" or q1 == "trumpet":
  Hufflepuff += 4
elif q3 == "3" or q1 == "piano":
  Ravenclaw += 4
elif q3 == "4" or q1 == "drum":
  Gryffindor += 4
else:
  print("Wrong input.")

maior = max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)
if Gryffindor == maior:
    print("Gryffindor venceu!")
elif Ravenclaw == maior:
    print("Ravenclaw venceu!")
elif Hufflepuff == maior:
    print("Hufflepuff venceu!")
elif Slytherin == maior:
    print("Slytherin venceu!")
else:
  print("Wrong input.")

print("Gryffindor =", Gryffindor, "Ravenclaw =", Ravenclaw, "Hufflepuff =", Hufflepuff, "Slytherin =", Slytherin)


