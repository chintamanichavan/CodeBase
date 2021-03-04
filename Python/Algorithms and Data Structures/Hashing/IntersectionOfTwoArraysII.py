# Python3


def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """

    # approach: sort two lists and use two pointers to compare

    nums1.sort()
    nums2.sort()
    
    p1 = p2 = 0
    result = []

    while p1 < len(nums1) and p2 < len(nums2):
        num1 = nums1[p1]
        num2 = nums2[p2]

        if num1 < num2:
            p1 += 1
        elif num1 > num2:
            p2 += 1
        else:
            result.append(num1)
            p1 += 1
            p2 += 1
    print(result)
    return result

nums1 = [1,2,3,4,5,6]
nums2 = [3,4,7,5,1,9,8]
intersect(nums1,nums2)
