import re
f = open('FinalAESOP.txt',"r")
op = open('output.txt',"r+")

normalisedinputfile=''

def Find_Length_of_Text(txtfile):
    rawinputfile=f.read()
    global normalisedinputfile
    
    n=len(rawinputfile)
    urls=open('urls.txt',"r+")
    s=re.findall(r'(https?://[^\s]+|ftp://[^\s]+)', rawinputfile)
    for i in s:
        urls.write(i+'\n')
    i=0
    while(i<n):
        if(rawinputfile[i]==" "):
             normalisedinputfile=normalisedinputfile.__add__(" ")
             i=i+1
             while(rawinputfile[i]==" "):
                 i=i+1

        else:
            normalisedinputfile=normalisedinputfile.__add__(rawinputfile[i])
            i=i+1
    normalisedinputfile=re.sub(r'(https?://[^\s]+|ftp://[^\s]+)','', normalisedinputfile, flags=re.MULTILINE)	
    op.write(normalisedinputfile)
    return len(normalisedinputfile)

def  Find_Pattern(pattern, InTextRange, algo,text):
    #some code to support multiple formats of InTextRange
    return len(algo(pattern, InTextRange,text))

def Build_Cross_Index(txtfile, algo):
	def stripPunctuations(word):
		retWord=''
		for char in word:
			if(char.isalnum()):
				retWord=retWord+char
		return retWord
	fileasString=txtfile.read()
	n=len(fileasString)
	words=list(set(map(stripPunctuations,fileasString.split())))
	words.sort()
	words=list(map(lambda x: (x,len(algo(x,(0,n,"indices"),fileasString))),words))
	print(words)
def RabinKarp(pattern, InTextRange, text):
    shifts = []
    if (InTextRange[2] == "indices"):
        text = text[InTextRange[0]:InTextRange[1]]
    m = len(pattern)
    n = len(text)
    text = text + " "  # to prevent ListIndexOutOfRange
    d = 26  # the radix
    q = 101  # the prime
    h = pow(d, m - 1) % q
    hashes = []
    p = 0  # hash of the pattern
    t = 0  # hash of the first substring of text
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
   
    for s in range(n - m + 1):
        if p == t:  # hashes match
            if (pattern == text[s:s + m]):
                shifts.append(s)
        # compute next hash
        
        t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q  # remove first letter

    return shifts


def ComputePrefixFunction(pattern):
    m = len(pattern)
    CPF = [None] * (m)

    CPF[0] = 0
    k = 0
    for q in range(1, m):
        while (k > 0 and pattern[k] != pattern[q]):
            k = CPF[k]
        if (pattern[k] == pattern[q]):
            k = k + 1
        CPF[q] = k
    return CPF


def Knuth_Morris_Pratt(pattern, InTextRange, text):
    shifts = []
    # compute all shifts and .append it to shifts
    if (InTextRange[2] == "indices"):
        text = text[InTextRange[0]:InTextRange[1]]

    CPF = ComputePrefixFunction(pattern)
    # print("lps :",lps[:])

    n = len(text)
    m = len(pattern)

    q = 0  # no of matched chararcters ;

    if (m == 0 or n == 0):
        return 0

    for i in range(n):

        while (q > 0 and pattern[q] != text[i]):
            q = CPF[q]
        if pattern[q] == text[i]:
            q = q + 1

        if q == m:
            shifts = shifts + [i - m + 1]
            q = CPF[q - 1]

    # print(shifts)
    return shifts
