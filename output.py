from string import ascii_lowercase


def outdat(sheet, data):
  rdata = []

  for row in data:
    rdata.append([row["EMAIL"], str(row["NAME"][0]) + " " + str(row["NAME"][1]), row["ID"], row["AVERAGE"], row["TIMES"][0], row["TIMES"][1], row["TIMES"][2], row["TIMES"][3], row["TIMES"][4]])

  sheet.update("A1:I" + str(len(data)), rdata)


def practiceout(sheet):
  fakedata = [
    ["ID", "Email", "First", "Last", "1", "2", "3", "4", "5"],
    ["ID", "Email", "First", "Last", "1", "2", "3", "4", "5"],
  ]

  nums = [0]


 # for i in range(99):
    #print(getlet(nums))
    #updatenums(nums)

  #print(getlet(nums))

  row = 1
  for data in fakedata:
    sheet.update("A" + str(row) + ":I" + str(row), [data])
    row += 1

  #nums = [26, 26, 23, 1]
  #nums = updatenums(nums, 0)
  #print(nums)

#def updatenums(nums, i=0):
#  nums[i] += 1
#  if nums[i] > 25:
#    nums[i] = 0
#    if len(nums) <= i + 1:
#      nums.append(0)
#    updatenums(nums, i + 1)
#    return nums

#def getlet(nums):
#  out = ""
#  for num in nums:
#    out += ascii_lowercase[num]
#  return out[::-1]
    
    




