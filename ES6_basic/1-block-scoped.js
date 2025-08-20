/**
 * taskBlock - Demonstrates block scoping with const.
 * Depending on the input, inner block variables are not
 * accessible outside of their scope.
 *
 * @param {boolean} trueOrFalse - Condition to trigger block scope.
 * @returns {Array} An array with the outer `task` and `task2` values.
 */
export default function taskBlock (trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    const task = true;
    const task2 = false;
    // these shadow the outer variables only inside this block
  }

  return [task, task2];
}
