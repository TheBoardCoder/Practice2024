# using a dictionary  joel moore 4 october 2017

'''
program illustrates the use of a dictionary in counting the occurances of
the letter in a phrase
testing github
'''
def main2():
  print('hello world')
  

def hist(phrase):
  d = dict()
  for i in phrase:
    d[i] = d.get(i, 0)+1
  return d  

def main():
  main2()
  phrase = input('enter a phrase ')
  
  count = hist(phrase)
  print(count)

main() 


