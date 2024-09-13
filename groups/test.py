# Python3 implementation to count the
# number of ways to divide N in
# groups such that each group
# has K number of elements

# Function to count the number
# of ways to divide the number N
# in groups such that each group
# has K number of elements
def calculate(pos, prev, left, k):
    # Base Case
    if (pos == k):
        if (left == 0):
            return 1;
        else:
            return 0;

    # If N is divides completely
    # into less than k groups
    if (left == 0):
        return 0;

    answer = 0;

    # Put all possible values
    # greater equal to prev
    for i in range(prev, left + 1):
        answer += calculate(pos + 1, i,
                            left - i, k);

    return answer;


# Function to count the number of
# ways to divide the number N
def countWaystoDivide(n, k):
    return calculate(0, 1, n, k);


# Driver Code
if __name__ == '__main__':
    N = 15;
    K = 6;

    print(countWaystoDivide(N, K));

# This code is contributed by 29AjayKumar