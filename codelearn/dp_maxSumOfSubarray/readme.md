Ta định nghĩa một dãy là đẹp khi dãy đó có tổng chia hết cho 9. Cho một mảng arr gồm các số nguyên được xếp thành một vòng tròn. Hãy tìm dãy con liên tiếp và đẹp có tổng lớn nhất. Trả về tổng của dãy đó, nếu không tồn tại dãy nào như vậy trả về -1.

Ví dụ:

Với arr = [-3,5,-4,7] thì maxSumOfBeautifulSubarray(arr) = 9 .

Như vậy dãy cần tìm là [7,-3,5] và có tổng là 9.
Đầu vào/Đầu ra:

[Thời gian chạy] 0.5s với C++, 3s với Java và C#, 4s với Python, Go và JavaScript.

[Đầu vào] array of integer
0<=arr.length<=10^5 
|arr[i]|<=10^9
[Đầu ra]long
