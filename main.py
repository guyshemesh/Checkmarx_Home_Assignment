import numpy as np

def numpy_hello_world():
    arr = np.array([1, 2, 3, 4, 5])
    if arr[0]==1:
      return "Hello World!"
    return "mistake"

if __name__ == "__main__":
    print(numpy_hello_world())
