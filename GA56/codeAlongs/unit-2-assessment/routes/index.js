var express = require("express");
var router = express.Router();
var todosDB = require("../data/todos");

/* GET home page. */
router.get("/", function (req, res, next) {
  let todos = todosDB.index();
  res.render("index", { title: "Unit 2 Assessment", todos });
});
router.post("/", function (req, res, next) {
  todosDB.create(req.body);

  res.redirect("/");
});

module.exports = router;
