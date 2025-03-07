class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def simple_sieve(limit):
            primes = []
            is_prime = [True] * (limit + 1)
            is_prime[0] = is_prime[1] = False

            for i in range(2, limit + 1):
                if is_prime[i]:
                    primes.append(i)
                    for j in range(i * i, limit + 1, i):
                        is_prime[j] = False
                        
            return primes

        def segmented_sieve(L, R):
            if L < 2:
                L = 2  # The first prime number is 2

            limit = int(math.sqrt(R)) + 1
            primes = simple_sieve(limit)  # Step 1: Find small primes up to sqrt(R)

            is_prime_range = [True] * (R - L + 1)

            # Step 2: Mark multiples of small primes in range [L, R]
            for prime in primes:
                # Find the smallest multiple of 'prime' within [L, R]
                start = max(prime * prime, (L + prime - 1) // prime * prime)
                
                for j in range(start, R + 1, prime):
                    is_prime_range[j - L] = False

            # Step 3: Collect the primes from the range
            return [i for i in range(L, R + 1) if is_prime_range[i - L]]

        a=segmented_sieve(left,right)
        if len(a)<2:
            return [-1,-1]
        if len(a)==2:
            return a
        ans=0
        min1=float("inf")
        for i in range(len(a)-1):
            if a[i+1]-a[i] <min1:
                ans=[a[i],a[i+1]]
                min1=a[i+1]-a[i]
        return ans