function longest(s1, s2) {
  // your code
  // 1. Combine the strings
  let combinedString = s1 + s2;
  
  // 2. Pass it to a Set to strip duplicates, then immediately spread it back into an array
  let uniqueChars = [...new Set(combinedString)];
  
  // 3. Sort the unique array and join it into the final string
  return uniqueChars.sort().join("");
}