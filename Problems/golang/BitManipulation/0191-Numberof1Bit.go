func hammingWeight(num uint32) int {
    ans := 0
    for i := 0; i < 32; i++ {
        if (num & (1 << i)) >> i == 1 {
            ans += 1
        }
    }
    return ans
}