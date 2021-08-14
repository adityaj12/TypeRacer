import time
import random

print("Welcome to Type Racer. Press x to play. ")
sentences = ["Peter Piper picked a peck of pickled peppers", "She sells seashells by the sea shore", "How much wood could a woodchuck chuck if a woodchuck could chuck wood?", "If a dog chews shoes, whose shoes does he choose?", "If you notice this notice, you will notice that this notice is not worth noticing", "I saw Susie sitting in a shoe shine shop"]

points = 0
num = 0
num2 = 0

if input("") == 'x':
  print('Ready...')
  time.sleep(1.5)
  print("Set...")
  time.sleep(1.5)
  print("Go!")
  
  begin_time = time.time()
  sent = sentences[random.randint(0,5)]
  print(sent)
  correct = sent.split()
  
  answer = input("Type: ")
  incorrect = answer.split()
  end_time = time.time()

print('Elapsed Time: %1.2f' % (end_time - begin_time) + " seconds")
for i in range(len(incorrect)):
  if correct[i] == incorrect[i]:
    points += 1
score = (points / len(correct))

print("You got a score of %1.2f" % (score * 100))