def classify_age(age):
       if age < 0:
       	print("Invalid age entered. Please try again. ")
       elif age <= 12:
        	print("You are a Child. ")
       elif age <= 19:
       	 print("You are a Teen. ")
       elif age <= 64:
       	 print("You are an Adult. ")
       else:
       	 print("You are a Senior. ")
       	 
classify_age(16)
