billionSwitches = function (input) {
  return input.reduce((prev, curr, index) => {
    if (index % 2 !== 0) {
      curr = curr * -1;
    }
    return prev + curr;
  }, 0);
};
