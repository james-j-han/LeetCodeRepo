class Solution(object):
    def heightChecker(self, heights):
          """
          :type heights: List[int]
          :rtype: int
          """
    
          # Q1: is len of heights and expected always equal?
    
          # MATCH: dictionary, two-pointer
    
          # return type: int
    
          # use two pointers to loop through heights array and expected array at the same time
          # expected is the sorted heights array
          # if the element at index does not match, add 1 to total
    
          total = 0
          expected = sorted(heights)
    
          for i, n in enumerate(heights):
              if n != expected[i]:
                  total += 1
    
          return total