print('=============================================== ToDoList ===============================================')

words = input('Enter your word to make a list : ').title()

list = words.split()

#for adding in list
def function(words):
  for words in list:
    index = 0
    index +=1
function(words)

while True:
  print('Please select below options')
  print('if you want to add more, Please write : Add ')
  print('if you want delete by Indexing Number, Please write : del by Indexing Number ')
  print('if you want delete by name, Please write : del by name ')
  print('if you want to get list, Please write : Get List ')
  print('if you want to exit from the Program, Please write : Exit ')
  
  user_input = input('Please write here ....')

  if user_input == 'Add':
  #Adding more on list
    add_more = input('Enter your Word to add more on the list : ').title()
    print(f'You have added word {add_more} into your list')
    list.append(add_more)
    user_input = input('Please write here if you want to do samething OR someother thing.... in Yes Or NO : ')
    if user_input == 'Yes':
       continue
    else:
      print('please write properly...')
      continue
    
  elif user_input == 'del by Indexing Number':
  #Deleting By Index Number
    By_Index_number = int(input('Enter your Word to delete from the list : '))
    del list[By_Index_number]
    print(f'You have removed word {By_Index_number} into your list')
    user_input = input('Please write here if you want to do samething OR someother thing.... in Yes Or NO : ').title()
    if user_input == 'Yes' or 'yes':
       continue
    else:
      print('please write properly...')
      continue
    
  elif user_input == 'Get List' or 'list':
  #Deleting By Index Number
    print(list)
    user_input = input('Please write here if you want to do samething OR someother thing.... in Yes Or NO : ').title()
    if user_input == 'Yes':
       continue
    else:
      break
      print('Thank you for using')
  
  elif user_input == 'del by name':
  #Deleting By String
    By_string = input('Enter your Word to delete by string Method : ')
    str(list.remove(By_string))
    print(f'You have removed word {By_string} into your list')
    print(list)
    user_input = input('Please write here if you want to do samething OR someother thing.... in Yes Or NO : ').title()
    if user_input == 'Yes':
       continue
    else:
      break
      print('Thank you for using')
  
  elif user_input == 'Exit' or 'exit' or 'No' or 'no':
    print('Thank you for using')
    break
  
  else:
    print('Please write properly')



print("Name : 'Daniyal Alam'")
print("Roll Number : 'AIC009423' ")
print("Institue Name : 'Saylani Welfare' ")
print("Email : 'scdaniyalalam@outlook.com' ")
      