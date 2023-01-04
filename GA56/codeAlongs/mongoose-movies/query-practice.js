// utility to initialize database
require("./config/database");
const Movie = require("./models/movie");
const Performer = require("./models/performer");
const data = require("./data");
const { promiseImpl } = require("ejs");
/*-- For each exercise below, write the code as described --*/
// let p1 = Movie.deleteMany({});
// let p2 = Performer.deleteMany({});

// Promise.all([p1, p2])
//   .then(function (results) {
//     console.log(results);
//     return Performer.create(data.performer);
//   })
//   .then(function (results) {
//     console.log(results);
//     return Movie.create(data.movie);
//   })
//   .then(function (results) {
//     console.log(results);
//   });

// console.log(data.movies);
// console.log(data.performers);

// for (let performer of data.performers) {
//   Performer.create(performer).then((res) => console.log(res));
// }

Promise.resolve()
  .then(function () {
    console.log("HERE");
    // 1) Find all movie docs
    return Movie.find({}); // remember to return the promise!
  })
  .then(function (result) {
    console.log("1): ", result);
    // 2) Find all performer docs
    return Performer.find({});
  })
  .then(function (result) {
    console.log("2): ", result);
    return Movie.find({ mpaaRating: "PG" });
    // Follow the same .then structure used above from this point forward
    // Don't forget to console.log the exercise number also as shown above
    // 3) Find all movies with an MPAA Rating of 'PG'
  })
  .then(function (results) {
    console.log("3): ", results);
    // 4) Find all movies that are still showing
    return Movie.find({ nowShowing: true });
  })

  .then(function (results) {
    console.log("4): ", results);
    // 5) Find all movies with an MPAA Rating of 'PG' or 'PG-13'
    return Movie.find({}).or([{ mpaaRating: "PG" }, { mpaaRating: "PG-13" }]);
  })
  .then(function (results) {
    console.log("5): ", results);
    // 6) Find the first movie found with a releaseYear of 2018
    return Movie.findOne({ releaseYear: 2018 });
  })

  .then(function (results) {
    console.log("6): " + results);
    // 7) Find all movies released after 1980
    return Movie.find({}).where("releaseYear").gt(1980);
  })
  .then(function (results) {
    console.log("7): " + results);
    // 8) Find all movies whose titles start with a 'C'
    // Hint: StackOverflow will show how to use a regular expression
    return Movie.find({}); //dont know how to do
  })
  .then(function (results) {
    console.log("8): " + results);
    // 9) Find the performer named 'Rami Malek'
    return Performer.find({ name: "Rami Malek" });
  })
  .then(function (results) {
    console.log("9): " + results);
    // 10) Find all performers born before 1980
    return Performer.find({}).where("born").lt(1980);
  })
  .then(function (results) {
    console.log("10): " + results);
    // 11) Find all performers whose name starts with a 'J'
    return Performer.find({}); //dont know how to do
  })
  .then(function (results) {
    console.log("11): " + results);
    // 12) Add a reference to performer 'Bill Murray' to
    //     the movie Caddyshack's cast property and save.
    //     console.log the updated movie.

    return Promise.all([
      Performer.findOne({ name: "Bill Murray" }),
      Movie.findOne({ title: "Caddyshack" }),
    ]);
  })
  .then(function (results) {
    const Bill = results[0];
    const caddy = results[1];

    caddy.cast.push(Bill.id);
    return caddy.save();
  })

  .then(function (results) {
    console.log(results);
    process.exit();
  });
