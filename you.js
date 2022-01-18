function formatDate(userDate) {
  // format from M/D/YYYY to YYYYMMDD
  //let s = d.toJSON().slice(0,10).split`-`.join``;
  return userDate.toJSON().slice(0, 10).split`/`.join``;
}

console.log(formatDate("12/31/2014"));
