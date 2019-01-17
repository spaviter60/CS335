
import sys
# Define a main() function that prints a little greeting.
def main():
 
  mult(int(sys.argv[1]), int (sys.argv[1]))
 

if __name__ == '__main__':
  main()
def mult(x, y):
  a = int(x)
  b = int(y)
  c = a * b
  print c
  return;