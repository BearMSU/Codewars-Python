function basicOp(operation, value1, value2){
  //Code
  const operators = {
    "+": (a, b) => a + b,
    "-": (a, b) => a - b,
    "*": (a, b) => a * b,
    "/": (a, b) => a / b,
  };
  return operators[operation](value1, value2);
}