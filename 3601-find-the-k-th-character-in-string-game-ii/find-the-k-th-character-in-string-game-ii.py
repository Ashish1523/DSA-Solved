class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # word="a"
        # w=k
        # i=0
        # while len(word)<k:
        #     ans=""
        #     if operations[i]==1:
        #         for j in range(len(word)):
        #             if word[j]=='z':
        #                 ans+='a'
        #             else:
        #                 ans+=chr(ord(word[j])+1)
        #     else:
        #         ans=word
        #     word+=ans
        #     i+=1
        # return word[k-1]

        lengths = [1]  # Initial length of "a"
        for op in operations:
            prev = lengths[-1]
            if op == 1 or op == 0:
                new_length = prev * 2
            lengths.append(new_length)
            if new_length >= k:
                break  # No need to go further if we already reach k

        # Step 2: Backtrack to find the origin of the k-th character
        idx = len(lengths) - 1
        char = 'a'  # The initial string
        while idx > 0:
            prev_len = lengths[idx - 1]
            if k > prev_len:
                k -= prev_len  # It came from the second half

                if operations[idx - 1] == 0:
                    # Copy, so the character is same as earlier
                    pass
                else:
                    # Shifted version, so shift the k-th char of previous
                    orig_char = char
                    if orig_char == 'z':
                        char = 'a'
                    else:
                        char = chr(ord(orig_char) + 1)
            else:
                # It came from the first half, go one level up
                pass  # char stays the same
            idx -= 1

        return char