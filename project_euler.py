# Lawrence Chen
# Project Euler solutions
# May 8, 2014

# Go to http://projecteuler.net/problems to see the problems 

from util import *

def p1():
  i = 1;
  sum = 0;  
  while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
      sum += i;
    i += 1; 
  print sum

def p2():
  target = 4000000
  arr = fibonacci(target);
  sum = 0
  for i in arr:
    if i % 2 == 0:
      sum += i
  print sum

def p3():
  target = 997799
  i = 2;
  largest_prime = 1;
  while target > 2:
    while target % i == 0:
      largest_prime = i
      target = target / i
    i+=1
  print largest_prime

def p4():
  largest_pali = 9009
  for i in xrange(999):
    for j in xrange(999):
      num = (i * j)
      if is_pali(num) and num > largest_pali:
        largest_pali = num
        break
  print largest_pali

def p5():
  sm_factorization = prime(2520)
  for x in xrange(11, 20):
    tmp = prime(x)
    sm_factorization = lcm(sm_factorization, tmp)
  print wrap(sm_factorization)

def p6():

  print 5050**2 - sum_squares(100)

def p7():
  arr = [2,3,5,7,11, 13]
  i = 17
  while len(arr) != 10001:
    i_is_prime = True
    for x in arr:
      if x > math.sqrt(i) + 1:
        break
      if i % x == 0:
        i_is_prime = False
        break
    if i_is_prime:
      arr.append(i)
    i += 2
  print arr[10000]

def p8():
  input = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
  def multiply(n):
    product = 1;
    for i in xrange(5):
      product *= n % 10
      n = n / 10
    return product
  
  i1 = 0; i2 = 5; largest_product = 0; 
  while i2 < len(input):
    n = multiply(int(input[i1:i2]))
    if n > largest_product:
      largest_product = n
    i1 += 1; i2 += 1
  print largest_product

def p9():
  def helper():
    for a in xrange(1,1000):
      for b in xrange(1,1000):
        c = math.sqrt(a**2 + b**2)
        if (int(c)**2 == a**2 + b**2) and (a + b + int(c) == 1000):
          print (a, b, int(c))
          return a*b*int(c)
  print helper()

def p10():
  arr = [2,3,5,7,11, 13]
  i = 17
  while i < 2000000:
    i_is_prime = True
    for x in arr:
      if i % x == 0:
        i_is_prime = False
        break
    if i_is_prime:
      print i
      arr.append(i)
    i += 2
  print sum_array(arr)

