from datetime import datetime



assets = []
values = []
user_input = ""
sent= True

while (sent):
  user_input = input("Enter assets you hold, it can be anything with monetary value you want to include. Examples: VTSAX, Bonds, TIPS, SPY, Cash, Gold. If you entered all your assets, type 'n' to move along: ")
  
  if user_input.lower() == "n":
    sent = False
    
  else:
    assets.append(user_input)
    print("Current list:", assets)


print("Current list:", assets)
gross = []
for asset in assets:
  


  user_input = float(input("Enter the value of your {} ".format(asset)))
  gross.append(user_input)


total = sum(gross)
print(total)

print("Your total portfolio value is:", total)

asset_values = []


for value in gross:
  asset_values.append((float(value) / float(total))*100)

print(assets, "\n", asset_values)



export = input("Do you want to save your data to a file? 'Y' is yes, any other value for no ")

# add file saving of data with date
date = datetime.today().strftime('%Y-%m-%d')


asset_values_str = [str(value) for value in asset_values]
gross_str = [str(value) for value in gross]

assets_str = [str(value) for value in assets]

assets_values_final = ' '.join(asset_values_str)
gross_final = ' '.join(gross_str)
assets_final = ' '.join(assets_str)



if export.lower() == 'y':
  print("x")
  with open("Data {} allocation.txt".format(date), "a") as file:
    file.write(date)
    file.write("\n")
    file.write("Assets: ")
    file.write("\n")
    file.write(assets_final)
    file.write("\n")
    file.write("Percentage values of assets: ")
    file.write("\n")
    file.write(assets_values_final)
    file.write("\n")
    file.write("Gross values of assets: ")
    file.write("\n")
    file.write(gross_final)
    file.write("\n")
    file.write("total value of portfolio: {}".format(total) + "\n")
    
    # close the file
    file.close()