import os
import pickle
def reverse_fun():
      with open("users.json","rb") as f:
          data = f.read()
      if("bin" or "sys" or "system" or "os" or "request" or "process" or "__reduce__" in data):
	return false
      else:
      	d = pickle.loads(data)
      	return d

if __name__ == '__main__':
      print(reverse_fun())