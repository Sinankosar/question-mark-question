import string
def QuestionsMarks(strParam):
  #Sinan Koşar
  a= 0
  b = 0
  if strParam[0].isdigit():
    a = int(strParam[0])
  for i in strParam:
    if i.isdigit():
      if int(i) + a == 10:
        if b ==3:
          return True
      else:
        a = int(i)
        b=0
    elif i =="?":
      b+=1

  # code goes here
  return strParam

# keep this function call here
print(QuestionsMarks("8???dsa2?s?4d??6s?"))

