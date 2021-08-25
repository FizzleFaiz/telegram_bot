import random

def random_image(): 
  i = random.randint(0,999)
  image = f"https://picsum.photos/200/300?random={i}"
  return image