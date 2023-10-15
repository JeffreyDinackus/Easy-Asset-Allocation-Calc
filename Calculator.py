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



export = input("Do you want to save your data to a file? 'Y' is yes, any other value for no")

# add file saving of data with date
date = datetime.today().strftime('%Y-%m-%d')


if export.lower() == 'y':
  print("x")
  with open("Data {} allocation.txt".format(date), "a") as file:
    file.write(date)
    file.write("Assets: ")

    file.write('\n'.join(str(i) for i in assets))
    file.write("Percentage values of assets: ")

    file.write('\n'.join(str(i) for i in asset_values))
    file.write("Gross values of assets: ")
    file.write('\n'.join(str(i) for i in gross))
    file.write("total value of portfolio: {}".format(total))
    
    # close the file
    file.close()