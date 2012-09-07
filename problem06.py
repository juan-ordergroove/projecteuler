sum_of_sqs = 0
for i in range(1,101):
    sum_of_sqs += i**2
sq_of_sum = 0
for i in range(1,101):
    sq_of_sum += i
sq_of_sum = sq_of_sum**2
print sq_of_sum - sum_of_sqs