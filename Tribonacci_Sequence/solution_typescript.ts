export function tribonacci(trib_sequence: Array<number>, n: number): number[] {
    if (n === 0) return [];

    for (var i = 0; i < (n - 3); i++) {
        let next_sequence = trib_sequence[i] + trib_sequence[i + 1] + trib_sequence[i + 2];
        trib_sequence.push(next_sequence);
    }

    return trib_sequence.splice(0, n);
}