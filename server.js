const express = require('express');
const morgan = require("morgan")

const PORT = process.env.PORT || 3000;
const INDEX = '/index.html';

const server = express()
  .use(morgan("tiny"))
  .use(express.static("./static"))
  .get("/", (req, res) => {
    res.redirect("/index.html")
  })
  .listen(PORT, () => console.log(`Listening on ${PORT}`));
