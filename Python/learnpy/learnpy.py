#!/usr/bin/python
# -*- coding: UTF-8 -*-


def ch1():
  pass
  
def ch8():
  # list 
  L1 = [] # 空列表
  L2 = [0, 1, 2, 3]
  L3 = ['abc', ['def', 'ghi']]
  
  L2[i]
  L3[i][j]
  L2[i:j]
  len(L2)
  L1 + L2  # 合并
  L2 * 3
  
  for x in L2 
  
  3 in L2
  
  L2.append(4)
  L2.extend([5, 6, 7])
  L2.sort()
  L2.index(1)
  L2.insert(I, X)
  L2.reverse()
  del L2[k]
  del L2[i:j]
  L2.pop()
  L2.remove(2)
  L2[i:j] = []
  L2[i] = 1
  L2[i:j] = [4, 5, 6]
  
  range(4)
  xrange(0, 4)
  L4 = [x**2 for x in range(5)] # 列表解析
  
  # dict
  D1 = {}
  D2 = {'spam':2, 'eggs':3}
  D3 = {'food':{'ham': 1, 'egg':2}}
  D2['eggs']
  D3['food']['ham']
  
  D2.has_key('egg')
  'eggs' in D2
  D2.keys()
  D2.values()
  D2.copy()
  D2.get(key, default)
  D2.upda(D1)
  D2.pop(key)
  len(D1)
  D2[key] = 42
  del D2[key]
  D4 = dict.fromkeys(['a', 'b'])
  D5 = dict(zip(keyslist, valslist))
  D6 = dict(name='Bob', age=42)
  
  
  

def main():
  ch1()


if __name__=="__main__":
  main()