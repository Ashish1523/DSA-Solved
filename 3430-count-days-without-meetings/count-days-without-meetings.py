class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        rem = 0
        n_end = 0
        meetings.sort()

        for start, end in meetings:
            if start > n_end + 1:
                rem += start - n_end - 1

            n_end = max(n_end, end)

        rem += days - n_end

        return rem