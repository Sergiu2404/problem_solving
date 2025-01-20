from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    dictionary = {}

    for elem in nums:
        dictionary[elem] = dictionary.get(elem, 0) + 1

    sorted_dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    result = []
    for tuple in sorted_dictionary:
        if(k == 0):
            break
        k-=1
        result.append(tuple[0])

    return result

if __name__ == '__main__':
    print(topKFrequent([1,2,2,3,3,3], 2))