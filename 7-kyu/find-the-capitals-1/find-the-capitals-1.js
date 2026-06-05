var capitals = function (word) {
  // Write your code here
  let capitalList = [];
  for (let i = 0; i < word.length; i++) {
    let char = word[i];
    if (char === char.toUpperCase() && char !== char.toLowerCase()) {
      capitalList.push(i);
    } else {
      continue;
    }
  } 
  return capitalList;
};