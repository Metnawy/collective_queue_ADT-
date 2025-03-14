
import copy
from collections.abc import Iterable
from functools import total_ordering
import random 


class collective_queue:
    #no initialization method we will discuss here how could do instatsiation or may be using methods from it directly or using static/class methods
    
    def enqueue(self):
        raise NotImplementedError("no implementation in ADT level")

    def dequeue(self):
        raise NotImplementedError("no implementation in ADT level")
    
    def clear(self):
       raise NotImplementedError("no implementation in ADT level")

    def order_with_change(self):
       raise NotImplementedError("no implementation in ADT level")
 

    def merge_with_change(self):
        raise NotImplementedError("no implementation in ADT level")
 

    def traverse(self):
       raise NotImplementedError("no implementation in ADT level")

    def __iter__(self):
        raise NotImplementedError("no implementation in ADT level")
 
    #def __repr__(self):
       # raise NotImplementedError("no implementation in ADT level")
     
    def size(self):
        raise NotImplementedError("no implementation in ADT level")
    
    def is_empty(self):
        raise NotImplementedError("no implementation in ADT level")
    def first(self):
       raise NotImplementedError("no implementation in ADT level")

    def last(self):
        raise NotImplementedError("no implementation in ADT level")
    
    def peek(self):
        
       raise NotImplementedError("no implementation in ADT level")
    def contains(self):
        raise NotImplementedError("no implementation in ADT level")

    def to_list(self):
        raise NotImplementedError("no implementation in ADT level")

    def copy(self):
        raise NotImplementedError("no implementation in ADT level")

    def reverse(self):
        raise NotImplementedError("no implementation in ADT level")

    @classmethod
    def from_iterable():
        ...

       
    @classmethod
    def merge_without_change():
        ...
    
       
    @classmethod
    def order_without_change():
        ...




class array_fixed_queue(collective_queue):
    """
    A fixed-size queue implementation using a dynamic list.

    This queue enforces a size limit and ensures that all elements are of a specified type.
    The queue grows dynamically but raises an error if the size limit is exceeded.

    Attributes:
        _limit (int): The maximum number of elements the queue can hold.
        _queue (list[T]): The list storing the elements of the queue.
        _type (type): The type of elements allowed in the queue.
    """
          
    def __init__(self,limit,the_type):
        if  not (isinstance(limit,int) and 0<=limit):
              raise Exception("there something wrong ")
        self._limit=limit
        self._queue=[]
        
        if the_type in (int,float,str,list,tuple,set,bool):
              self.the_type=the_type
        else:
              raise TypeError("that type of the queue elements isn't acceptable")
       

   
    
    def enqueue(self,data):
        """
        purpose:one of the core operations in the queue by adding a new consistant data at the ending of the queue
        arguments:data ...the supposed data to append to the end of the queue if it met the conditions 
        return:None 
        exception:raising index error if the queue is full OR type error of the new data isn't consistant with the acceptable type in the queue
        """
        if len(self._queue)==self._limit:
            raise IndexError("no available indeces to insert a new data")
        if not(type(data)==self.the_type):
            raise TypeError(f"type of {data}:{type(data)} isn't consistant with the declared type of that queue{self.the_type} ")
        self._queue.append(data)


    def dequeue(self):
        """
        purpose:returning the first value of the queue according to the approach FIFO
        arguments:no passed arguments in the interface calling 
        return: the value of the first inseration in the queue
        exception:indexerror if the queue is empty
        """
       
        if len(self._queue)==0:
             raise IndexError("the queue is empty")

        length=len(self._queue)

        value=self._queue[0]
        
        for i in range(length-1):
            self._queue[i]=self._queue[i+1]
        
        self._queue.pop()

        return value
         


    def clear(self):
        '''
        purpose:removing all elements of the queue
        return :an empty queue
        '''
        self._queue=[]
        return self


    def merge_with_change(self,second):
      '''
      purpose: merging the concerned queue with another queue
      args:the second iterable object to be merging it's value(with keeping the reference) with the first one
      considerations:
      we have two considerations each of them has many possible approaches to handle
      first one-the limit as by adding a new elements we could break the limit
      we have choose to edit the limit to at least accept the new data 
      second one - the unacceptable elements due to the inconsistancy of type here we have many sciearios if we already accepted
      some of that elements in the main/concerned queue 
      1st scenario accept just consistant elements from the iterable second object
      2nd scenario stop the process without reversing and rollback what is already have insearted 
      3rd scenario apply the principle take it all or leave it all by apply a rollback process 
      we choosed the the 3rd scenario ...no clear context related to the purpose to adopt this choice just what it has of complexity and challange

      return:the updated version of the queue if any changes have applied 
      '''
      
      try:
        iter(second)
        old_limit=self._limit
        if (len(self._queue)+len(second))<=self._limit:
            
            inseration_counter=0
            for i in second:
                if type(i)==self.the_type:
                    self._queue.append(i)
                    inseration_counter+=1
                    

                else:
                    #here we found defect element and started to apply take it all or leave it all principle and rollback process
                    for _ in range(inseration_counter):
                        self._queue.pop()
                        
                    self._limit=old_limit
                    break
            return self

        else:
      
            self._limit=len(self._queue)+len(second)
            inseration_counter=0
            for i in second:
                if type(i)==self.the_type:
                    self._queue.append(i)
                    inseration_counter+=1

                else:
                    #here we found defect element and started to apply take it all or leave it all principle and rollback process
                    for _ in range(inseration_counter):
                        self._queue.pop()
                        self._limit=old_limit
                    
                    break
            return self


      except :
          raise TypeError(f"the second object type is :{type(second)} it's not iterable ...the second should be iterable to merge it ")
      

    def merge_without_change(self,second):
      '''
      purpose: merging a copy of the concerned queue with another queue
      args:the second iterable object to be merging it's value(with keeping the reference) with the copy of  first one
      considerations:
      we have two considerations each of them has many possible approaches to handle
      first one-the limit as by adding a new elements we could break the limit
      we have choose to edit the limit to at least accept the new data 
      second one - the unacceptable elements due to the inconsistancy of type here we have many sciearios if we already accepted
      some of that elements in the main/concerned queue 
      1st scenario accept just consistant elements from the iterable second object
      2nd scenario stop the process without reversing and rollback what is already have insearted 
      3rd scenario apply the principle take it all or leave it all by apply a rollback process 
      we choosed the the 3rd scenario ...no clear context related to the purpose to adopt this choice just what it has of complexity and challange

      return:the updated version of the queue copy if any changes have applied 
      '''
        
      try:
        iter(second)
        new_copy=copy.deepcopy(self)
        old_limit=new_copy._limit
        if (len(new_copy._queue)+len(second))<=new_copy._limit:
            
            inseration_counter=0
            for i in second:
                if type(i)==new_copy.the_type:
                    new_copy._queue.append(i)
                    inseration_counter+=1
                    

                else:
                    #here we found defect element and started to apply take it all or leave it all principle and rollback process
                    for _ in range(inseration_counter):
                        new_copy._queue.pop()
                        
                    new_copy._limit=old_limit
                    break
            return new_copy

        else:
      
            new_copy._limit=len(new_copy._queue)+len(second)
            inseration_counter=0
            for i in second:
                if type(i)==new_copy.the_type:
                    new_copy._queue.append(i)
                    inseration_counter+=1

                else:
                    #here we found defect element and started to apply take it all or leave it all principle and rollback process
                    for _ in range(inseration_counter):
                        new_copy._queue.pop()
                        new_copy._limit=old_limit
                    
                    break
            return new_copy


      except :
          raise TypeError(f"the second object type is :{type(second)} it's not iterable ...the second should be iterable to merge it ")
    
    def traverse(self):
        '''
        purpose:presents another version of the __str__ method in another way 
        '''
        if not self._queue:
            return None

        for index,node in enumerate(self._queue):

            print(f"at index:{index+1}   the value is:{node}")

    def elements(self):
        '''
        purpose:returning a queue of all elements 
        '''
        return self._queue

    def __iter__(self):
        '''
        purpose:returning iterable objext to work with for loop,iter(),next()
        '''
        for i in self._queue:
            yield i

    def __repr__(self):
        '''
        purpose:showing the representation of the queue
        '''
        return f"{self._queue}"

    def size_actual_queue(self):
        #showing the actual no of elements in the queue
        return len(self._queue)
    
    def capacity(self):
        #the maximum acceptable elements in the queue
        return self._limit

    def is_empty(self):
        #check if the queue is empty or not 
        return not self._queue
    
    def first(self):
        #returning the first element without removing it 
        if not self._queue:
            raise IndexError("the queue is empty")
        return self._queue[0]
    
    def last(self):
        #returning the last element without removing it 
        if not self._queue:
            raise IndexError("the queue is empty")
        return self._queue[-1]


    def contains(self,value):
         '''
         purpose:searching if specific element exists in a queue or not 
         arguments:the value which we want to exist it's existance
         return :true or false
         '''
         if not self._queue:
             return False
         if type(value)!=self.the_type:
             return False
         for i in self._queue:
             if i==value:
                 return True
             
         return False

    def copy(self):
        #return a copy queue of that queue
        new_copy=copy.deepcopy(self)
        return new_copy

    def reverse_without_change(self):
        '''
        purpose :this method is concerned to reverse any linear/sequintial data structure but as we are working in the context of queue which 
        is built in the approach FIFO we won't apply it on the main queue but another independant copy of it
        exceptions: value error if the queue is empty
        return :the reversed version of the main queue
        '''
        if not self._queue:
            new_copy=copy.deepcopy(self)
            return new_copy
        
        new_copy=copy.deepcopy(self)

        iteration=len(new_copy._queue)//2

        left_curser=0
        right_curser=-1

        for _ in range(iteration):
            new_copy._queue[left_curser],new_copy._queue[right_curser]=new_copy._queue[right_curser],new_copy._queue[left_curser]
            left_curser+=1
            right_curser-=1

        return new_copy

        
        

    def order_without_change(self,the_type):
      '''
        purpose:as part of our considering the main nature of queue is FIFO ... when we are in need to have an ordered version of the queue we
        create a copy and apply that on it 

        arguments :either d/a  d:desceeding ordering ...a:ascednding ordering
        return :and ordered copy of the queue
        exceptions:
        '''
      new=copy.deepcopy(self)
      if not new._queue:
            return new
      if not (the_type,str) or not(the_type=="d" or the_type=="a"):
            raise TypeError
        
      if the_type=="a":
        def sort_merge(the_list,right_side,left_side):
            left_start=left_side[0]
            left_end=left_side[1]
            right_start=right_side[0]
            right_end=right_side[1]
            def swap(the_list,index,right_start,right_end):
            
              while index<right_end:
                    if the_list[index]>the_list[right_start]:
                        the_list[index],the_list[right_start]=the_list[right_start],the_list[index]
                        index=right_start
                        right_start+=1
                         
                        
                    else:
                        return
              return
                    
            if not  the_list[left_end]<=the_list[right_start]:

                for i in range(left_start,left_end+1):
                    swap(the_list,i,right_start,right_end)


            return [left_start,right_end]


        def helper(the_list,start,end):
            if (end-start)==0:
                return [start,start]
            mid=(end+start)//2
            left_side=helper(the_list,start,mid)
            right_side=helper(the_list,mid+1,end)
            return sort_merge(the_list,right_side,left_side)
        
        helper(new._queue,0,len(new._queue)-1)

        return new
      
      else:
        def sort_merge(the_list,right_side,left_side):
            left_start=left_side[0]
            left_end=left_side[1]
            right_start=right_side[0]
            right_end=right_side[1]
            def swap(the_list,index,right_start,right_end):
            
              while index<right_end:
                    if the_list[index]<the_list[right_start]:
                        the_list[index],the_list[right_start]=the_list[right_start],the_list[index]
                        index=right_start
                        right_start+=1
                         
                        
                    else:
                        return
              return
                    
            if not  the_list[left_end]>=the_list[right_start]:

                for i in range(left_start,left_end+1):
                    swap(the_list,i,right_start,right_end)


            return [left_start,right_end]


        def helper(the_list,start,end):
            if (end-start)==0:
                return [start,start]
            mid=(end+start)//2
            left_side=helper(the_list,start,mid)
            right_side=helper(the_list,mid+1,end)
            return sort_merge(the_list,right_side,left_side)
        
        helper(new._queue,0,len(new._queue)-1)

        return new

    def max(self):
        return max(self._queue)

    def min(self):
        return min(self._queue)

    def access_without_delete(self,index):
        if not isinstance(index,int):
            raise TypeError("the index to access the node value should be intger")

        if not (0<=index<=len(self._queue)-1):
            raise IndexError("the index is out of range")

        return self._queue[index]

    def change_element(self,index,value):
        if not isinstance(index,int):
            raise TypeError("the index should be intger")
        if len(self._queue)-1<index or index<0:#it's a vailable to use negative indices but we will restrict it in the non-negative indices to avoid the unintended flaws
            raise IndexError("the index doesn't exist")
        
        if type(value)!=self.the_type:
            raise TypeError("this value type isn't consistant with the queue type ")
        self._queue[index]=value
        

    #the comparsion methods 
    #these methods are defined as built-in ,,but here we will change the approach of the comparsion which is based on [IS] operator
    #we will adopt anothor approach based in a wider view making the equivilance is based on the value in abstract not the place on memory .


    def __eq__(self, second):

        if not isinstance(second,array_fixed_queue):
            return False
        
        if not (self.the_type==second.the_type):
            return False
        
        return self._queue==second._queue
        
        
    
    def __ne__(self,second):
        return not self==second
    def __lt__(self,second):
           
        if not isinstance(second,array_fixed_queue):
            raise TypeError(f"< ioerator should compare instances from the same class")
        
        if not (self.the_type==second.the_type):
            raise ValueError("both instances aren't consistant in the type of elements to use (<)")
        
        return self._queue<second._queue
    
    def __le__(self,second):
        if not isinstance(second,array_fixed_queue):
            raise TypeError(f"<= ioerator should compare instances from the same class")
        
        if not (self.the_type==second.the_type):
            raise ValueError("both instances aren't consistant in the type of elements to use (<=)")
        
        return self._queue<=second._queue
    def  __gt__(self,second):
        if not isinstance(second,array_fixed_queue):
            raise TypeError(f"> ioerator should compare instances from the same class")
        
        if not (self.the_type==second.the_type):
            raise ValueError("both instances aren't consistant in the type of elements to use (>)")
        
        return self._queue>second._queue
    def __ge__(self,second):
        if not isinstance(second,array_fixed_queue):
            raise TypeError(f">= ioerator should compare instances from the same class")
        
        if not (self.the_type==second.the_type):
            raise ValueError("both instances aren't consistant in the type of elements to use (>=)")
        
        return self._queue>=second._queue

    def __len__(self):
        return len(self._queue)
    
      

