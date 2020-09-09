import eel
from subprocess import Popen, PIPE
# Set web files folder
eel.init('web')
string = ''

@eel.expose
def start_algorithm(n,p):
    # print(n,p)
    global string
    string  = ''
    m, s = matrix_product(p)
      
    print_parenthesization(s, 1, int(n))
   
    result_dict = {
        "result" : m[1][int(n)],
        "string" : string

    }
    
    return (result_dict)


def print_parenthesization(s, start, end):
    global string
    if start == end:
      
        string += ' A{} '.format(str(start))
        return 
 
    k = s[start][end]
 
   
    string += '('
    print_parenthesization(s, start, k)
    print_parenthesization(s, k + 1, end)
   
    string += ')'
    
    return string
    
def matrix_product(p):
    length = len(p) # len(p) = number of matrices + 1
     
    m = [[-1]*length for _ in range(length)]
    s = [[-1]*length for _ in range(length)]
 
    matrix_product_helper(p, 1, length - 1, m, s)
 
    return m, s

def matrix_product_helper(p, start, end, m, s):
    
    if m[start][end] >= 0:
        return m[start][end]
 
    if start == end:
        q = 0
    else:
        # It acts as an unbounded upper value for comparison. This is useful for finding lowest values for something.
        q = float('inf')
        for k in range(start, end):
            #cost[i,j] = min {c[i,k] + c[k+1,j] + d(i-1) * d(k) * d(j)}
            temp = (matrix_product_helper(p, start, k, m, s) + matrix_product_helper(p, k + 1, end, m, s) + (int(p[start - 1])*int(p[k])*int(p[end])))
            if q > temp:
                q = temp
                s[start][end] = k
 
    m[start][end] = q
    return q

eel.start('index.html', size=(1000, 600))
