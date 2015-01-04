import math, time
import copy
import calendar # for p19()
import decimal  # for p26()
import operator # for p59()
from fractions import Fraction # for p57()

# returns all primes less than or equal to n
def sieve_of_eratosthenes(n):
  sieve = [True for i in xrange((n-1)/2 + 1)] # gets 
  
  for sieve_ind in xrange(1, len(sieve)):
    if sieve_ind:
      val_at_ind = 2*sieve_ind + 1
      if val_at_ind**2 > n: break
      for composite in xrange(val_at_ind + 2*val_at_ind, n + 1, 2*val_at_ind):
        composite_ind = (composite - 1) / 2
        sieve[composite_ind] = False
  print sieve
  return [2] + [2*i + 1 for i in xrange(1, len(sieve)) if sieve[i]]

# solves the quadratic equation ax^2 + bx + c = 0
def quadratic(a, b, c):
  try:
    r1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    r2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    return list(set([r1, r2]))
  except:
    return []

# calculates all permutations of the list l
def scrambled_set(s):
  def helper(s, s_list):
    if len(s) == 1:
      return [s]
    elif len(s) == 0:
      return []
    else:
      for char in s:
        s_list +=map(lambda x: char + x, helper(s.replace(char, "", 1), []))
      return list(set(s_list))
  return helper(s, [])

# calculates set subtraction of A - B
def set_subtraction(A, B):
  return_set = []
  for a in A:
    if not a in B:
      return_set.append(a)
  return return_set

# calculates the powerset of l
def power_set(l):
  size = len(l)
  pset = []
  for i in xrange(2**size):
    i_bin = bin(i)[2:].zfill(size)
    partial_pset = []
    for j in xrange(len(i_bin)):
      c = i_bin[j]
      if c == '1':
        partial_pset.append(l[j])
    pset.append(partial_pset)
  return pset


# returns n1 xor n2 where n1 and n2 are ints
def xor(n1, n2):
  return (n1 & ~n2) | (~n1  & n2)

def fibonacci(n):
  arr = [1,1]
  while True:
    sum = arr[-1] + arr[-2]
    if sum > n:
      break
    else:
      arr.append(sum)
  return arr

def is_pali(n):
  n = str(n)
  if len(n) <= 1:
    return True
  else:
    return (n[0] == n[-1] and is_pali(n[1:-1]))

# gives prime factorization of n
# deprecated ---- use prime_factorization() instead
def prime(n):
  i = 2
  arr = []
  while n > 1:
    cnt = 0
    while (n % i == 0):
      n = n / i
      cnt += 1
    if cnt > 0:
      arr.append((i, cnt))
    i += 1
  return arr

# gives prime factorization of n in the form of a dictionary
# key: prime factor, value: number of times
def prime_factorization(n):
  i = 2
  arr = {}
  if n > 1:
    cnt = 0
    while (n % i == 0):
      n /= i
      cnt += 1
      if cnt > 0:
        arr[i] = cnt
    i += 1
  while n > 1:
    cnt = 0
    while (n % i == 0):
      n = n / i
      cnt += 1
    if cnt > 0:
      arr[i] = cnt
    i += 2
  return arr

# checks if there is a tuple in l that contains x in first index
def contains(l, x):
  for t in l:
    if t[0] == x:
      return True
  return False

# returns index at which x is located in l
def index(l, x):
  i = 0
  for t in l:
    if t[0] == x:
      return i
    i += 1
  return i

# gives lcm of 2 prime_factorization arrays
def lcm(a, b):
  n1 = prime_factorization(a).items()
  n2 = prime_factorization(b).items()
  # print n1
  arr = []
  for (a1, a2) in n1:
    new_elem = (a1, a2)
    if contains(n2, a1): 
      new_elem = (a1, max(a2, n2[index(n2, a1)][1]))
    arr.append(new_elem)
  for (b1,b2) in n2:
    if not contains(n1, b1):
      arr.append((b1, b2))
  return wrap(arr)

# gives hcf of 2 numbers; also accepts prime_factorization arrays
def hcf(n1, n2):
  if type(n1) is int:
    n1 = prime_factorization(n1)
  if type(n2) is int:
    n2 = prime_factorization(n2)

  hcf = 1
  for k1, v1 in n1.iteritems():
    if k1 in n2:
      hcf *= (k1 * min(v1, n2[k1]))
  return hcf

# turns factorization list into number
def wrap(x):
  sum = 1
  for (a1, a2) in x:
    sum *= a1**a2
  return sum

# calculates sum of squares of first n natural numbers
def sum_squares(n):
  sum = 0
  for i in xrange(n+1):
    sum += i*i
  return sum

# sums digits in a number (ie, sum_digits(123) = 6)
def sum_digits(n):
  n = str(n)
  sum = 0
  for c in n:
    sum += int(c)
  return sum

def sum_array(arr):
  sum = 0
  for i in arr:
    sum += i
  return sum 

