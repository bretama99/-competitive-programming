# arr = [6]
# arr1 = []
# sum1 =0
# for i in range(len(arr)):
#     sum1 = sum(arr[:i+1])
#     arr1.append(max(sum1,sum(arr[i:])))
# print(max(arr1))
def max_aggrigate_temperature_change(n,temp_change):
    if n==1:
        return (temp_change[0])
    left = temp_change[0]
    right = sum(temp_change)
    temp_right_now = max(left,right)
    max_temp_change = temp_right_now
    for i in range(1,n):
        left = left + temp_change[i]
        right = right-temp_change[i-1]
        temp_right_now = max(right,left)
        if temp_right_now>max_temp_change:
            max_temp_change = temp_right_now
    return (max_temp_change)
























