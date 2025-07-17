class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def bfs(image,r,c):
            orig=image[r][c]
            image[r][c]=color
            q=deque()
            q.append([r,c])
            coord=[[-1,0],[1,0],[0,-1],[0,1]]
            while q:
                row,col=q.popleft()
                for r,c in coord:
                    nrow=row+r
                    ncol=col+c
                    if (0<=nrow<len(image)) and (0<=ncol<len(image[0])) and image[nrow][ncol]==orig:
                        image[nrow][ncol]=color
                        q.append([nrow,ncol])


        if image[sr][sc]==color:
            return image
        else:
            bfs(image,sr,sc)
            return image
            