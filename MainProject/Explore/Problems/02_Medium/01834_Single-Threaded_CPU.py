"""
You are given n tasks labeled from 0 to n - 1 represented by a 2D integer array tasks,
where tasks[i] = [enqueueTime_i, processingTime_i] means that the i-th task will be available to process at enqueueTime_i and will take processingTime_i to finish processing.
You have a single-threaded CPU that can process at most one task at a time and will act in the following way:
  If the CPU is idle and there are no available tasks to process, the CPU remains idle.
  If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
  Once a task is started, the CPU will process the entire task without stopping.
  The CPU can finish a task then start a new one instantly.
Return the order in which the CPU will process the tasks.
Constraints:
  tasks.length == n
  1 <= n <= 10^5
  1 <= enqueueTime_i, processingTime_i <= 10^9
"""

import heapq

class Solution:
    def getOrder(self, tasks):
        for i, task in enumerate(tasks): task.append(i)  # task[2] = index in tasks
        tasks.sort()
        heap, self.res, self.run_task, self.end_tm = [], [], None, None
        self.set_run_task(task=tasks[0])
        i = 1
        while i < len(tasks):
            task = tasks[i]
            if task[0] <= self.end_tm:
                heapq.heappush(heap, ((task[1], task[2]), task))
                # heapq.heappush(heap, (1e6*task[1]+task[2], task))
                i += 1
            else:
                if heap:
                    self.set_run_task(task=heapq.heappop(heap)[1])
                else:
                    self.set_run_task(task)
                    i += 1

        while heap:
            self.set_run_task(task=heapq.heappop(heap)[1])
        return self.res

    def set_run_task(self, task):
        self.res.append(task[2])  # index
        self.run_task = task
        beg_tm = task[0] if self.end_tm is None or self.end_tm <= task[0] else self.end_tm
        self.end_tm = beg_tm + task[1]

sln = Solution()  # Example 1
tasks = [[1,2],[2,4],[3,2],[4,1]]
print(sln.getOrder(tasks))

sln = Solution()  # Example 2
tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
print(sln.getOrder(tasks))

# sln = Solution()
# tasks = [[5,2],[7,2],[9,4],[6,3],[5,10],[1,1]]
# print(sln.getOrder(tasks))
#
# sln = Solution()
# tasks = [[35,36],[11,7],[15,47],[34,2],[47,19],[16,14],[19,8],[7,34],[38,15],[16,18],[27,22],[7,15],[43,2],[10,5],[5,4],[3,11]]
# print(sln.getOrder(tasks))
#
# sln = Solution()
# tasks = [[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]
# print(sln.getOrder(tasks))