var mysql = require('mysql');
var express = require('express');
var app = express();
    
console.log('Get connection ...');
    
var conn = mysql.createConnection({
    host : '172.20.0.2',
    user : 'root',
    password : 'root',
    database : 'devops'
});

conn.connect(function(err) {
    if (err) throw err;
    console.log("Connected!");
});

app.use(express.static(__dirname + '/app'));

app.get("/", function(req, res){
    var cmd = `SELECT * FROM unity`;
    conn.query(cmd, function(err, result) {
        if (err) throw err;
        console.log(result);
        res.render('home.ejs', {result: result});
    });
});

app.get("/unity:number", function(req, res){
    var cmd = `SELECT * FROM (SELECT * FROM unity WHERE id_unite = ${req.params.number} ORDER BY date_insertion DESC LIMIT 10) as quer ORDER BY quer.date_insertion ASC`;
    conn.query(cmd, function(err, result) {
        if (err) throw err;
        res.render(`unity_${req.params.number}.ejs`, {result: result});
    });
});

app.get("/update:number", function(req, res){
    var cmd = `SELECT * FROM (SELECT * FROM unity WHERE id_unite = ${req.params.number} ORDER BY date_insertion DESC LIMIT 1) as quer ORDER BY quer.date_insertion ASC`;
    conn.query(cmd, function(err, result) {
        if (err) throw err;
        res.send({result: result});
    });
});

app.engine('html', require('ejs').renderFile);
app.set('port', process.env.PORT || 6060);
app.set('view engine', 'html');

app.listen(app.get('port'), function () {
    console.log('Express server listening on port ' + app.get('port'));
});

