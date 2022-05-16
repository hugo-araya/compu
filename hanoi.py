def hanoi(n, com, aux, fin):
  if n==1:
      print(com, "->", fin)
  else:
      hanoi(n-1,com,fin,aux)
      print(com, "->", fin)
      hanoi(n-1, aux, com, fin)

if __name__ == "__main__":
    hanoi(64, 1, 2, 3)
