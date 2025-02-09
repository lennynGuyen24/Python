choice=input("Pick your type of pine tree(supertree / tree): ")
if choice=="supertree":
    super_tree_size=int(input("How many trees would you like your supertree to have?: "))
    tree_size=int(input("How many rows would you like the tree to have?:  "))
    if 5<=tree_size<=20:
      tree_name = input("Type a name for your pine tree: ")
      print(f"Here's {tree_name}, your super pine tree: ")
      smaller_tree=1
      while smaller_tree<super_tree_size+1:
       index=0
       for index in range(tree_size):
        print(f"{' '*(tree_size-index+20)}{'*'*(2*index+1)}")
       smaller_tree+=1
      for index in range(tree_size-3):
        if 5<=tree_size<10:
          print(f"{' '*(tree_size-1+20)}{'*'*3}")
        elif 10<=tree_size<15:
          print(f"{' '*(tree_size-2+20)}{'*'*5}")
        else:
            print(f"{' ' * (tree_size - 4 + 20)}{'*' * 9}")
    else:
      print(f"Tree size must be between 5 and 20 rows!")
else:
    tree_size = int(input("How many rows would you like the tree to have?:  "))
    if 5 <= tree_size <= 20:
        tree_name = input("Type a name for your pine tree: ")
        print(f"Here's {tree_name}, your pine tree: ")
        for index in range(tree_size):
          print(f"{' ' * (tree_size - index + 20)}{'*' * (2 * index + 1)}")
        for index in range(tree_size-3):
          if 5<=tree_size<10:
            print(f"{' '*(tree_size-1+20)}{'*'*3}")
          elif 10<=tree_size<15:
            print(f"{' '*(tree_size-2+20)}{'*'*5}")
          else:
            print(f"{' '*(tree_size-4+20)}{'*'*9}")
    else:
      print(f"Tree size must be between 5 and 20 rows!")