class array_dynamic_queue(collective_queue):
    """
    A dynamic size queue implementation using a dynamic list.

    This queue doesn't enforce a size limit 
    it ensures that all elements are of a specified type.


    Attributes:
        _queue (list[T]): The list storing the elements of the queue.
        _type (type): The type of elements allowed in the queue.
    """
          
    def __init__(self,the_type):

        self._queue=[]
        
        if the_type in (int,float,str,list,tuple,set,bool):
              self.the_type=the_type
        else:
              raise TypeError("that type of the queue elements isn't acceptable")


    def enqueue(self,data):
        """
        purpose:one of the core operations in the queue by adding a new consistant data at the ending of the queue
        arguments:data ...the supposed data to append to the end of the queue if it met the conditions 
        return:None 
        exception:raising type error if the new data isn't consistant with the acceptable type in the queue
        """
        
        if not(type(data)==self.the_type):
            raise TypeError(f"type of {data}:{type(data)} isn't consistant with the declared type of that queue{self.the_type} ")
        self._queue.append(data)


    def dequeue(self):
        """
        purpose:returning the first value of the queue according to the approach FIFO
        arguments:no passed arguments in the interface calling 
        return: the value of the first inseration in the queue
        exception:indexerror if the queue is empty
        """
       
        if len(self._queue)==0:
             raise IndexError("the queue is empty")

        length=len(self._queue)

        value=self._queue[0]
        
        for i in range(length-1):
            self._queue[i]=self._queue[i+1]
        
        self._queue.pop()

        return value
         

    def clear(self):
        '''
        purpose:removing all elements of the queue
        return :an empty queue
        '''
        self._queue=[]
        return self

    def merge_with_change(self,second):
      '''
      purpose: merging the concerned queue with another queue
      args:the second iterable object to be merging it's value(with keeping the reference) with the first one
      considerations:
 
      the unacceptable elements due to the inconsistancy of type here we have many sciearios if we already accepted
      some of that elements in the main/concerned queue 
      1st scenario accept just consistant elements from the iterable second object
      2nd scenario stop the process without reversing and rollback what is already have insearted 
      3rd scenario apply the principle take it all or leave it all by apply a rollback process 
      we choosed the the 3rd scenario ...no clear context related to the purpose to adopt this choice just what it has of complexity and challange

      return:the updated version of the queue if any changes have applied 
      '''
      
      try:
            iter(second)
       
            
            inseration_counter=0
            for i in second:
                if type(i)==self.the_type:
                    self._queue.append(i)
                    inseration_counter+=1
                    

                else:
                    #here we found defect element and started to apply take it all or leave it all principle and rollback process
                    for _ in range(inseration_counter):
                        self._queue.pop()
                    return self
                        
                    
            return self

      except :
          raise TypeError(f"the second object type is :{type(second)} it's not iterable ...the second should be iterable to merge it ")

    
    def merge_without_change(self,second):
      '''
      purpose: merging a copy of the concerned queue with another queue
      args:the second iterable object to be merging it's value(with keeping the reference) with the copy of  first one
      considerations:
      the unacceptable elements due to the inconsistancy of type here we have many sciearios if we already accepted
      some of that elements in the main/concerned queue 
      1st scenario accept just consistant elements from the iterable second object
      2nd scenario stop the process without reversing and rollback what is already have insearted 
      3rd scenario apply the principle take it all or leave it all by apply a rollback process 
      we choosed the the 3rd scenario ...no clear context related to the purpose to adopt this choice just what it has of complexity and challange

      return:the updated version of the queue copy if any changes have applied 
      '''
        
      try:
            iter(second)
            new_copy=copy.deepcopy(self)
            inseration_counter=0
            for i in second:
                if type(i)==new_copy.the_type:
                    new_copy._queue.append(i)
                    inseration_counter+=1
                    

                else:
                    #here we found defect element and started to apply take it all or leave it all principle and rollback process
                    for _ in range(inseration_counter):
                        new_copy._queue.pop()
             
                    return new_copy
            return new_copy

      except :
          raise TypeError(f"the second object type is :{type(second)} it's not iterable ...the second should be iterable to merge it ")

    

    def traverse(self):
        '''
        purpose:presents another version of the __str__ method in another way 
        '''
        if not self._queue:
            return None

        for index,node in enumerate(self._queue):

            print(f"at index:{index+1}   the value is:{node}")

    
    
    def elements(self):
        '''
        purpose:returning a queue of all elements 
        '''
        return self._queue


    
    def __iter__(self):
        '''
        purpose:returning iterable objext to work with for loop,iter(),next()
        '''
        for i in self._queue:
            yield i

    def __repr__(self):
        '''
        purpose:showing the representation of the queue
        '''
        return f"{self._queue}"

    def size_actual_queue(self):
        #showing the actual no of elements in the queue
        return len(self._queue)
    

    def __len__(self):
        #get the length of the array with function len
        return len(self._queue)

    def is_empty(self):
        #check if the queue is empty or not 
        return not self._queue
    
    def first(self):
        #returning the first element without removing it 
        if not self._queue:
            raise IndexError("the queue is empty")
        return self._queue[0]
    
    def last(self):
        #returning the last element without removing it 
        if not self._queue:
            raise IndexError("the queue is empty")
        return self._queue[-1]


    def contains(self,value):
         '''
         purpose:searching if specific element exists in a queue or not 
         arguments:the value which we want to exist it's existance
         return :true or false
         '''
         if not self._queue:
             return False
         if type(value)!=self.the_type:
             return False
         for i in self._queue:
             if i==value:
                 return True
             
         return False


    
    def copy(self):
        #return a copy queue of that queue
        new_copy=copy.deepcopy(self)
        return new_copy

    def reverse_without_change(self):
        '''
        purpose :this method is concerned to reverse any linear/sequintial data structure but as we are working in the context of queue which 
        is built in the approach FIFO we won't apply it on the main queue but another independant copy of it
        exceptions: value error if the queue is empty
        return :the reversed version of the main queue
        '''
        if not self._queue:
            new_copy=copy.deepcopy(self)
            return new_copy
        
        new_copy=copy.deepcopy(self)

        iteration=len(new_copy._queue)//2

        left_curser=0
        right_curser=-1

        for _ in range(iteration):
            new_copy._queue[left_curser],new_copy._queue[right_curser]=new_copy._queue[right_curser],new_copy._queue[left_curser]
            left_curser+=1
            right_curser-=1

        return new_copy


    
    
    def order_without_change(self,the_type):
      '''
        purpose:as part of our considering the main nature of queue is FIFO ... when we are in need to have an ordered version of the queue we
        create a copy and apply that on it 

        arguments :either d/a  d:desceeding ordering ...a:ascednding ordering
        return :and ordered copy of the queue
        exceptions:raising type error if the user enter something other than d/a string characters 
        '''
      new=copy.deepcopy(self)
      if not new._queue:
            return new
      if not (the_type,str) or not(the_type=="d" or the_type=="a"):
            raise TypeError
        
      if the_type=="a":
        def sort_merge(the_list,right_side,left_side):
            left_start=left_side[0]
            left_end=left_side[1]
            right_start=right_side[0]
            right_end=right_side[1]
            def swap(the_list,index,right_start,right_end):
            
              while index<right_end:
                    if the_list[index]>the_list[right_start]:
                        the_list[index],the_list[right_start]=the_list[right_start],the_list[index]
                        index=right_start
                        right_start+=1
                         
                        
                    else:
                        return
              return
                    
            if not  the_list[left_end]<=the_list[right_start]:

                for i in range(left_start,left_end+1):
                    swap(the_list,i,right_start,right_end)


            return [left_start,right_end]


        def helper(the_list,start,end):
            if (end-start)==0:
                return [start,start]
            mid=(end+start)//2
            left_side=helper(the_list,start,mid)
            right_side=helper(the_list,mid+1,end)
            return sort_merge(the_list,right_side,left_side)
        
        helper(new._queue,0,len(new._queue)-1)

        return new
      
      else:
        def sort_merge(the_list,right_side,left_side):
            left_start=left_side[0]
            left_end=left_side[1]
            right_start=right_side[0]
            right_end=right_side[1]
            def swap(the_list,index,right_start,right_end):
            
              while index<right_end:
                    if the_list[index]<the_list[right_start]:
                        the_list[index],the_list[right_start]=the_list[right_start],the_list[index]
                        index=right_start
                        right_start+=1
                         
                        
                    else:
                        return
              return
                    
            if not  the_list[left_end]>=the_list[right_start]:

                for i in range(left_start,left_end+1):
                    swap(the_list,i,right_start,right_end)


            return [left_start,right_end]


        def helper(the_list,start,end):
            if (end-start)==0:
                return [start,start]
            mid=(end+start)//2
            left_side=helper(the_list,start,mid)
            right_side=helper(the_list,mid+1,end)
            return sort_merge(the_list,right_side,left_side)
        
        helper(new._queue,0,len(new._queue)-1)

        return new
    


    def max(self):
        if not self._queue:
            return ValueError("this array is empty no value to be the maximum")

        if len(self._queue)==1:
            return self._queue[0]

        curser=self._queue[0]

        for i in range(1,len(self._queue)):
            if self._queue[i]>curser:
                curser=self._queue[i]

        return curser

    def min(self):
        if not self._queue:
            return ValueError("this array is empty no value to be the maximum")

        if len(self._queue)==1:
            return self._queue[0]

        curser=self._queue[0]

        for i in range(1,len(self._queue)):
            if self._queue[i]<curser:
                curser=self._queue[i]

        return curser


    def access_without_delete(self,index):
        if not isinstance(index,int):
            raise TypeError("the index to access the node value should be intger")

        if not (0<=index<=len(self._queue)-1):
            raise IndexError("the index is out of range")

        return self._queue[index]

    def change_element(self,index,value):
        if not isinstance(index,int):
            raise TypeError("the index should be intger")
        if len(self._queue)-1<index or index<0:#it's a vailable to use negative indices but we will restrict it in the non-negative indices to avoid the unintended flaws
            raise IndexError("the index doesn't exist")
        
        if type(value)!=self.the_type:
            raise TypeError("this value type isn't consistant with the queue type ")
        self._queue[index]=value
        

    
    #the comparsion methods 
    #these methods are defined as built-in ,,but here we will change the approach of the comparsion which is based on [IS] operator
    #we will adopt anothor approach based in a wider view making the equivilance is based on the value in abstract not the place on memory .


    def __eq__(self, second):

        if not isinstance(second,array_fixed_queue):
            return False
        
        if not (self.the_type==second.the_type):
            return False
        
        return self._queue==second._queue
        
        
    
    def __ne__(self,second):
        return not self==second
    def __lt__(self,second):
           
        if not isinstance(second,array_fixed_queue):
            raise TypeError(f"< ioerator should compare instances from the same class")
        
        if not (self.the_type==second.the_type):
            raise ValueError("both instances aren't consistant in the type of elements to use (<)")
        
        return self._queue<second._queue
    
    def __le__(self,second):
        if not isinstance(second,array_fixed_queue):
            raise TypeError(f"<= ioerator should compare instances from the same class")
        
        if not (self.the_type==second.the_type):
            raise ValueError("both instances aren't consistant in the type of elements to use (<=)")
        
        return self._queue<=second._queue
    def  __gt__(self,second):
        if not isinstance(second,array_fixed_queue):
            raise TypeError(f"> ioerator should compare instances from the same class")
        
        if not (self.the_type==second.the_type):
            raise ValueError("both instances aren't consistant in the type of elements to use (>)")
        
        return self._queue>second._queue
    def __ge__(self,second):
        if not isinstance(second,array_fixed_queue):
            raise TypeError(f">= ioerator should compare instances from the same class")
        
        if not (self.the_type==second.the_type):
            raise ValueError("both instances aren't consistant in the type of elements to use (>=)")
        
        return self._queue>=second._queue


    