def num_divisors(n):
  arr = prime(n)
  product = 1
  for (a1, a2) in arr:
    product *= a2 + 1
  return product

# returns number of terms in collatz sequence for n
def collatz(n):
  cnt = 1
  while n!= 1:
    if n % 2 == 0:
      n = n/2
    else:
      n = 3*n + 1
    cnt += 1
  return cnt

def proper_divisors(n):
  divisors = []
  for i in xrange(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
      divisors.append(i)
      if i != 1 and n/i != i:
        divisors.append(n/i)
  return divisors

def is_prime(n):
  for i in xrange(3, int(math.sqrt(n)) + 1, 2):
    if n % i == 0:
      return False
  return not (n % 2 == 0)

def only_primes(l):
  return_l = []
  for elem in l:
    if is_prime(int(elem)):
      return_l.append(elem)
  return return_l

def create_primes():
  prime_d = {2:1, 3:1, 5:1, 7:1, 11:1, 13:1}
  arr = [2,3,5,7,11,13]
  i = 17
  while i < 1000000:
    # # print "in while"
    i_is_prime = True
    for x in arr:
      if x > math.sqrt(i):
        break
      if i % x == 0:
        i_is_prime = False
        break
    if i_is_prime:
      prime_d[i] = 1
      arr.append(i)
    i += 2
  print len(prime_d)
  return prime_d

def create_triangle_list(n):
  l = [1,3,6,10,15,21,28,36,45,55]
  i = 11
  num = i * (i+1) /2
  while num < n:
    l.append(num)
    i += 1
    num = i * (i+1) / 2
  return l

def choose (a, b):

  return math.factorial(a) / (math.factorial (b) * math.factorial(a - b))

# number chain is defined as in p92(), dict is the list of preseen num chains
def number_chain(n, dict):
  def helper(n, l):
    if dict.has_key(n):
      l.append(dict[n])
      return l
    elif n == 1 or n == 89:
      l.append(n)
      return l
    else:
      str_n = str(n)
      sum = 0
      for c in str_n:
        sum += int(c) ** 2
      l.append(n)
      return helper(sum, l)
  return helper(n, [])

############################CLASSES###################################

# represent a fraction as ([a,b],[c,d]) such that it is equal to (ab)/(cd)
class DigitFraction:
  numerator = (0,0)
  denominator = (0, 1)

  def __init__(self, a=0, b=0, c=0, d=1):
    # print "%d, %d, %d, %d"%(a,b,c,d)
    self.numerator = (a, b)
    self.denominator = (c, d)

  def __repr__(self):
    a = self.numerator[0]
    b = self.numerator[1]
    c = self.denominator[0]
    d = self.denominator[1]
    return "(%d, %d) / (%d, %d)" % (a, b, c, d)

  # returns fraction as (n,d) s.t. self = n/d
  def simplify(self):
    n = self.numerator[0] * 10 + self.numerator[1]
    d = self.denominator[0] * 10 + self.denominator[1]
    return n,d

  def lt1(self):
    (n,d) = self.simplify()
    return n/d < 1

  def simplified_division(self):
    n1 = self.numerator
    d1 = self.denominator
    a = n1[0]; b = n1[1]; c = d1[0]; d = d1[1]

    if a == 0 or b == 0 or not self.lt1(): 
      return False
    elif a == c and self.is_equal(Fraction(0, b, 0, d)):
      return True
    elif a == d and self.is_equal(Fraction(0, b, 0, c)):
      return True
    elif b == c and self.is_equal(Fraction(0, a, 0, d)):
      return True
    elif b == d and self.is_equal(Fraction(0, a, 0, c)):
      return True
    else:
      return False

  # returns if self is of the same value as Fraction `f2`
  def is_equal(self, f2):
    fract1 = self.simplify()
    fract2 = f2.simplify()
    return fract1[0] * fract2[1] == fract1[1] * fract2[0]

# represents number 123 as [1, 2, 3]
class Number:
  def __init__(self, n=0):
    self.rep = []
    if n != 0:
      while n > 0:
        # print "n: %d"%n
        ones = n % 10
        n /= 10
        # print "ones: %d"%ones
        self.rep.insert(0, ones)
        # print self.rep
      # print self.rep
    else:
      self.rep.append(n)

  def __repr__(self):
    return str(self.rep)

  def remove_msb(self):
    return self.rep[1:]

  def remove_lsb(self):
    return self.rep[:len(self.rep) - 1]

  def to_int(self):
    cnt = len(self.rep) - 1
    sum = 0
    for digit in self.rep:
      sum += digit * 10**(cnt)
      cnt -= 1
    return sum

# stores number in the form a**b
class BigNum:
  def __init__(self, a, b):
    self._num = (a, b)
    self._exp = b * math.log(a) / math.log(2)

  def __cmp__(self, other):
    return cmp(self._exp, other._exp)
