def sets():
  set1 = set([10, 20, 18, 4])
  set1.add(7)
  set1[0] = 22
  set1.remove(18)
  print(sorted(set1))
  return


def loop():
  for x in [10, 20, 30, 40, 50]:
    print(x * 2, end=' ')
  return


def list():
  list1 = [1, 9, 3, 6]
  x = int(input('Enter a number: '))
  if x in list1:
    print('In', end=' ')
  if x is list1[0]:
    print('Is')
  return


def listAcc():
  nums = [5, 4, 8, 3, 1, 9]
  for i in range(5, -1, -3):
    print(nums[i], end=' ')
  return


def listLoop():
  nums = [5, 4, 8]
  nums2 = [1, 3]
  for i in range(len(nums)):
    for j in range(len(nums2)):
      print(nums[i] * nums2[j], end=' ')
    print()
  return


def enumeration():
  numbers = [-3, 6, 0, -5, 11, 9]
  this_one = numbers[0]
  this_index = 0
  for (pos, num) in enumerate(numbers):
    if pos > this_index:
      this_one = num
      this_index = pos
  print(this_index, this_one)
  return


def enumer2():
  nums = [2, 9, 4, 1]
  for pos, val in enumerate(nums):
    print(pos * val, end=' ')
  return


def newPassword():
  password = input("New Password: ")
  password2 = input("Confirm New Password: ")
  while password != password2:
    password = input("New Password: ")
    password2 = input("Confirm New Password: ")
  print("You have successfully changed your password.")
  return


def nameAndGrade():
  Grades = {"Julie": 90, "Laura": 95, "Stan": 88}
  for name in Grades:
    print(f'Name: {name}')
    print(f'Grade: {Grades[name]}\n')
  return


def hiddenQuote():
  hidden_quote = [
      'Let', 'apple', 'your', 'elephant', 'soul', 'chair', 'stand', 'umbrella',
      'cool', 'rocket', 'and', 'spoon', 'composed', 'banana', 'before',
      'telescope', 'a', 'tree', 'million', 'giraffe', 'universes.',
      'simultaneously.'
  ]
  for index in range(0, len(hidden_quote) - 1, 2):
    print(hidden_quote[index], end=' ')
  return


def randomProb():
  stuff = (61, "dog", 21.12, "42", 42)
  if stuff[4] == 42:
    stuff[1] = "cat"
  elif stuff[2] < 25.52:
    print(stuff.count(42))
  return


def intersection():
  set1 = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
  set2 = set([0, 2, 4, 6, 8])
  set3 = set([0, 3, 6, 9])

  only_set1 = set1.difference(set2, set3)

  print(only_set1)
  return


def subscriptions():
  monthly_subs = {
      "Netflix": 9.99,
      "Spotify": 9.99,
      "Hulu": 5.99,
      "HBO Max": 14.99
  }

  price = float(input("How much can you spend? "))

  if price in monthly_subs:
    print(f"You should try {monthly_subs[price]}!")
  else:
    print("Couldn't find something for you.")
  return


def whileOverFor():
  numberList = [2.25, 1.75, 5.5, 3.33, 9.9, 4.67, 8.125, 7.4, 6.87]
  while numberList:
    print(f'{numberList.pop(0)**2:.2f}')
  return


def outputObs():
  sentence = ["I", "Love", "Apples", "over", "Oranges"]
  for x in enumerate(sentence):
    print(x)

  pairs = {1: "I", 2: "Love", 3: "Apples", 4: "over", 5: "Oranges"}
  for x in enumerate(pairs):
    print(x)
  return