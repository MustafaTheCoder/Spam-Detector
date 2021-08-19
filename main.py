text = input("Text: ")
spam = False

if("make money fast"):
    spam = True
    print("Spam Detected!") 
elif("subscribe this"):
    spam = True
    print("Spam Detected!")
elif("buy now"):
    spam = True
    print("Spam Detected!")
elif("purchase now"):
    spam = True
    print("Spam Detected!")
elif("for free"):
    spam = True
    print("Spam Detected!")
elif("click this"):
    spam = True
    print("Spam Detected!")
else:
    spam = False
    print("Spam Not Found!")    
