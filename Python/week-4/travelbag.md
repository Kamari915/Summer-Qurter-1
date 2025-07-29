1. One difference between a list and a tuple:
   A list is mutable (you can change, add, or remove items), while a tuple is immutable (once created, it cannot be changed).

2. When is it better to use a list over a tuple
   When you need to modify the data—such as adding, removing, or updating elements—it's better to use a list

3. How do you remove an item from a list
   You can use the .remove() method or the delkeyword.
   Example:
python
   my_list = [1, 2, 3]
   my_list.remove(2)  
   # or
   del my_list[0]    
  

4. Two mutation functions you can use on lists

  .append() – Adds an item to the end of the list.
     Example: my_list.append(4)
   .pop() – Removes and returns the last item (or a specific index).
     Example:my_list.pop() ormy_list.pop(1)

Let me know if you want more examples!
