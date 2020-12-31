def sumInts(*args):
   """Sums an array of integers.
   :param args: Array of arguments
   :type args: Integers
   :return: Sum
   :rtype: Integer
   """
   r = 0;
   for i in args:
      r += i
   return r

def main():
   print("Sum = " + str(sumInts(1,2,3)))
   print("Sum = " + str(sumInts(1,2)))
   
if __name__ == '__main__':
   main()