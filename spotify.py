# Chill Artist and their respective Artist ID
chill_dict = {
  "keshi":"spotify:artist:3pc0bOVB5whxmD50W79wwO",
  "Sasha Sloan":"spotify:artist:4xnihxcoXWK3UqryOSnbw5",
  "Khalid": "spotify:artist:6LuN9FCkKOj5PcnpouEgny",
  "Gentle Bones": "spotify:artist:4jGPdu95icCKVF31CcFKbS",
  "blackbear": "spotify:artist:2cFrymmkijnjDg9SS92EPM",
  "Childish Gambino": "spotify:artist:73sIBHcqh3Z3NyqHKZ7FOL",
  "The Weeknd": "spotify:artist:1Xyo4u8uXC1ZmMpatF05PJ"
}

# 80s Artist and their respective Artist ID
eight_dict = {
  "Queen":"spotify:artist:1dfeR4HaWDbWqFHLkxsg1d",
  "Bon Jovi":"spotify:artist:58lV9VcRSjABbAbfWS6skp",
  "Journey":"spotify:artist:0rvjqX7ttXeg3mTy8Xscbt",
  "LeAnn Rimes": "spotify:artist:2d3VHzlOEwXvmBdS4pzOPL",
  "Foreigner": "spotify:artist:6IRouO5mvvfcyxtPDKMYFN"
}

# Childhood and their respective Artist ID
child_dict = {
  "Linkin Park":"spotify:artist:6XyY86QOPPrYVGvF9ch6wz",
  "Rihanna":"spotify:artist:5pKCCKE2ajJHZ9KAiaK11H",
  "Paramore":"spotify:artist:74XFHRwlV6OrjEM0A2NCMF",
  "Coldplay": "spotify:artist:4gzpq5DPGxSnKTe4SA8HAU",
  "Maroon 5": "spotify:artist:04gDigrS5kc9YWfZHwBETP",
  "Jonas Brothers":"spotify:artist:7gOdHgIoIKoe4i9Tta6qdD",
  "Taylor Swift": "spotify:artist:06HL4z0CvFAxyc27GXpf02",
  "Avril Lavigne": "spotify:artist:0p4nmQO2msCgU4IF37Wi3j"
}

# Mando Pop Artist and their respective Artist ID
mando_dict = {
  "Jay Chou":"spotify:artist:2elBjNSdBE2Y3f0j1mjrql",
  "Eric Chou":"spotify:artist:5fEQLwq1BWWQNR8GzhOIvi",
  "JJ Lin":"spotify:artist:7Dx7RhX0mFuXhCOUgB01uM",
  "Ren Ran":"spotify:artist:6f4srX54JFrLNK4aTJe2Sc",
  "高爾宣OSN":"spotify:artist:4TcOznbEZBqev21LzAH4KE",
  "G.E.M": "spotify:artist:7aRC4L63dBn3CiLDuWaLSI",
  "A-Mei Chang": "spotify:artist:6noxsCszBEEK04kCehugOp"
}

country_code ={
  "Singapore" :"SG",
  "United States": "US"
}

user = '21fvcbefalygwzh3n6df5ykxa'

# Class for Spotify Search func
class sp_s:
  def __init__(self,s_type):
    self.s_type = s_type