@total_ordering
class array_circular_fixed_queue(collective_queue):
    """
     objectives:creating a subclass of collective queue ADT  with concerete data structure array 
     with specification of fixed size and circular nature in inseration and deletion to enhance the time complexity 
     with felixiblity in the type of the elements in the queue as first element type define the type accepted data in the recent 
     consideration:
     1-here we let the type of data acceptable at the instance of the class up to the first element in the instance 
     2-very important consideration i used as fundmental feature of the queue ...we will have two layers,,, one virtual represents
     the queue we inserted & deleted with tracking the timeline of inserations
     the second layer represents the actual data in memory where we won't delete any value in dequeue we just will drop it from the logic of 
     the concerned queue ..in enqueue if there were still space until the limit we append if we reached to the limit we check if there old deleted 
     elements from the logic layer ( still in actual memory ) and replace the new ones with them 


     note:may be this choice of having two layers of data one virtual(represents the intended queue)and another one is real ( repersents the data on memory )
     isn't the ideal practice in some terms but i am building it in that way as part of my training 
     """

    def __init__(self,limit):
        
        if  isinstance(limit,int) and (limit>0):
            self._limit=limit
        else :
            raise Exception("the limit should be intger more than 0")
        
        self._queue=[]
        self._type=None
        self._size=0
        self._first_index=None
        self._last_index=None


    def _real_index(self,index):
        if not isinstance(index,int):
            raise TypeError("the index should be intger object")
        real_index=self._first_index+index
        if real_index>self._limit-1:
            real_index=(real_index%self._limit)
            return real_index
        else:
            return real_index

    def enqueue(self,data):
        '''
        objectives:adding new element to the queue at the end of the array apply the main specification FIFO
        specifications:
          limit:we check the limit of the array 
          data consistancy :if the array isn't empty we should insure the type of the inserted data is the same as the self._type
        '''
        if not (self._size<self._limit):
            raise IndexError("the queue is full ..No space to add new element")
        
        if self._size==0:
            self._type=type(data)
            if not self._queue:
             
               self._queue.append(data)
            else:
                self._queue[0]=data
            self._size+=1
            self._first_index=0
            self._last_index=0
        else:
            if self._type==type(data):
               old_last_index=self._last_index
               self._last_index=(self._last_index+1)%self._limit
               if self._last_index>old_last_index:
                  if self._last_index>len(self._queue)-1:
                     self._queue.append(data)
                     
                  else:
                      self._queue[self._last_index]=data
               else:
                 
                   self._queue[self._last_index]=data

               self._size+=1
               
               

            else:
                raise ValueError(f"the inseration isn't acceptable due to the inconsistancy of it's type({type(data)}) and the acceptable data type ({self._type})")
            

   
    def dequeue(self):
        '''
        objective:poping out the first value in the queue according to the approach FIFO
        specification:we applying the circular specification on the array to save time of shifting data in that case 
        '''
        if self._size==0:
            raise IndexError("the queue is empty no values to dequeue")
        
        elif self._size==1:
            value=self._queue[self._first_index]
            self._size-=1
            self._first_index=None
            self._last_index=None
            self._type=None

            return value
        else:
            value=self._queue[self._first_index]
            self._first_index=(self._first_index+1)%self._limit
            self._size-=1

            return value
        

    def clear(self):

        self._queue=[]
        self._type=None
        self._size=0
        self._first_index=None
        self._last_index=None


    def order_without_change(self,the_type):
        '''
        objectives:ordering the queue in asceding way or descending way 
        consideration:due to the nature of the queue with considering the timeline of the each element inseration 
        we won't change the order of the origional queue but we will work on a copy of it .
        parameters:
         the_type:which should be either a (ascending) or d (descending)
        '''

        if 0<=self._size<=1:
            return copy.deepcopy(self) 
    
        if not the_type in ("a","d"):
            raise ValueError(f"the type shoud be either (a) represent ascending order or (b) represents descending ")
        
        new_queue=copy.deepcopy(self)

        if the_type=="a":#ascending version of the method 
            if new_queue._last_index<new_queue._first_index:#case of the distrubting of the concerned queue circullary on the array
                virtual_end=new_queue._limit+new_queue._last_index

                def merge(the_list,right_side,left_side):
                    first_left=left_side[0]
                    last_left=left_side[1]
                    first_right=right_side[0]
                    last_right=right_side[1]

                    pointer=first_left
                    def real_index(index):
                        if index>=new_queue._limit:
                            real_ind=index-new_queue._limit
                            return real_ind
                        else:
                            return index
                        
                    def on_right_side_swap(the_list,start,end):
                         pointer=start

                         while pointer<end:
                             if the_list[real_index(pointer)]<=the_list[real_index(pointer+1)]:
                                 return
                             else:
                                 the_list[real_index(pointer)],the_list[real_index(pointer+1)]=the_list[real_index(pointer+1)],the_list[real_index(pointer)]
                                 pointer+=1
                         return
                    while pointer<=last_left:
                          if not the_list[real_index(pointer)]<=the_list[real_index(first_right)]:
                             the_list[real_index(pointer)],the_list[real_index(first_right)]=the_list[real_index(first_right)],the_list[real_index(pointer)]
                             on_right_side_swap(the_list,first_right,last_right)

                             #comparing in the right side
                             pointer+=1
                          else:
                              pointer+=1

                    
                    return [first_left,last_right]
                def helper(the_list,start,end):
                    if start==end :
                        return [start,end]
                    mid=(start+end)//2
                    left_side=helper(the_list,start,mid)
                    right_side=helper(the_list,mid+1,end)
                    return merge(the_list,right_side,left_side)

                helper(new_queue._queue,new_queue._first_index,virtual_end)

                return new_queue

            
            else:
                #case of the distrubting of the concerned queue Normally on the array
           

                def merge(the_list,right_side,left_side):
                    first_left=left_side[0]
                    last_left=left_side[1]
                    first_right=right_side[0]
                    last_right=right_side[1]

                    pointer=first_left
                    
                        
                    def on_right_side_swap(the_list,start,end):
                         pointer=start

                         while pointer<end:
                             if the_list[pointer]<=the_list[pointer+1]:
                                 return
                             else:
                                 the_list[pointer],the_list[pointer+1]=the_list[pointer+1],the_list[pointer]
                                 pointer+=1
                         return
                    while pointer<=last_left:
                          if not the_list[pointer]<=the_list[first_right]:
                             the_list[pointer],the_list[first_right]=the_list[first_right],the_list[pointer]
                             on_right_side_swap(the_list,first_right,last_right)

                             #comparing in the right side
                             pointer+=1
                          else:
                              pointer+=1

                    
                    return [first_left,last_right]
                def helper(the_list,start,end):
                    if start==end :
                        return [start,end]
                    mid=(start+end)//2
                    left_side=helper(the_list,start,mid)
                    right_side=helper(the_list,mid+1,end)
                    return merge(the_list,right_side,left_side)

                helper(new_queue._queue,new_queue._first_index,new_queue._last_index)

                return new_queue
            


        else:#the ascending version of the method
            if new_queue._last_index<new_queue._first_index:#case of the distrubting of the concerned queue circullary on the array
                virtual_end=new_queue._limit+new_queue._last_index

                def merge(the_list,right_side,left_side):
                    first_left=left_side[0]
                    last_left=left_side[1]
                    first_right=right_side[0]
                    last_right=right_side[1]

                    pointer=first_left
                    def real_index(index):
                        if index>=new_queue._limit:
                            real_ind=index-new_queue._limit
                            return real_ind
                        else:
                            return index
                        
                    def on_right_side_swap(the_list,start,end):
                         pointer=start

                         while pointer<end:
                             if the_list[real_index(pointer)]>=the_list[real_index(pointer+1)]:
                                 return
                             else:
                                 the_list[real_index(pointer)],the_list[real_index(pointer+1)]=the_list[real_index(pointer+1)],the_list[real_index(pointer)]
                                 pointer+=1
                         return
                    while pointer<=last_left:
                          if not the_list[real_index(pointer)]>=the_list[real_index(first_right)]:
                             the_list[real_index(pointer)],the_list[real_index(first_right)]=the_list[real_index(first_right)],the_list[real_index(pointer)]
                             on_right_side_swap(the_list,first_right,last_right)

                             #comparing in the right side
                             pointer+=1
                          else:
                              pointer+=1

                    
                    return [first_left,last_right]
                def helper(the_list,start,end):
                    if start==end :
                        return [start,end]
                    mid=(start+end)//2
                    left_side=helper(the_list,start,mid)
                    right_side=helper(the_list,mid+1,end)
                    return merge(the_list,right_side,left_side)

                helper(new_queue._queue,new_queue._first_index,virtual_end)

                return new_queue

            
            else:
                #case of the distrubting of the concerned queue Normally on the array
           

                def merge(the_list,right_side,left_side):
                    first_left=left_side[0]
                    last_left=left_side[1]
                    first_right=right_side[0]
                    last_right=right_side[1]

                    pointer=first_left
                    
                        
                    def on_right_side_swap(the_list,start,end):
                         pointer=start

                         while pointer<end:
                             if the_list[pointer]>=the_list[pointer+1]:
                                 return
                             else:
                                 the_list[pointer],the_list[pointer+1]=the_list[pointer+1],the_list[pointer]
                                 pointer+=1
                         return
                    while pointer<=last_left:
                          if not the_list[pointer]>=the_list[first_right]:
                             the_list[pointer],the_list[first_right]=the_list[first_right],the_list[pointer]
                             on_right_side_swap(the_list,first_right,last_right)

                             #comparing in the right side
                             pointer+=1
                          else:
                              pointer+=1

                    
                    return [first_left,last_right]
                def helper(the_list,start,end):
                    if start==end :
                        return [start,end]
                    mid=(start+end)//2
                    left_side=helper(the_list,start,mid)
                    right_side=helper(the_list,mid+1,end)
                    return merge(the_list,right_side,left_side)

                helper(new_queue._queue,new_queue._first_index,new_queue._last_index)

                return new_queue
        

    def merge_with_change(self,second):
        '''
        objectives:mergeing  a new sequence of data with changing our main instance 
        consideration :
           FIFO:here is no harness of that principle due to the new data will append the old sequeuence as the newer ,the only difference in adding them as a chunck not just one element
           consistancy of data:
              here we have three choices:
                1-take it all or leave it all
                2-accept until have element with different type
                3-take only the consistant type
              i have choosed the first choice

            the-limitation:we will adopt the approach of adding elements until get the capcity is full 

            Note: we have tried to not stop the flow of the code when meeting inconsistant data in merging return we have merged or the original one as it's

        '''
        if isinstance(second,array_circular_fixed_queue):#case of the same array_circular_fixed_queue data type
            if self._size==0 and second._size==0:
                return self
            
            try :
                    for i in second:
                        self.enqueue(i)
            except Exception :
                    return self
                # we used try -except to avoid break the flow in case of any problem
            return self

        elif isinstance(second,Iterable):#case of iterable data type object
            if isinstance(second,dict):
                for i in second.items():# here we adding a tuple of key-value
                    try :
                        self.enqueue(i)

                
                    except Exception:
                        return self
            else:
                old_size=self._size
                for i in second:
                      
                    try :
                        self.enqueue(i)
                      
                    except ValueError:# applying the roll-back on  mixed sequences when finding in consistant value ...removing all previous added values
                        no_values=self._size-old_size
                        
                        while no_values:
                            if self._last_index!=0:
                               self._last_index-=1
                               self._size-=1
                               no_values-=1
                           
                            else:
                                self._last_index=self._limit-1
                                self._size-=1
                                no_values-=1
                   
                            
                        if self._size==0:
                             #here we handle the edge-case of merging empty object(array_circular) with another iterable object(with possibility of roll-back at any point of insertion due it's mix not one data type)
                             #in case of roll-back we decrease self._size which increased with the inserations ,,if self._size after that equals zero this means the original
                             # was empty and by applying the following we assure we removed any changes in the basic attributes 
                             self._queue=[]
                             self._type=None
                             self._size=0
                             self._first_index=None
                             self._last_index=None
                        return self
                    except Exception:
                        return self
                    
            return self

        else:# not suitable for iterating data type
            raise TypeError("the type of the argument isn't suitable ...it should be iterable")
    
    def merge_without_change(self,second):
        '''
        objectives:mergeing  a new sequence of data with changing our main instance 
        consideration :
           FIFO:here is no harness of that principle due to the new data will append the old sequeuence as the newer ,the only difference in adding them as a chunck not just one element
           consistancy of data:
              here we have three choices:
                1-take it all or leave it all
                2-accept until have element with different type
                3-take only the consistant type
              i have choosed the first choice

            the-limitation:we will adopt the approach of adding elements until get the capcity is full 

            Note: we have tried to not stop the flow of the code when meeting inconsistant data in merging return we have merged or the original one as it's

        '''
        
        if isinstance(second,array_circular_fixed_queue):#case of the same array_circular_fixed_queue data type
            if self._size==0 and second._size==0:
                return self
            first=copy.deepcopy(self)
            try :
                    for i in second:
                        first.enqueue(i)
            except Exception :
                    return first
                # we used try -except to avoid break the flow in case of any problem
            return first

        elif isinstance(second,Iterable):#case of iterable data type object
            first=copy.deepcopy(self)
            if isinstance(second,dict):
                for i in second.items():# here we adding a tuple of key-value
                    try :
                        first.enqueue(i)

                
                    except Exception:
                        return first
            else:
                old_size=first._size
                for i in second:
                      
                    try :
                        first.enqueue(i)
                      
                    except ValueError:# applying the roll-back on  mixed sequences when finding in consistant value ...removing all previous added values
                        no_values=first._size-old_size
                        
                        while no_values:
                            if first._last_index!=0:
                               first._last_index-=1
                               first._size-=1
                               no_values-=1
                           
                            else:
                                first._last_index=first._limit-1
                                first._size-=1
                                no_values-=1
                   
                            
                        if first._size==0:
                             #here we handle the edge-case of merging empty object(array_circular) with another iterable object(with possibility of roll-back at any point of insertion due it's mix not one data type)
                             #in case of roll-back we decrease self._size which increased with the inserations ,,if self._size after that equals zero this means the original
                             # was empty and by applying the following we assure we removed any changes in the basic attributes 
                             first._queue=[]
                             first._type=None
                             first._size=0
                             first._first_index=None
                             first._last_index=None
                        return first
                    except Exception:
                        return first
                    
            return first

        else:# not suitable for iterating data type
            raise TypeError("the type of the argument isn't suitable ...it should be iterable")
    

    def __iter__(self):
        if self._size==0:
            #here my approach to handle the empty queue with __iter__
            #i didn't raise error to not stop the flow of the code or return none because it's at the end it's a value .. i prefered to return NOTHING 

            for i in range(0,0):
                yield
        elif self._last_index>=self._first_index:
            for i in range(self._first_index,self._last_index+1):
                yield self._queue[i]
        else:
             pointer1=self._first_index
             while pointer1<self._limit:
                 yield self._queue[pointer1]
                 pointer1+=1

             pointer2=0
             while pointer2<=self._last_index:
                 yield self._queue[pointer2]
                 pointer2+=1

    def traverse(self):
        if self._size==0:
            return None
        if self._last_index<self._first_index:
            general_index=0
            poniter1=self._first_index
            while poniter1<self._limit:
                print(f"at the index:{general_index}....the value is:{self._queue[poniter1]}")
                general_index+=1
                poniter1+=1

            poniter2=0      
            while poniter2<=self._last_index:
                print(f"at the index:{general_index}....the value is:{self._queue[poniter2]}")
                general_index+=1
                poniter2+=1



        else:
            for index,element in enumerate(range(self._first_index,self._last_index+1)):
                print(f"at the index:{index}....the value is:{self._queue[element]}")

    def queue(self):
        '''
        objectives:retuen a list of the queue in the intended sequenece
        '''
       
        if self._size==0:
            return []
        
        considered=[]
        if self._last_index<self._first_index:
            
            poniter1=self._first_index
            while poniter1<self._limit:
                considered.append(self._queue[poniter1])
                
                poniter1+=1

            poniter2=0      
            while poniter2<=self._last_index:
                considered.append(self._queue[poniter2])
                poniter2+=1



        else:
            for element in range(self._first_index,self._last_index+1):
                considered.append(self._queue[element])

        return considered

    def enforcing_change_of_sequenece_two_elements(self,index1,index2):
        '''
        ALERT: we use this method in rare exceptional cases and needs ..it's against the default behaviour of the queue
        objectives:swapping the sequences of two elements in the queue
        inputs:index1,index2 two intgers on the array range 

        '''
        if not (isinstance(index1,int) and isinstance(index2,int)):
            raise TypeError(f"both of indeces {index1,index2} should be intgers")
        if not (0<=index1<=self._size-1 and 0<=index2<=self._size-1):
            raise IndexError(f"both indeces{index1,index2} should be in the range of (0,{self._size-1})")
        in1=self._real_index(index1)
        in2=self._real_index(index2)
        self._queue[in1],self._queue[in2]=self._queue[in2],self._queue[in1]
        

    def enforcing_change_of_sequence_by_chunk(self,index1,index2,ref):
            """
        ALERT: we use this method in rare exceptional cases and needs ..it's against the default behaviour of the queue
        objective:change the position of a chunck of elements according specfic reference index either before or after

            """
            if not (isinstance(index1,int) and isinstance(index2,int) and isinstance(ref,int)):
                raise TypeError(f"all indeces {index1,index2,ref} should be intgers")
        
            if  not (index1!=index2 and index1!=ref and index2!=ref):
               raise ValueError(f"{index1,index2,ref} shouldn't be reptatitve ")
        
            if  index1<ref<index2 or index2<ref<index1:
               raise ValueError(f"there is something wrong here prevent applying the method ..{ref} shouldn't between {index1,index2} ")
        
            if not (0<=index1<=self._size-1 and 0<=index2<=self._size-1 and 0<=ref<=self._size-1):
                raise IndexError(f"all of the concerned indeces ({index1,index2,ref}) should be in the range of ({0,self._size-1})")
        
 
            if index1>index2:
                index1,index2=index2,index1
            if index1==(ref+1):
                return self
            new=[]
            if 0<ref and index2<ref and 0<index1:#case1 the chunck before the ref and index1 greater than the start of the queue
                pointer=0
                while pointer<index1:
                    new.append(self._queue[self._real_index(0)])
                    pointe+=1

                if index2+1!=ref:
                    pointer=index2+1
                    while pointer<ref:
                        new.append(self._queue[self._real_index(pointer)])
                        pointer+=1
                index_after_ref=ref+1
                new.append(self._queue[self._real_index(ref)])
                pointer=index1
                while pointer<=index2:
                    new.append(self._queue[self._real_index(pointer)])
                    pointer+=1

                while len(new)<self._size:
                    new.append(self._queue[self._real_index(index_after_ref)])
                    index_after_ref+=1

                del self._queue
                self._queue=new
                self._first_index=0
                self._last_index=self._size-1

                return self 

            elif 0<ref and index2<ref and index1==0:#case2 the chunck before the ref and index1 equals the start of the queue
                new=[]
                if index2+1!=ref:
                    pointer=index2+1
                    while pointer<ref:
                        new.append(self._queue[self._real_index(pointer)])
                        pointer+=1

                index_after_ref=ref+1
                new.append(self._queue[self._real_index(ref)])
                pointer=index1
                while pointer<=index2:
                    new.append(self._queue[self._real_index(pointer)])
                    pointer+=1
                
                while len(new)<self._size:
                    new.append(self._queue[self._real_index(index_after_ref)])
                    index_after_ref+=1

                del self._queue
                self._queue=new
                self._first_index=0
                self._last_index=self._size-1

                return self
            
            else:#cases of chunck after the ref 
                    
                    if ref+1==index1:
                        return self
                    new=[]
                    if 0<ref:#the ref equals the start
                        pointer=0
                        while pointer<ref:
                            new.append(self._queue[self._real_index(pointer)])
                            pointer+=1
                    flag_ref_after=False
                    
                    if not ref+1==index1:
                       after_ref_start=ref+1
                       after_ref_end=index1-1
                       flag_ref_after=True
                    after_chunk=index2+1

                    new.append(self._queue[self._real_index(ref)])
                    pointer=index1

                    while pointer<=index2:
                        new.append(self._queue[self._real_index(pointer)])
                        pointer+=1

                    if flag_ref_after :
                        while after_ref_start<=after_ref_end:
                                new.append(self._queue[self._real_index(after_ref_start)])  
                                after_ref_start+=1

                    while len(new)<self._size:
                         new.append(self._queue[self._real_index(after_chunk)])  
                         after_chunk+=1
                    
                    del self._queue
                    self._queue=new
                    self._first_index=0
                    self._last_index=self._size-1

                    return self
                               

    def size_actual_queue(self):
        '''
        objectives:return the actual no of elements in the queue
        '''
        return self._size
        
    def __len__(self):
        return self._size
    
    def capacity(self):
        '''
        objectives:return the ceiling of the elements to have at the array
        '''
        return self._limit
    
    def copy(self):
        return copy.deepcopy(self)
    
    def is_empty(self):
        return True if not self._size else False
    
    def first(self):
        '''
        objectives :return the value of the first value in the array without removing it

        '''
        if not self._size:
            raise IndexError("the queue is empty no values in first or in another position to get it")
        return self._queue[self._first_index]
    def last(self):
        '''
        objectives :return the value of the lastvalue in the array without removing it

        '''
        if not self._size:
            raise IndexError("the queue is empty no values in last or in another position to get it")
        return self._queue[self._last_index]
    
    def __repr__(self):

        if self._size==0:
            return f"{[]}"
        actual_queue=[]
        pointer=self._first_index
        while len(actual_queue)<self._size:
              actual_queue.append(self._queue[pointer])
              pointer=(pointer+1)%self._limit
           
        return f"{actual_queue}"
    
    def contains(self,value):
         '''
         purpose:searching if specific element exists in a queue or not 
         arguments:the value which we want to exist it's existance
         return :true or false
         '''
         if not self._queue:
             return False
         if type(value)!=self._type:
             return False
         if self._last_index<self._first_index:
            
            poniter1=self._first_index
            while poniter1<self._limit:
                if value==self._queue[poniter1]:
                    return True
                poniter1+=1

            poniter2=0      
            while poniter2<=self._last_index:
                if value==self._queue[poniter2]:
                    return True
                poniter2+=1

         else:
            for index in range(self._first_index,self._last_index):
                if value==self._queue[index]:
                    return True
             
         return False

    def reverse_without_change(self):
        '''
        purpose :this method is concerned to reverse any linear/sequintial data structure but as we are working in the context of queue which 
        is built on the approach FIFO we won't apply it on the main queue but another independant copy of it
        exceptions: value error if the queue is empty
        return :the reversed version of the main queue
        
        if self._size==0:
            raise ValueError("there is no element in queue to reverse it's a copy")
        the_copy=copy.deepcopy(self)

        pointer1=0
        pointer2=the_copy._size-1
        the_mid=the_copy._size//2
        for _ in range(the_mid):
           the_copy._queue[the_copy._real_index(pointer1)],the_copy._queue[the_copy._real_index(pointer2)]=the_copy._queue[the_copy._real_index(pointer2)],the_copy._queue[the_copy._real_index(pointer1)]
           pointer1+=1
           pointer2-=1

        return the_copy '''
        the_copy=copy.deepcopy(self)
        mid=(the_copy._size-1)//2
        counter=0
        if the_copy._last_index<the_copy._first_index:
            pointer1=the_copy._first_index
            pointer2=the_copy._last_index
            
            while counter<=mid:
                the_copy._queue[pointer1],the_copy._queue[pointer2]=the_copy._queue[pointer2],the_copy._queue[pointer1]
                counter+=1
                if pointer1==(the_copy._limit-1):
                    pointer1=0

                else:
                    pointer1+=1

                if pointer2==0:
                    pointer2=the_copy._limit-1
                else: 
                    pointer2-=1

        else:
            pointer1=the_copy._first_index
            pointer2=the_copy._last_index
            
            while counter<=mid:
                the_copy._queue[pointer1],the_copy._queue[pointer2]=the_copy._queue[pointer2],the_copy._queue[pointer1]
                counter+=1
                pointer1+=1
                pointer2-=1


        return the_copy

    def max(self):
        '''
        purpose:finding the max value
        '''
        if self._size==0:
            raise ValueError("the queue is empty no elements to get the maximum")
        
        
        the_max=self._queue[self._first_index]

        if self._last_index<self._first_index:
            pointer1=self._first_index

            while pointer1<=(self._limit-1):
                if the_max<self._queue[pointer1]:
                    the_max=self._queue[pointer1]
                pointer1+=1

            pointer2=0

            while pointer2<=self._last_index:

                if the_max<self._queue[pointer2]:
                    the_max=self._queue[pointer2]
                pointer2+=1

        else:
            for i in range(self._first_index,self._last_index+1):
                if the_max<self._queue[i]:
                    the_max=self._queue[i]

        return the_max

    def min(self):
        '''
        purpose:finding the min value
        '''
        if self._size==0:
            raise ValueError("the queue is empty no elements to get the maximum")
        
        
        the_min=self._queue[self._first_index]

        if self._last_index<self._first_index:
            pointer1=self._first_index

            while pointer1<=(self._limit-1):
                if the_min>self._queue[pointer1]:
                    the_min=self._queue[pointer1]
                pointer1+=1

            pointer2=0

            while pointer2<=self._last_index:

                if the_min>self._queue[pointer2]:
                    the_min=self._queue[pointer2]
                pointer2+=1

        else:
            for i in range(self._first_index,self._last_index+1):
                if the_min>self._queue[i]:
                    the_min=self._queue[i]

        return the_min

    def access_without_delete(self,index):
        '''
        objective:accessing a specific element using it's index
        '''
        if not isinstance(index,int):
            raise TypeError("the index is out of range")
        if not (0<=index<=(self._size-1)):
            raise IndexError("the index is out of range")
        real_index=index+self._first_index
        if real_index>self._limit-1:
            real_index=(real_index%self._limit)
            
        return self._queue[real_index]
    

    def change_element(self,index,value):
        '''
        objective:accessing a specific element using it's index
        '''
        if not isinstance(index,int):
            raise TypeError("the index is out of range")
        if not (0<=index<=(self._size-1)):
            raise IndexError("the index is out of range")
        if not self._type==type(value):
            raise TypeError(f"we couldn't substitute this element with this the new value because it's type:{type(value)} not consistant with the dominant type in the queue:{self._type}")
        real_index=index+self._first_index
        if real_index>self._limit-1:
            real_index=(real_index%self._limit)
           
        self._queue[real_index]=value

    #here we define the special methods related to comparsion 
      # == ,!= by default mannar using is operator to implement those methods but i will use another approach hence the cretria will be the all values are the same in both queues 

    def __eq__(self, second):

        if not isinstance(second,array_circular_fixed_queue):
            return False
        return self.queue()==second.queue()
    
    def __ne__(self,second):
        if not isinstance(second,array_circular_fixed_queue):
            return False
        return self.queue()!=second.queue()
    
    def __lt__(self,second):

        if not isinstance(second,array_circular_fixed_queue):
            raise TypeError(f"the second element of comparsion from the same tyoe {array_circular_fixed_queue}")
            
        return self.queue()<second.queue()
    
        
