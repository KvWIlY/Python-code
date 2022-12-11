from functools import reduce                                                                                                      

n = int(input('Digite o valor para encontrar o fibonacci: '))                                                                    
fibonacci = reduce(lambda x, y: x + [x[-2] + x[-1]], range(n-2), [0, 1])   
print(fibonacci)                                                        