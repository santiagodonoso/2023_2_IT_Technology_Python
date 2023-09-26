try:
  raise Exception("ups")
  print("x")
except Exception as e:
  print(e)
finally:
  print("done")


  