@total_ordering 
class arrary_circular_dynamic_queue(collective_queue,Iterable):
    '''
    circular_dynamic:
    here we have two features with their very critical consequences on the structure of the code & the performance of the main operations
    1-circularity of filling the array as the omitted element we don't re-size the array we just put space holder(none) and a new enqueue could be in index on the concerete index before the the first order element of the queue in the concerte array 
    2-the dynamic -no limit- size 
    here we have a big hardship to track the sequence of inseration as we did in another cases (array_circular_fixed_queue)
    by such method:
        def _real_index(self,index):
        if not isinstance(index,int):
            raise TypeError("the index should be intger object")
        real_index=self._first_index+index
        if real_index>self._limit-1:
            real_index=(real_index%self._limit)
            return real_index
        else:
            return real_index

    becuase as example of that we could have array of 0-8 indices
    then 1,2 element in enqueue in 3,4 indices
         3,4 element in enqueue in 0,1 indices
         5,6 element in enqueue in 5,6 indices
         7   element in enqueue in 2   index 
         8,9 element in enqueue in 7,8 indices 

    all of that chaos comes from circularity with no-limit size ,which push us resorting to not optimal tools on the terms of time & space complexity
    NOTE : in normal project i won't implement a queue by that concrete circular-dynamic .. i just apply it in the context of training

    '''
    def __init__(self):
        self._queue=[]       
        self._track_queue_indices=[]
        self._track_empty_indices=[]
        

    def enqueue(self,data):
        if not  type(data):
            raise TypeError("we couldnt insert None value ")
        if  not self._track_queue_indices or (type(data)==type(self._queue[self._track_queue_indices[0]])) :
            pass
        else:
            raise TypeError(f"type of the {data} as {type(data)} not equal the dominant type of the queue {type(self._queue[self._track_queue_indices[0]])}")
            

        if len(self._track_queue_indices)==len(self._queue):
            
               self._queue.append(data)
               self._track_queue_indices.append(len(self._queue)-1)
            
        else:
            
            new_index=self._track_empty_indices.pop(0)
            self._queue[new_index]=data
            self._track_queue_indices.append(new_index)

    def consistancy(self):
        return len(self._queue)==len(self._track_empty_indices)+len(self._track_queue_indices)
        
    def dequeue(self):
        if not  self._track_queue_indices:
            raise IndexError("no values in the queue to dequeue")
        the_index_of_value=self._track_queue_indices.pop(0)
        self._track_empty_indices.append(the_index_of_value)
        the_value=self._queue[the_index_of_value]
        self._queue[the_index_of_value]=None
        return the_value
    
    def __repr__(self):
        the_actual=[]

        for i in self._track_queue_indices:
            the_actual.append(self._queue[i])

        return f"{the_actual}"
    

    def __len__(self):
        return len(self._track_queue_indices)


    def __getitem__(self,index):

       if not isinstance(index,int):
           raise TypeError("the index should be intger")
       
       if not self._track_queue_indices:
           raise IndexError("index out of range")
       if not 0<=index<=len(self._track_queue_indices)-1:
           raise IndexError("the index out of range")
       return self._queue[self._track_queue_indices[index]]

    def clear(self):
        self._queue=[]
        
        
        self._track_queue_indices=[]
        self._track_empty_indices=[]

    def queue(self):
        '''
        return the ordered queue 
        '''
           
        the_actual=[]

        for i in self._track_queue_indices:
            the_actual.append(self._queue[i])

        return the_actual


    def __iter__(self):
        
        for i in self._track_queue_indices:
            yield self._queue[i]


    def merge_with_change(self,second):
        '''
        objectives :merging our main array_circular_dynamic size queue with the elements from another iterable object
        critical point: we have a constraint which rules our inseration as there is adominant data type(if it wasn't empty )
        and at the same time the iterable object which will be merged on our queue isn't condition to have only one type of all elment to accept 
        or refuse them from first time 
        here we have three options:
        -take it all or leave it all ....here we may need to apply the technique of roll-back
        -accept until have collide or contrary 
        -accept as possible as element consistant with the dominant data type .
         i choosed take it all or leave it all 
        '''

        if not isinstance(second,Iterable):
            raise TypeError(f"type of {second} should be type iterable")
        
        elif isinstance(second,dict):
             if self._track_queue_indices:
                 if type(self._queue[self._track_queue_indices[0]])!= tuple:
                     return self
             for i in second.items():
                 
                     self.enqueue(i)
                 
             return self

        elif isinstance(second,Iterable):
            
            if not self._track_queue_indices:
            
                for i in second:
                    try :
                        self.enqueue(i)                     
                    except:
                        self._queue=[]
                        self._track_empty_indices=[]
                        self._track_queue_indices=[]
                        return self 
                return self
                    
            no_inseration=0
            the_type=type(self._queue[self._track_queue_indices[0]])
            for i in second:
                
                if type(i)==the_type:
                    self.enqueue(i)
                    no_inseration+=1
                    

                else:
                    for _ in range(no_inseration):
                        ind=self._track_queue_indices.pop()
                        self._queue[ind]=None
                        self._track_empty_indices.append(ind)
                    return self
        return self
            


    def merge_without_change(self,second):
        '''
        objectives :merging acopy of our main array_circular_dynamic size queue with the elements from another iterable object
        critical point: we have a constraint which rules our inseration as there is adominant data type(if it wasn't empty )
        and at the same time the iterable object which will be merged on our queue isn't condition to have only one type of all elment to accept 
        or refuse them from first time 
        here we have three options:
        -take it all or leave it all ....here we may need to apply the technique of roll-back
        -accept until have collide or contrary 
        -accept as possible as element consistant with the dominant data type .
         i choosed take it all or leave it all 
        '''

        if not isinstance(second,Iterable):
            raise TypeError(f"type of {second} should be type iterable")
        
        elif isinstance(second,dict):
             the_copy=copy.deepcopy(self)
             if the_copy._track_queue_indices:
                 if type(the_copy._queue[the_copy._track_queue_indices[0]])!= tuple:
                     return the_copy
             for i in second.items():
                 
                     the_copy.enqueue(i)
                 
             return the_copy

        elif isinstance(second,Iterable):
            the_copy=copy.deepcopy(self)
            if not the_copy._track_queue_indices:
            
                for i in second:
                    try :
                        the_copy.enqueue(i)                     
                    except:
                        the_copy._queue=[]
                        the_copy._track_empty_indices=[]
                        the_copy._track_queue_indices=[]
                        return the_copy
                return the_copy
                    
            no_inseration=0
            the_type=type(the_copy._queue[the_copy._track_queue_indices[0]])
            for i in second:
                
                if type(i)==the_type:
                    the_copy.enqueue(i)
                    no_inseration+=1
                    

                else:
                    for _ in range(no_inseration):
                        ind=the_copy._track_queue_indices.pop()
                        the_copy._queue[ind]=None
                        the_copy._track_empty_indices.append(ind)
                    return the_copy
        return the_copy


    def traverse(self):


        if  not self._track_queue_indices:
            return None
        
        for i,k in enumerate(self._track_queue_indices):

            print(f"the element at index ({i}): {self._queue[self._track_queue_indices[k]]}")        

        

    def contains(self,element):
        '''
        objectives:checking the existance of an element on the queue or not 
        arguments:
          element:which we need to check it's existance
        output: true or false according to the existance

        '''

        if not self._track_queue_indices :
            return False
        
        if not (type(element)==type(self._queue[self._track_queue_indices[0]])):
            return False
        
        for i in self._track_queue_indices:
            if element==self._queue[i]:
                return True
            
        return False
    
   
    def size_actual_queue(self):
        '''
        objectives:return the total numbers in the queue
        '''

        return len(self._track_queue_indices)
            
    def is_empty(self):
        return True if not self._track_queue_indices else False

    def first(self):
        '''
        objectives:return the first element of the queue without removing it ; if it wasn't empty queue 
        '''
        if not self._track_queue_indices:
            raise IndexError("there is no element in the queue")
        
        return self._queue[self._track_queue_indices[0]]
    
    def last(self):
        '''
        objectives:return the last element of the queue without removing it ; if it wasn't empty queue 
        '''
        if not self._track_queue_indices:
            raise IndexError("there is no element in the queue")
        
        return self._queue[self._track_queue_indices[-1]]
    
    def copy (self):
        new_copy=copy.deepcopy(self)
        return new_copy
    
    def reverse_without_change(self):
        '''
        objective : reverse the queue 
        considerations:
          as the ordering of inserations and poping the elements of queue is something very concerete in queue
          context and applying the principle FIFO ,,then something such as reversing will violate that ...we will apply the reversing on a copy of the queue

        '''
        the_copy=copy.deepcopy(self)
        if not the_copy._track_queue_indices:
            return the_copy
        iterations=len(the_copy._track_queue_indices)//2
        left_side_indices=0
        right_side_indices=-1

        for _ in range(iterations):
            the_copy._track_queue_indices[left_side_indices],the_copy._track_queue_indices[right_side_indices]=the_copy._track_queue_indices[right_side_indices],the_copy._track_queue_indices[left_side_indices]
            left_side_indices+=1
            right_side_indices-=1

        return the_copy
    

    def order_without_change(self,the_type):
        '''
        objectives:ordering the queue either in ascending way (a) or in descending way (d)
        consideration:as the feature of FIFO is main constraint of the queue we can't violate ,,,we will apply this operation on a copy of the queue
        arguments:the_type which should either a:ascending or  d:descending
        output: an re-ordered copy of the queue
        '''

        if not self._track_queue_indices:
            the_copy=copy.deepcopy(self)

            return the_copy
        
        if the_type=="a":
           the_copy=copy.deepcopy(self)
           def helper(the_copy,first_index,last_index):
               def merge(the_copy,left_side,right_side):
                   first_left=left_side[0]
                   last_left=left_side[1]
                   first_right=right_side[0]
                   last_right=right_side[1]

                   for i in range(first_left,last_left+1):
                        if the_copy._queue[the_copy._track_queue_indices[i]]>the_copy._queue[the_copy._track_queue_indices[first_right]]:
                           the_copy._track_queue_indices[i],the_copy._track_queue_indices[first_right]=the_copy._track_queue_indices[first_right],the_copy._track_queue_indices[i]
                           
                           #shifting on the right side
                           start=first_right

                           while start<last_right:
                                if the_copy._queue[the_copy._track_queue_indices[start]]>the_copy._queue[the_copy._track_queue_indices[start+1]]:
                                    the_copy._track_queue_indices[start],the_copy._track_queue_indices[start+1]= the_copy._track_queue_indices[start+1],the_copy._track_queue_indices[start]
                                    start+=1

                                else:
                                    break

                   return [first_left,last_right]

               if first_index==last_index:
                  return [first_index,last_index]
               mid=(first_index+last_index)//2
               left_side=helper(the_copy,first_index,mid)
               right_side=helper(the_copy,mid+1,last_index)

               return merge(the_copy,left_side,right_side)
        
           helper(the_copy,0,len(the_copy._track_queue_indices)-1)
           return the_copy

        elif the_type=="d":
           the_copy=copy.deepcopy(self)
           def helper(the_copy,first_index,last_index):
               def merge(the_copy,left_side,right_side):
                   first_left=left_side[0]
                   last_left=left_side[1]
                   first_right=right_side[0]
                   last_right=right_side[1]

                   for i in range(first_left,last_left+1):
                        if the_copy._queue[the_copy._track_queue_indices[i]]<the_copy._queue[the_copy._track_queue_indices[first_right]]:
                           the_copy._track_queue_indices[i],the_copy._track_queue_indices[first_right]=the_copy._track_queue_indices[first_right],the_copy._track_queue_indices[i]
                           
                           #shifting on the right side
                           start=first_right

                           while start<last_right:
                                if the_copy._queue[the_copy._track_queue_indices[start]]<the_copy._queue[the_copy._track_queue_indices[start+1]]:
                                    the_copy._track_queue_indices[start],the_copy._track_queue_indices[start+1]= the_copy._track_queue_indices[start+1],the_copy._track_queue_indices[start]
                                    start+=1

                                else:
                                    break

                   return [first_left,last_right]

               if first_index==last_index:
                  return [first_index,last_index]
               mid=(first_index+last_index)//2
               left_side=helper(the_copy,first_index,mid)
               right_side=helper(the_copy,mid+1,last_index)

               return merge(the_copy,left_side,right_side)


        
           helper(the_copy,0,len(the_copy._track_queue_indices)-1)
           return the_copy

        else:
            raise ValueError(f"the type argument should be either (a) or (d) ...{the_type} isn't accepted")


    def min(self):
        if not self._track_queue_indices:
            raise ValueError("no elements on the queue to get the min ")
        minimum=self._queue[self._track_queue_indices[0]]
        for i in range(1,len(self._track_queue_indices)):
            if self._queue[self._track_queue_indices[i]]<minimum:
                minimum=self._queue[self._track_queue_indices[i]]

        return minimum

    
    def max(self):
        if not self._track_queue_indices:
            raise ValueError("no elements on the queue to get the min ")
        maximum=self._queue[self._track_queue_indices[0]]
        for i in range(1,len(self._track_queue_indices)):
            if self._queue[self._track_queue_indices[i]]>maximum:
                maximum=self._queue[self._track_queue_indices[i]]

        return maximum


    def access_without_delete(self,index):
        '''
        objectives:getting the value at specific index 
        argument:index within the range of the queue indices 
        '''
        if not (type(index)==int) :
            raise TypeError(f"the index should be intger")
        
        if not self._track_queue_indices:
            raise IndexError("the queue already is empty... nothing to access")
        if not 0<=index<=len(self._track_queue_indices)-1:
            raise IndexError(f"the index ({index}) should be in the range of 0 to {len(self._track_queue_indices)-1}")
        
        return self._queue[self._track_queue_indices[index]]

    def change_element(self,index,value):
        '''
        objective:change the value of an element at specific index without change the order of the inserartion
        arguments:
          index:intger in the range of the indices 
          value: the new value with type is consistant with the dominant type in the queue 
          return :return None 
        '''

        if not (type(index)==int) :
            raise TypeError(f"the index should be intger")
        
        if not self._track_queue_indices:
            raise IndexError("the queue already is empty... nothing to access")
        if not 0<=index<=len(self._track_queue_indices)-1:
            raise IndexError(f"the index ({index}) should be in the range of 0 to {len(self._track_queue_indices)-1}")
        if not (type(value)==type(self._queue[self._track_queue_indices[0]])):
            raise TypeError(f"the new value type  should be as adominant type which {type(self._queue[self._track_queue_indices[0]])} while it's {type(value)} ")

        self._queue[self._track_queue_indices[index]]=value


    def __setitem__(self,index,value):
        self._queue[self._track_queue_indices[index]]=value

    def __eq__(self,second):
        '''
        here as we define the equivilance between two objects the main one is our array circular_dynamic queue ...we will go beyond the direct 
        meaning of the equivlance as the two interfaces&pointers refer to the same object on the memory to the space of equivlance in the value
        and also won't make it restricted with only object of the same data type but with any iterable object
        note :if the both iterables are the same on the values but not in the order the method will return false
        '''

        if not isinstance(second,Iterable):
            raise TypeError("the second sobject should be iterable")
        
        if len(second)!=len(self):
            return False
        
        for i in range(len(self)):
            if type(self[i])!=type(second[i]):
                return False
            elif self[i]!=second[i]:
                return False
            
        return True
    

    def __lt__(self,second):
        '''
        objectives: comparing two objects of the same data type 
        as the comparing of two oop object is something very complex and it gets much harder in cases of lt,le,gt,ge 
        we will limit the comparing of them to the same objects not a wide to compare with any iterable
        '''
        if not isinstance(second,arrary_circular_dynamic_queue):
            raise TypeError(f"the operators <,<=,>,>= need both operands to be the same array_circular_dynamic_queue")

        if (not self._track_queue_indices) and second._track_queue_indices:
            return True #here it's true as the first one is empty 

        if self._track_queue_indices and (not second._track_queue_indices):
             return False

        if type(self._queue[self._track_queue_indices[0]])!=type(second._queue[second._track_queue_indices[0]]):
            raise TypeError("the objects aren't comparable")


        if len(self)<len(second):
            return True
        elif len(second)>len(self):
            return False
        else:
            for i in range(len(self)-1):
                if self[i]>=second[i]:
                    return False
            return True