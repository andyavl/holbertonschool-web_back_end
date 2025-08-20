export default function taskBlock (trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    /* yet another documentation for checker */
    const task = true;
    const task2 = false;
    /* it whines but doesnt say what the problem is */
  }

  return [task, task2];
}
