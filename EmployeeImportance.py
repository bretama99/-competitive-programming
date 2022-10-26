"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        impEmployee = {}
        subEmployee = {}
        
        for employee in employees:
            impEmployee[employee.id] = employee.importance
            subEmployee[employee.id] = employee.subordinates
        def dfs(id):
            result = impEmployee[id]
            for ordinate in subEmployee[id]:
                result += dfs(ordinate)
            return result
        return dfs(id)
