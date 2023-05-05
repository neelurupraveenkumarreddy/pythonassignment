# printing an roman number form of an integer
ones=['','I','II','III','IV','V','VI','VII','VIII','IX']
tens=['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
huns=['','C','CC','CCC','CD','D','DC','DCC','DCCC','DM']
thus=['','M','MM','MMM']
k=input()
if len(k)==2:
    k="00"+k 
elif len(k)==1:
    k="000"+k 
elif len(k)==3:
    k='0'+k
o=int(k[-1])
t=int(k[-2])
h=int(k[-3])
th=int(k[-4])
s=thus[th]+huns[h]+tens[t]+ones[o]
print(s)
