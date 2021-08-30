const longest = (s1:  string, s2: string): string => {
    return [...new Set([...new Set(s1)].concat([...new Set(s2)]))].sort().join('');
}