class SuffixTreeArray(object):
	def __init__(self,s):
		SuffArray=[]
		self.LCP=[]
		self.n=len(s)
		self.s=s
		for i in range(len(s)):
			SuffArray.append((s[i:],i))
		
		self.SA=sorted(SuffArray,key=lambda x: str.upper(x[0]))
		for i in range(len(self.SA)-1):
			zipOfStrings=list(zip(self.SA[i][0],self.SA[i+1][0]))
			
			i=0
			match=False
			while(i<len(zipOfStrings)and match==False ):
				if(zipOfStrings[i][0]!=zipOfStrings[i][1]):
					self.LCP.append(i)
					match=True
				elif(i==len(zipOfStrings)-1):
					self.LCP.append(i+1)
				i=i+1
	def matchpatterns(self,s):
		shifts = set()
		lo=0
		hi=self.n-1
		lens=len(s)
		ind=-1
		while(lo<=hi):
			mid=(lo+hi)//2
			mem=self.SA[mid][0]
			
			
			if(mem[0:lens]==s):
				ind=mid
				break
			elif str.upper(mem)>str.upper(s):
				hi=mid-1
			else:
				lo=mid+1
			#print(lo,hi,mid)
			#print(mem,s)
		if ind!=-1:
			lowindex=ind
			while(lowindex>=0 and str.upper(self.SA[lowindex][0][0:lens])==str.upper(s)):
				if self.SA[lowindex][0][0:lens]==s:
					shifts.add(self.SA[lowindex][1])
				lowindex=lowindex-1
			
			highindex=ind
			while(highindex<self.n and str.upper(self.SA[highindex][0][0:lens])==str.upper(s)):
				if self.SA[highindex][0][0:lens]==s:
					shifts.add(self.SA[highindex][1])
				highindex=highindex+1
			
			
			#for i in range(lowindex,highindex+1):
				#shifts.append(self.SA[i][1])
			
		return(sorted(list(shifts),key=lambda x: x))
	def maxpalindrome(self,size):
		palindromes=[]
		s=self.s
		sRev=s[::-1]
		SuffArray=[]
		for i in range(len(s)):
			SuffArray.append((s[i:],i,"str"))
		for i in range(len(sRev)):
			SuffArray.append((sRev[i:],i,"rev"))
		SuffArray=sorted(SuffArray,key=lambda x: str.upper(x[0]))
		#print(SuffArray)
		LCP=[]
		for i in range(len(SuffArray)-1):
			#print(SuffArray[i][2],SuffArray[i+1][2])
			if(SuffArray[i][2]==SuffArray[i+1][2]):
				LCP.append(0)
			else:
				zipOfStrings=list(zip(SuffArray[i][0],SuffArray[i+1][0]))
				
				i=0
				match=False
				while(i<len(zipOfStrings)and match==False ):
					if(zipOfStrings[i][0]!=zipOfStrings[i][1]):
						LCP.append(i)
						match=True
					elif(i==len(zipOfStrings)-1):
						LCP.append(i+1)
					i=i+1
		#print(LCP)
		for i in range(len(LCP)):
			if(LCP[i]>=size and SuffArray[i][0][:LCP[i]]==SuffArray[i][0][:LCP[i]][::-1]):
				palindromes.append(SuffArray[i][0][:LCP[i]])
		return(palindromes)
	
def ST(pattern, InTextRange, text):
    # compute all shifts and .append it to shifts
	if (InTextRange[2] == "indices"):
		text = text[InTextRange[0]:InTextRange[1]]
	tree=SuffixTreeArray(text)
		
	return tree.matchpatterns(pattern)
def palindrome(text,no):
    tree=SuffixTreeArray(text)
    print(tree.maxpalindrome(no))


"""
opp = open('test.txt',"r+")
Build_Cross_Index(opp, RabinKarp)
"""
#print(normalisedinputfile)
print("Length of input file after removing URLs",Find_Length_of_Text(op))
print("Input the range of indices")
lower=int(input())
upper=int(input())
print("Enter the text to be searched")
iptext=str(input())
print("Suffix Tree Matching\n",ST(iptext,(lower,upper,"indices"),normalisedinputfile))
print("Knuth_Morris_Pratt Matching\n",Knuth_Morris_Pratt(iptext,(lower,upper,"indices"),normalisedinputfile))
print("RabinKarp Matching\n",RabinKarp(iptext,(lower,upper,"indices"),normalisedinputfile))
print("Enter the limit for palindrome size")
palindrome(normalisedinputfile[lower:upper],int(input()))

