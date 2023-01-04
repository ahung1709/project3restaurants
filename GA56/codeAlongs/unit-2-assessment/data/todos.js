let todosArray = [];

function index() {
  return todosArray;
}
function create(createdToDo) {
  createdToDo.done = false;
  createdToDo.each = "sophia";
  createdToDo.id = Math.floor(Math.random() * 100000000);
  todosArray.push(createdToDo);
}

module.exports = { index, create };
