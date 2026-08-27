
#exercise 1
class CountDown:

    def __init__(self,num):
        self.num=num


    def __iter__(self):
        pass
        return self

    def __next__(self):
        if self.num>=1:
            num=self.num
            self.num-=1
            return num

        raise StopIteration



ct=CountDown(10)

print(next(ct))
print(next(ct))
print(next(ct))
print(next(ct))
print(next(ct))
print(next(ct))
print(next(ct))
print(next(ct))
print(next(ct))
print(next(ct))
print(next(ct))




#exercise 2

def even_numbers(n):
 for i in range(n+1):
    if(i%2==0):

     yield i

evens=even_numbers(10)
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))


#exercise 3


odd_squares=(n**2 for n in range(21) if n%2!=0 )
print(next(odd_squares))
print(next(odd_squares))
print(next(odd_squares))
print(next(odd_squares))
print(next(odd_squares))
print(next(odd_squares))
print(next(odd_squares))
print(next(odd_squares))
    
        
    