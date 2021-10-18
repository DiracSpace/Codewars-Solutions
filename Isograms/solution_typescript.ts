export function isIsogram(str: string): boolean {
    const duplicates_array = str.split('').map(c => c.toLocaleLowerCase());
    const uniques_array = Array.from(new Set(duplicates_array));
    return (duplicates_array.length === uniques_array.length);
}