def p11():
  input = [
  [ 8, 02, 22, 97, 38, 15, 00, 40, 00, 75, 04, 05, 07, 78, 52, 12, 50, 77, 91,  8],
  [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 04, 56, 62, 00],
  [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 03, 49, 13, 36, 65],
  [52, 70, 95, 23, 04, 60, 11, 42, 69, 24, 68, 56, 01, 32, 56, 71, 37, 02, 36, 91],
  [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
  [24, 47, 32, 60, 99, 03, 45, 02, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
  [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
  [67, 26, 20, 68, 02, 62, 12, 20, 95, 63, 94, 39, 63,  8, 40, 91, 66, 49, 94, 21],
  [24, 55, 58, 05, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
  [21, 36, 23,  9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95],
  [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 03, 80, 04, 62, 16, 14,  9, 53, 56, 92],
  [16, 39, 05, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57],
  [86, 56, 00, 48, 35, 71, 89, 07, 05, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
  [19, 80, 81, 68, 05, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 04, 89, 55, 40],
  [04, 52,  8, 83, 97, 35, 99, 16, 07, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
  [88, 36, 68, 87, 57, 62, 20, 72, 03, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
  [04, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18,  8, 46, 29, 32, 40, 62, 76, 36],
  [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 04, 36, 16],
  [20, 73, 35, 29, 78, 31, 90, 01, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 05, 54],
  [01, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 01, 89, 19, 67, 48],
  ]

  def multiply(arr):
    product = 1
    for i in arr:
      product *= i
    return product

  def max_horizontal():
    max_val = 0
    for i in xrange(len(input)):
      arr = input[i]
      ind1 = 0; ind2 = 4
      while ind2 < len(arr):
        max_val = max(max_val, multiply(arr[ind1:ind2]))
        ind1 += 1; ind2 += 1
    return max_val

  def max_vertical():
    max_val = 0
    for i in xrange(len(input) - 3):
      for j in xrange(len(input) - 3):
        arr = [input[i][j], input[i+1][j], input[i+2][j], input[i+3][j]]
        max_val = max(max_val, multiply(arr))
    return max_val

  # max diagonal in the /// direction
  def max_diagonal_forward():
    max_val = 0
    for i in xrange(3, len(input)):
      for j in xrange(len(input) - 3):
        arr = [input[i][j], input[i-1][j+1], input[i-2][j+2], input[i-3][j+3]]
        max_val = max(max_val, multiply(arr))
    return max_val


  print max(max_horizontal(), max_vertical(), max_diagonal_forward()) 
        
def p12():
  arr = [0]
  def triangle(n):
    if n < len(arr):
      return arr[n]
    else:
      v = n + triangle(n-1)
      arr.append(v)
      return v

  def helper():
    k = 500
    i = triangle(k)
    while True:
      n = num_divisors(i)
      print ("i: %d; n: %d" % (i, n))
      if n > 500:
        return i
      k += 1
      i += k

  print helper()

def p13():
  input = [
  37107287533902102798797998220837590246510135740250,
  46376937677490009712648124896970078050417018260538,
  74324986199524741059474233309513058123726617309629,
  91942213363574161572522430563301811072406154908250,
  23067588207539346171171980310421047513778063246676,
  89261670696623633820136378418383684178734361726757,
  28112879812849979408065481931592621691275889832738,
  44274228917432520321923589422876796487670272189318,
  47451445736001306439091167216856844588711603153276,
  70386486105843025439939619828917593665686757934951,
  62176457141856560629502157223196586755079324193331,
  64906352462741904929101432445813822663347944758178,
  92575867718337217661963751590579239728245598838407,
  58203565325359399008402633568948830189458628227828,
  80181199384826282014278194139940567587151170094390,
  35398664372827112653829987240784473053190104293586,
  86515506006295864861532075273371959191420517255829,
  71693888707715466499115593487603532921714970056938,
  54370070576826684624621495650076471787294438377604,
  53282654108756828443191190634694037855217779295145,
  36123272525000296071075082563815656710885258350721,
  45876576172410976447339110607218265236877223636045,
  17423706905851860660448207621209813287860733969412,
  81142660418086830619328460811191061556940512689692,
  51934325451728388641918047049293215058642563049483,
  62467221648435076201727918039944693004732956340691,
  15732444386908125794514089057706229429197107928209,
  55037687525678773091862540744969844508330393682126,
  18336384825330154686196124348767681297534375946515,
  80386287592878490201521685554828717201219257766954,
  78182833757993103614740356856449095527097864797581,
  16726320100436897842553539920931837441497806860984,
  48403098129077791799088218795327364475675590848030,
  87086987551392711854517078544161852424320693150332,
  59959406895756536782107074926966537676326235447210,
  69793950679652694742597709739166693763042633987085,
  41052684708299085211399427365734116182760315001271,
  65378607361501080857009149939512557028198746004375,
  35829035317434717326932123578154982629742552737307,
  94953759765105305946966067683156574377167401875275,
  88902802571733229619176668713819931811048770190271,
  25267680276078003013678680992525463401061632866526,
  36270218540497705585629946580636237993140746255962,
  24074486908231174977792365466257246923322810917141,
  91430288197103288597806669760892938638285025333403,
  34413065578016127815921815005561868836468420090470,
  23053081172816430487623791969842487255036638784583,
  11487696932154902810424020138335124462181441773470,
  63783299490636259666498587618221225225512486764533,
  67720186971698544312419572409913959008952310058822,
  95548255300263520781532296796249481641953868218774,
  76085327132285723110424803456124867697064507995236,
  37774242535411291684276865538926205024910326572967,
  23701913275725675285653248258265463092207058596522,
  29798860272258331913126375147341994889534765745501,
  18495701454879288984856827726077713721403798879715,
  38298203783031473527721580348144513491373226651381,
  34829543829199918180278916522431027392251122869539,
  40957953066405232632538044100059654939159879593635,
  29746152185502371307642255121183693803580388584903,
  41698116222072977186158236678424689157993532961922,
  62467957194401269043877107275048102390895523597457,
  23189706772547915061505504953922979530901129967519,
  86188088225875314529584099251203829009407770775672,
  11306739708304724483816533873502340845647058077308,
  82959174767140363198008187129011875491310547126581,
  97623331044818386269515456334926366572897563400500,
  42846280183517070527831839425882145521227251250327,
  55121603546981200581762165212827652751691296897789,
  32238195734329339946437501907836945765883352399886,
  75506164965184775180738168837861091527357929701337,
  62177842752192623401942399639168044983993173312731,
  32924185707147349566916674687634660915035914677504,
  99518671430235219628894890102423325116913619626622,
  73267460800591547471830798392868535206946944540724,
  76841822524674417161514036427982273348055556214818,
  97142617910342598647204516893989422179826088076852,
  87783646182799346313767754307809363333018982642090,
  10848802521674670883215120185883543223812876952786,
  71329612474782464538636993009049310363619763878039,
  62184073572399794223406235393808339651327408011116,
  66627891981488087797941876876144230030984490851411,
  60661826293682836764744779239180335110989069790714,
  85786944089552990653640447425576083659976645795096,
  66024396409905389607120198219976047599490197230297,
  64913982680032973156037120041377903785566085089252,
  16730939319872750275468906903707539413042652315011,
  94809377245048795150954100921645863754710598436791,
  78639167021187492431995700641917969777599028300699,
  15368713711936614952811305876380278410754449733078,
  40789923115535562561142322423255033685442488917353,
  44889911501440648020369068063960672322193204149535,
  41503128880339536053299340368006977710650566631954,
  81234880673210146739058568557934581403627822703280,
  82616570773948327592232845941706525094512325230608,
  22918802058777319719839450180888072429661980811197,
  77158542502016545090413245809786882778948721859617,
  72107838435069186155435662884062257473692284509516,
  20849603980134001723930671666823555245252804609722,
  53503534226472524250874054075591789781264330331690
  ]
  sum = 0
  for i in input:
    sum += i
  print sum

def p14():
  num = 1
  num_terms = 1
  for i in xrange(1,1000000):
    z = collatz(i)
    if z > num_terms:
      num = i
      num_terms = z
  print num
  
def p16():
  n = 1<<1000
  sum = 0
  while n > 0:
    sum += n % 10 
    n = n / 10
  print sum

def p17():
  """this function is INCORRECT"""
  # constants:
  AND = 3
  ONE = 3
  TWO = 3
  THREE = 5
  FOUR = 4
  FIVE = 4
  SIX = 3
  SEVEN = 5
  EIGHT = 5
  NINE = 4
  TEN = 3
  ELEVEN = 6
  TWELVE = 6
  THIRTEEN = 8
  FOURTEEN = 8
  FIFTEEN = 7
  SIXTEEN = 7
  SEVENTEEN = 9
  EIGHTEEN = 8
  NINETEEN = 8
  XTY = 6
  HUNDRED = 7

  # sum of numbers {0..9}
  lt_10 = ONE + TWO + THREE + FOUR + FIVE + SIX + SEVEN + EIGHT + NINE

  # sum of numbers {0..19}
  lt_20 = (ONE + TWO + THREE + FOUR + FIVE + SIX + SEVEN + EIGHT + NINE + TEN + 
    ELEVEN + TWELVE + THIRTEEN + FOURTEEN + FIFTEEN + SIXTEEN + SEVENTEEN + 
    EIGHTEEN + NINETEEN)

  num_hundred = 9 * HUNDRED
  num_hundred_prefix = 100 * lt_10
  num_and = 9 * 99 * AND
  num_lt_20 = 10 * lt_20
  num_xty = 10 * 8 * XTY
  num_gt_20 = 10 * 8 * lt_10

  print num_hundred + num_hundred_prefix + num_and + num_lt_20 + num_xty + num_gt_20
    
def p18():
  input = [
  [75],
  [95, 64],
  [17, 47, 82],
  [18, 35, 87, 10],
  [20, 04, 82, 47, 65],
  [19, 01, 23, 75, 03, 34],
  [88, 02, 77, 73, 07, 63, 67],
  [99, 65, 04, 28, 06, 16, 70, 92],
  [41, 41, 26, 56, 83, 40, 80, 70, 33],
  [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
  [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
  [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
  [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
  [63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
  [04, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60, 04, 23]
  ]

  OPT = copy.copy(input)

  # fills the edges of OPT
  for i in xrange(1, len(OPT)):
    OPT[i][0] = OPT[i-1][0] + input[i][0]
    OPT[i][len(OPT[i])-1] = OPT[i-1][len(OPT[i-1])-1] + input[i][len(OPT[i])-1]

  for i in xrange(1, len(OPT)):
    for j in xrange(1, len(OPT[i])):
      # print "i: " + str(i)
      # print "j: " + str(j) + "\n"
      if i != j and j != 0:
        OPT[i][j] = max(OPT[i-1][j], OPT[i-1][j-1]) + input[i][j]

  print max(OPT[len(OPT)-1])

def p19():
  # num sundays from {1 Jan 1901, ...,  31 Dec 2000}
  num_sundays = 0
  for year in xrange(1901, 2001):
    for month in xrange(1,13):
      weeks = calendar.monthcalendar(year, month)
      if weeks[0][6] == 1:
        num_sundays += 1

  print num_sundays

def p20():
  arr = [1]
  def factorial(n):
    if n < len(arr):
      return arr[n]
    else:
      tot = n * factorial(n-1)
      arr.append(tot)
      return tot
  def sum_digits(n):
    sum = 0
    while n > 1:
      sum += n % 10
      n = n / 10
    return sum

  val = factorial(100)
  print sum_digits(val)

def p21():
  amicable_nums = []
  for a in xrange(1, 10000):
    d_a = sum_array(proper_divisors(a))
    b = d_a
    d_b = sum_array(proper_divisors(b))
    if a == d_b and a != b and not d_a in amicable_nums:
      amicable_nums.append(a)
      amicable_nums.append(d_a)
  print sum_array(amicable_nums)

def p22():
  def name_score (s):
    sum = 0;
    for i in s:
      sum += ord(i) - 64
    return sum

  f = open('names.txt')
  input = f.read()
  arr = []
  while '\"' in input:
    i1 = input.index('\"')
    i2 = input[i1+1:].index('\"')
    name = input[i1+1:i2+1]
    arr.append(name)
    input = input[i2+3:]
  arr.sort()
  
  i = 1
  sum = 0
  for j in arr:
    sum += i * name_score(j)
    i += 1
  print sum

def p23():
  def proper_divisors(n):
    divisors = []
    for i in xrange(1, n/2 + 1):
      if n % i == 0:
        divisors.append(i)
    return divisors
  def sum_divisors(n):
    sum = 0;
    for i in n:
      sum += i
    return sum

  abundant_numbers = []
  
  def sum_abundant(n):
    for i in abundant_numbers:
      for j in abundant_numbers:
        if i + j == n:
          return True
    return False

  def is_abundant(n):
    if sum_divisors(proper_divisors(n)) > n:
      return True
    return False

  total_sum = 0
  for i in xrange(1, 28124):
    # print i
    if not sum_abundant(i):
      # print i
      total_sum += i
    if is_abundant(i):
      # print i
      abundant_numbers.append(i)
  
  print total_sum    

def p24():
  
  print "solved with math"

def p25():
  i1 = 1; i2 = 1; k = 3
  fib_num = 2

  while fib_num < 10**999:
    i1 = i2; i2 = fib_num; fib_num = fib_num + i1; k+=1
  
  print k

def p26():
  d = decimal
  d.getcontext().prec = 1000
  """determines length of reciprocal of 1/n"""
  def reciprocal_length(n):
    n = (d.Decimal(1) / d.Decimal(n)) * 10**10  # shift by 5 digits to remove any unrepeating segments
    n = str(n - int(n))[2:]                     # string of decimal place
    fst_num = n[0]                              # first character
    ind = 0                                     # index of next `fst_num`
    is_valid = False

    while not is_valid:
      try:
        ind = n[ind + 1:].index(fst_num) + ind + 1
        # checking to see if ind is first repeat
        for i in xrange(1,6):
          if n[i] != n[ind + i]:
            break
          elif i == 5 and n[i] == n[ind + i]:
            is_valid = True      
      except Exception, e:
        is_valid = True

    return ind

  longest_recip = 1; n = 1
  for i in xrange(2,1000):
    z = reciprocal_length(i)
    if z > longest_recip:
      longest_recip = z
      n = i
  print "longest reciprocal is %d with length %d"% (n, longest_recip)

def p27():
  def chain(a,b):
    cnt = 0
    n = 0
    val = n*n + a *n + b
    while is_prime(val):
      cnt += 1
      n += 1
      val = n*n + a *n + b
    return cnt

  result = (0, 0, 0) # (maxcnt, a, b)
  for a in xrange(-1000, 1001):
    for b in range (-1000,1001):
      cnt = chain(a,b)
      if cnt > result[0]:
        result = (cnt, a, b)
  print result
      
def p28():
  def sum_diagonals(t):
    sum = 0
    col = len(t) - 1
    for row in xrange(len(t)): 
      sum += t[row][row] #sums diagonal from nw to se
      sum += t[row][col]
      col -= 1
    return sum

  table = []
  for i in xrange(1001):
    table.append([])
    for j in xrange(1001):
      table[i].append(0)
  
  cnt = 1001**2

  # CONSTANTS
  NORTHEAST = 0
  NORTHWEST = 1
  SOUTHWEST = 2
  SOUTHEAST = 3

  corner = NORTHEAST
  ne = (0, 1000); nw = (0,0); sw = (1000, 0); se = (1000, 1000)
  while cnt != 0:
    if corner == NORTHEAST:
      row = table[ne[0]]
      i = ne[1]
      while i >= nw[1]:
        row[i] = cnt
        cnt -= 1
        i -= 1
      
      ne = (ne[0] +1, ne[1])
      nw = (nw[0] +1, nw[1])
      corner = NORTHWEST
    elif corner == NORTHWEST:
      col = nw[1]
      i = nw[0]
      while i <= sw[0]:
        table[i][col] = cnt
        cnt -= 1
        i += 1

      nw = (nw[0], nw[1] +1)
      sw = (sw[0], sw[1]+1)
      corner = SOUTHWEST

    elif corner == SOUTHWEST:
      row = table[sw[0]]
      i = sw[1]
      while i <= se[1]:
        row[i] = cnt
        cnt -= 1
        i += 1

      sw = (sw[0]-1, sw[1])
      se = (se[0]-1, se[1])
      corner = SOUTHEAST

    else: #corner == SOUTHEAST
      col = se[1]
      i = se[0]
      while i >= ne[0]:
        table[i][col] = cnt
        cnt -= 1
        i -= 1

      se = (se[0], se[1]-1)
      ne = (ne[0], ne[1]-1)
      corner = NORTHEAST
  print sum_diagonals(table) - 1
      
def p29():
  arr = []
  for i in xrange(2, 101):
    for j in xrange(2, 101):
      n = i**j
      if not n in arr:
        arr.append(n)
  print len(arr)

def p30():
  def sum_digits(n):
    sum = 0
    while n > 0:
      sum += (n % 10) **5
      n = n/10
    return sum

  tot = 0
  for i in xrange(2,3000000000):
    if i == sum_digits(i):
      tot += i
  print tot

# unsolved
def p31():
  currency = [1,2,5,10,20,50,100,200]
  # currency = [100, 200]
  currency.reverse();
  total = 200;
  cnt = 0   

def p33():
  non_trivials = []

  f = Fraction()
  for c in xrange(10):
    for d in xrange(10):
      for a in xrange(10):
        for b in xrange(10):
          f = Fraction(a,b,c,d)
          if c == 0 and d == 0:
            continue
          if f.simplified_division():
            non_trivials.append(f)


  print non_trivials

def p34():
  def sum_digits(n):
    sum  = 0
    while n > 0:
      sum += factorial(n%10)
      n = n/10
    return sum
  
  f_list = [1]
  def factorial(n):
    if n < len(f_list):
      return f_list[n]
    tmp = n * factorial(n-1)
    f_list.append(tmp)
    return tmp
  
  
  sum = 0
  for i in xrange(12, 30000000):
    if i == sum_digits(i):
      sum += i
  print sum

def p35():
  # f is one's place, e is ten's, ..., a is hundred-thousands
  def create(a=0, b=0, c=0, d=0, e=0, f=0):
    rep = [0,0,0,0,0,0]
    rep[0] = a
    rep[1] = b
    rep[2] = c
    rep[3] = d
    rep[4] = e
    rep[5] = f
    return truncate(rep)

  def to_int(l):
    cnt = len(l) - 1
    sum = 0
    for digit in l:
      sum += digit * 10**(cnt)
      cnt -= 1
    return sum

  def to_number(i):
    rep = []
    while i > 0:
      rmdr = i % 10
      i /= 10
      rep.insert(0,rmdr)
      # print "inserted %d" %rmdr
    return rep


  # returns number with leading-0s removed
  def truncate(l):
    arr = []
    front_zero = True
    for dig in l:
      if front_zero and dig == 0:
        continue
      elif front_zero and dig != 0:
        front_zero = False
        arr.append(dig)
      else:
        arr.append(dig)
    return arr

  def rotate(l):
    arr = copy.copy(l)

    for i in xrange(len(l)):
      arr[(i+1) % len(l)] = l[(i + 2) % len(l)]
    # print arr
    return arr

  def check_rotations(i):
    n = rotate(to_number(i))
    is_prime = True
    for i in xrange(len(n)-1):
      # print str(n) + "\n"
      if not to_int(n) in primes:
        is_prime = False
        break
      n = rotate(n)
    return is_prime

  primes = create_primes()
  arr = []
  for i in xrange(1000000):
    if not i in primes: # not a prime number
      continue
    elif check_rotations(i): # i is in circular prime and not accounted for
      arr.append(i)
  # print arr
  print len(arr)
  
  # print check_rotations(1013)

def p36():
  sum = 0
  for i in xrange(1,1000000, 2):
    if is_pali(i) and is_pali(str(bin(i))[2:]):
      sum += i
  print sum

def p37():
  def check_right(n):
    for i in xrange(len(n.rep)):
      if not n.to_int() in primes:
        return False
      n.rep = n.remove_msb()
    return True

  def check_left(n):
    for i in xrange(len(n.rep)):
      if not n.to_int() in primes:
        return False
      n.rep = n.remove_lsb()
    return True

  primes = create_primes()
  num_trunc = 0
  i = 11
  arr = []
  while num_trunc != 11:
    if i > 1000000:
      raise Exception("Need to expand primes list")
    if i in primes and check_left(Number(i)) and check_right(Number(i)):
      arr. append(i)
      num_trunc += 1
    i += 2 
  print arr
  sum_array(arr)

def p39():
  perimeter_count = {}
  max_p = 0
  max_count = 0

  for a in xrange(1, 1000):
    for b in xrange(1, 1000):
      c_squared = a**2 + b**2
      c_is_int = int(math.sqrt(c_squared))**2 == c_squared

      if not c_is_int or (a + b + math.sqrt(c_squared) > 1000):
        continue
      elif c_is_int:
        p = (a + b + math.sqrt(c_squared))
        # if b < a: 
        #   continue
        if p in perimeter_count:
          perimeter_count[p] += 1
          if max_count < perimeter_count[p]:
            max_count = perimeter_count[p]
            max_p = p 
        else:
          perimeter_count[p] = 1

  print "max_p: %d\nAppeared %d times" %(max_p, max_count)

def p40():
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
      # else:
      #   self.rep.append(n)

    def __repr__(self):
      return str(self.rep)

    # n is integer
    def concatenate_num(self, n):
      for i in Number(n).rep:
        self.rep.append(i)

  n = Number()
  # print n
  for i in xrange(1,200000):
    n.concatenate_num(i)
  
  z = n.rep
  print z[1 - 1] * z[10 - 1] * z[100 - 1] * z[1000 - 1] * z[10000 - 1] * z[100000 - 1] *z[1000000 - 1]

def p42():
  input = open("words.txt")
  s = input.read()
  s = s[1:len(s) -1] # removes first and last '"' from the input
  arr = s.split('","')
  triangle_list = create_triangle_list(400)
  tri_cnt = 0

  for word in arr:
    sum  = 0
    for char in word:
      # print "char is " + char
      # print "val is " + str(ord(char)) + "\n"
      sum += (ord(char) - ord('A') + 1)
    if sum in triangle_list:
      tri_cnt += 1
  print tri_cnt

def p44():
  pentagon_list = [1, 5, 12, 22, 35, 51, 70, 92]
  def create_pentagon_list():
    n = 9
    while n != 100000:
      pentagon_list.append(int(n * (3*n-1) * 0.5))
      n+=1
  create_pentagon_list()

  d = []
  # for i in pentagon_list:
  #   for j in pentagon_list:
  #     print i,j
  #     if i == j or j > i: break
  #     elif i+j in pentagon_list and i - j in pentagon_list:
  #       d.append(i - j)
  # print d

  print max(pentagon_list)

def p45():
  def create_triangle_dict():
    arr = {}
    for i in xrange(286, 100000):
      arr[(i * (i+1) / 2)] = 1
    return arr
  def create_pentagon_dict():
    arr = {}
    for i in xrange(166,100000):
      arr[(i * (3*i-1)/2)] = 1
    return arr
  def create_hexagon_dict():
    arr = {}
    for i in xrange(144, 100000):
      arr[(i * (2*i-1))] = 1
    return arr
  t_dict = create_triangle_dict()
  p_dict = create_pentagon_dict()
  h_dict = create_hexagon_dict()
  for i in t_dict.keys():
    if p_dict.has_key(i) and h_dict.has_key(i):
      print i 
      break
  print "done"
 
def p46():
  p_list = [2,3,5,7,11, 13]
  def create_prime_list(): 
    i = 17
    while len(p_list) != 10001:
      i_is_prime = True
      for x in p_list:
        if x > math.sqrt(i) + 1:
          break
        if i % x == 0:
          i_is_prime = False
          break
      if i_is_prime:
        p_list.append(i)
      i += 2
  def goldbach_conjecture(n):
    for i in p_list:
      if i > n:
        break
      for j in xrange(1, int(math.sqrt(n))):
        v = i + 2*j*j
        if v == n:
          return True
    return False

  create_prime_list()

  for i in xrange(9, p_list[len(p_list) - 1], 2):
    if i in p_list:
      continue
    else: #i is not prime
      if not goldbach_conjecture(i):
        print i
        break

def p47():
  p_list = [2,3,5,7,11, 13]

  """input:prime factorization list; output: number of prime factors"""
  def num_primes(l):
    cnt = 0;
    for i in l:
      if i in p_list:
        cnt += 1
    return cnt

  i = 17
  while len(p_list) != 3402:
    i_is_prime = True
    for x in p_list:
      if x > math.sqrt(i) + 1:
        break
      if i % x == 0:
        i_is_prime = False
        break
    if i_is_prime:
      p_list.append(i)
    i += 2

  k = 647
  while True:
    p1 = num_primes(prime(k))
    p2 = num_primes(prime(k+1))
    p3 = num_primes(prime(k+2))
    p4 = num_primes(prime(k+3))
    # print k
    if p1 == 4 and p2 == 4 and p3 == 4 and p4 == 4:
      print k;
      break
    elif p2 ==4 and p3 ==4 and p4 == 4:
      k += 1
    elif p3 ==4 and p4 ==4:
      k += 2
    elif p4 == 4:
      k +=3
    else: # p_i != 4 for all 1 <= i <= 4
      k += 4

def p48():
  sum = 0
  for i in xrange(1,1001):
    sum += (i**i) % 10**10
  print sum % 10**10

def p50():
  p_list = [2,3,5,7,11, 13]
  def create_prime_list(): 
    i = 17
    while p_list[len(p_list) - 1] < 1000000:
      i_is_prime = True
      for x in p_list:
        if x > math.sqrt(i) + 1:
          break
        if i % x == 0:
          i_is_prime = False
          break
      if i_is_prime:
        p_list.append(i)
      i += 2
  print "Begin prime list create..."
  create_prime_list()
  print "Prime list create finished...\n"

  # create OPT table
  OPT = [[p_list[i]] for i in xrange(len(p_list))]
  # print OPT

  # OPT[i][j] = sum of p_list[i..j]
  l = 0
  max_prime = 0
  for i in xrange(len(p_list)):
    arr = OPT[i]
    for j in xrange(i, len(p_list)-1):
      sum = arr[j-i] + p_list[j+1]
      if sum in p_list and j - i > l:
        l = j-i
        max_prime = sum
        print max_prime
      arr.append(sum)
    # print arr
    OPT[i] = arr

  # print OPT
  print "Done. Max_prime is %d" % max_prime

def p53():
  cnt = 0
  for n in xrange(1, 101):
    for r in xrange(1, (n / 2) + 1):
      if choose(n, r) > 1000000:
        if n / 2.0 == r:
          cnt += 1
        else:
          cnt += 2
  print cnt

def p55():
  def is_lychrel(n):
    def reverse(n):
      n = str(n)
      new_str = ""
      for i in xrange(len(n)-1, -1, -1):
        new_str += n[i]
      return new_str
    def helper_lychrel(n, cnt):
      if cnt > 50:
        return False
      elif is_pali(n):
        return True
      else:
        return helper_lychrel(int(n) + int(reverse(n)), cnt + 1)
    n += int(reverse(n))
    n = str(n)
    return helper_lychrel(n, 0)

  num_lychrel = 0
  for i in xrange(1, 10000):
    if not is_lychrel(i):
      num_lychrel += 1
  print "Number of Lychrel Numbers in the range {1, 10,000} : %d" % num_lychrel
  # print is_lychrel(4994)

def p56():
  greatest_sum = 0
  for a in xrange(2, 100):
    for b in xrange(2, 100):
      s = sum_digits(a**b)
      if s > greatest_sum:
        greatest_sum = s
  print "greatest sum : %d" % greatest_sum

def p67():
  def readFile(filename):
    arr = []
    f = open(filename)
    for line in f:
      nums = line.split();
      for i in xrange(len(nums)):
        nums[i] = int(nums[i])
      arr.append(nums)
    return arr

  input = readFile("triangle.txt")
  OPT = copy.copy(input)
  # fills the edges of OPT
  for i in xrange(1, len(OPT)):
    OPT[i][0] = OPT[i-1][0] + input[i][0]
    OPT[i][len(OPT[i])-1] = OPT[i-1][len(OPT[i-1])-1] + input[i][len(OPT[i])-1]

  for i in xrange(1, len(OPT)):
    for j in xrange(1, len(OPT[i])):
      # print "i: " + str(i)
      # print "j: " + str(j) + "\n"
      if i != j and j != 0:
        OPT[i][j] = max(OPT[i-1][j], OPT[i-1][j-1]) + input[i][j]

  print max(OPT[len(OPT)-1])

def p71():
  def check_conditions(n, d, distance):
    a = hcf(n, d) == 1
    new_distance = (3.0/7) - float(n) / d
    b = new_distance < distance
    c = new_distance > 0.0
    return a and b and c

  distance = 1.0
  numerator = 1
  for d in xrange(1, 1000001):
    print d
    if d % 2 == 0:
      for n in xrange(1, d, 2):
        if check_conditions(n, d, distance):
          distance = (3.0 / 7) - float(n) / d
          numerator = n
    else:
      for n in xrange(1, d):
        if check_conditions(n, d, distance):
          distance = (3.0 / 7) - float(n) / d
          numerator = n

  print "numerator : %d" % numerator

def p72():
  num_reduced_fractions = 0
  for d in xrange(1, 1000001):
    if d % 2 == 0:
      for n in xrange(1, d, 2):
        if hcf(n, d) == 1:
          num_reduced_fractions += 1
    else:
      for n in xrange(1, d):
        if hcf(n, d) == 1:
          num_reduced_fractions += 1

  print "num_reduced_fractions : %d" % num_reduced_fractions

def p81():
  def readFile(filename):
    arr = []
    f = open(filename)
    for line in f:
      nums = map(int, line.split(','));
      arr.append(nums)
    return arr
  
  input = readFile("matrix.txt")
  OPT = []

  # create OPT table initialized to all 0
  for i in xrange(len(input)):
    arr = []
    for j in xrange(len(input)):
      arr.append(0)
    OPT.append(arr)

  # Recurrence Relation  
  # OPT[i][j] = min(OPT[i][j-1], OPT[i-1][j]) + input[i,j]

  # fill edge cases first
  for i in xrange(len(OPT)):
    if i == 0:
      OPT[i][i] = input[i][i]
    else:
      OPT[i][0] = OPT[i - 1][0] + input[i][0]
      OPT[0][i] = OPT[0][i-1] + input[0][i]

  # fill rest of OPT
  for i in xrange(1,len(OPT)):
    for j in xrange(1,len(OPT)):
      OPT[i][j] = min(OPT[i][j-1], OPT[i-1][j]) + input[i][j]

  print OPT[len(OPT) - 1][len(OPT) - 1]
  # print OPT[0][0]

def p92():
  seen_numbers = {}
  cnt_89 = 0
  for i in xrange(2, 10000000):
    chain = number_chain(i, seen_numbers)
    ending_num = chain[-1]
    if ending_num == 89:
      cnt_89 += 1
    if len(chain) > 1:
      for n in chain[:-1]:
        seen_numbers[n] = ending_num
    # if i % 100000 == 0: print i 
  print "cnt_89 : %d" % cnt_89
  print "dictionary size : %d" % len(seen_numbers)

    
  

##############################################################################
t1 = time.time()

p92()

print "<Finished in " + str(time.time() - t1) + " seconds.>"









