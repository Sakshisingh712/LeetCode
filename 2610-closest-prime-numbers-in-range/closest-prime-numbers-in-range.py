class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        min_dist = float('inf')
        p = 2
        result = [-1, -1]
        prime_pairs = [True] * (right + 1)
        prime_pairs[0] = False
        prime_pairs[1] = False
        while p*p <= right:
            if prime_pairs[p]:
                for i in range(p*p, right+1, p):
                    prime_pairs[i] = False
            p += 1
        primes = [p for p in range(left, right+1) if prime_pairs[p]==True]
        
        if len(primes) < 2:
            return result

        for i in range(len(primes)-1):
            dist = primes[i+1] - primes[i]
            if dist < min_dist:
                min_dist = dist
                result = [primes[i], primes[i+1]]
        return result