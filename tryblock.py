'''tryblock'''
try:
    a=[1,2,3]
    print(int(a))
    print(b)
except NameError:
  print("name error")
except ValueError:
  print("value error")
except TypeError:
  print("type error")
else:
  print("Nothing went wrong")
finally:
    print("thank you")
