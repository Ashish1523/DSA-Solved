class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.maxHeap=[]
        self.taskPriorityMap={}
        self.taskOwnerMap={}

        for task in tasks:
            self.add(task[0],task[1],task[2])

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.maxHeap,(-priority,-taskId))
        self.taskPriorityMap[taskId]=priority
        self.taskOwnerMap[taskId]=userId


    def edit(self, taskId: int, newPriority: int) -> None:
        heapq.heappush(self.maxHeap,(-newPriority,-taskId))
        self.taskPriorityMap[taskId]=newPriority

    def rmv(self, taskId: int) -> None:
        self.taskPriorityMap[taskId]=-1

    def execTop(self) -> int:
        while self.maxHeap:
            negPriority,negtaskId=heapq.heappop(self.maxHeap)
            priority=-negPriority
            taskId=-negtaskId

            if self.taskPriorityMap.get(taskId,-1)==priority:
                self.taskPriorityMap[taskId]=-1
                return self.taskOwnerMap[taskId]
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()