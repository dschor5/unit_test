def sumInts(*args):
   r = 0;
   for i in args:
      r += i
   return r

def main():
   print("Sum = " + str(sumInts(1,2,3)))
   print("Sum = " + str(sumInts(1,2)))
   
if __name__ == '__main__':
   main()