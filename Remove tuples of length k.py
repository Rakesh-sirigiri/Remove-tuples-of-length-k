test_list = [(4,5), (4,2), (3,4,7), (2,9), (2,3,5,6)]
print("The original list : " + str(test_list))
K = 1
res = [ele for ele in test_list if len(ele) != K]
print("Filtered list : " + str(res))
