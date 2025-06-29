# 1257 (Medium) Smallest Common Region
"""
You are given some lists of regions where the first region of each list directly contains all other regions in that list.
If a region x contains a region y directly, and region y contains region z directly, then region x is said to contain region z indirectly.
Note that region x also indirectly contains all regions indirectly containd in y.
Naturally, if a region x contains (either directly or indirectly) another region y, then x is bigger than or equal to y in size. Also, by definition, a region x contains itself.
Given two regions: region1 and region2, return the smallest region that contains both of them.
It is guaranteed the smallest region exists.

Constraints:
  2 <= regions.length <= 10^4
  2 <= regions[i].length <= 20
  1 <= regions[i][j].length, region1.length, region2.length <= 20
  region1 != region2
  regions[i][j], region1, and region2 consist of English letters.
  The input is generated such that there exists a region which contains all the other regions, either directly or indirectly.
  A region cannot be directly contained in more than one region.
"""

from typing import List

# Runtime = 217 ms  Beats 67.40%  ;  Memory = 22.48 MB  Beats 52.60%
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        self.create_region_map(regions)
        region1_path = self.create_region_path(region1)
        smallest_region = region2
        while smallest_region not in region1_path:
            smallest_region = self.region_map.get(smallest_region)
        return smallest_region  # smallest_region in region1_path

    def create_region_map(self, regions: List[List[str]]):
        self.region_map = {}  # str child: str parent
        for arr in regions:
            for i in range(1, len(arr)): self.region_map[arr[i]] = arr[0]

    def create_region_path(self, region):
        region_path = set()  # Earth -> ... -> region
        curr_region = region
        while curr_region:
            region_path.add(curr_region)
            curr_region = self.region_map.get(curr_region)
        return region_path


sln = Solution()
regions = [
    ["Earth","North America","South America"],
    ["North America","United States","Canada"],
    ["United States","New York","Boston"],
    ["Canada","Ontario","Quebec"],
    ["South America","Brazil"]
]
print(sln.findSmallestRegion(regions, region1="Quebec", region2="New York"))  # Output: "North America"

sln = Solution()
regions = [
    ["Earth", "North America", "South America"],
    ["North America", "United States", "Canada"],
    ["United States", "New York", "Boston"],
    ["Canada", "Ontario", "Quebec"],
    ["South America", "Brazil"]
]
print(sln.findSmallestRegion(regions, region1="Canada", region2="South America"))  # Output: "Earth"