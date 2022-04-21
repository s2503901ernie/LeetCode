func countOdds(low int, high int) int {
    n := 0
    if low % 2 == 1 || high % 2 == 1 {
        n = 1
    }
    n += (high - low) / 2
    return n
}
