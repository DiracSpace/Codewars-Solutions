const longest = (s1, s2) => {
    return [...new Set([...new Set(s1)].concat([...new Set(s2)]))].sort().join('');
}
