class Spreadsheet:

    def __init__(self, rows: int):
        self.mapy=defaultdict(int)


    def setCell(self, cell: str, value: int) -> None:
        self.mapy[cell]=value

    def resetCell(self, cell: str) -> None:
        self.mapy[cell]=0

    def getValue(self, formula: str) -> int:
        arr=formula[1:].split("+")
        ans=0
        for val in arr:
            if val.isnumeric():
                ans+=int(val)
            else:
                ans+=self.mapy[val]
        return ans


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)