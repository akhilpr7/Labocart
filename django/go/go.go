package main

import (
  "database/sql"
  "fmt"
  "github.com/jasonlvhit/gocron"
  _ "github.com/lib/pq"
  "time"
  "math"
)

const (
  host     = "localhost"
  port     = 5432
  user     = "labouser"
  password = "123"
  dbname   = "labocart"
)

func main() {
  psqlInfo := fmt.Sprintf("host=%s port=%d user=%s "+
    "password=%s dbname=%s sslmode=disable",
    host, port, user, password, dbname)
  db, err := sql.Open("postgres", psqlInfo)
  if err != nil {
    panic(err)
  }
  defer db.Close()

  err = db.Ping()
  if err != nil {
    panic(err)
  }

  fmt.Println("Successfully connected!")
  gocron.Every(2).Second().Do(workStatus, db)
  gocron.Every(1).Second().Do(fetchsub, db)
  gocron.Every(60).Second().Do(rating, db)
	<-gocron.Start()
}

func workStatus(db *sql.DB){
  var id int
  fmt.Println("hooooo")
  // fetchsub(db)
  fetch_id := db.QueryRow(`SELECT id FROM ecommerce_hiremodel WHERE user_status=true AND worker_status=true `)
  fetch_id.Scan(&id)
  sqlStatement := `
  UPDATE ecommerce_hiremodel
  SET status=3
  WHERE id = $1;`
  _, err := db.Exec(sqlStatement, id)
  if err != nil {
    panic(err)
  }
  
}

func fetchsub(db *sql.DB) {
	// var usernames []string
  fmt.Println("fuvvvvvvvv")
  var username string
	var subscribed_at time.Time
	var packagenum int
  var validity float64
	row,_ := db.Query(
    `SELECT username FROM authentication_newusermodel WHERE is_sub=true;`  )
  defer row.Close()
  for row.Next(){
    row.Scan(&username)
    row1 := db.QueryRow(
     `SELECT subscribed_at FROM authentication_newusermodel WHERE username = $1` ,username)
    row1.Scan(&subscribed_at)
    row2 := db.QueryRow(
     `SELECT package FROM authentication_newusermodel WHERE username = $1` ,username)
    row2.Scan(&packagenum)
    row3 := db.QueryRow(
     `SELECT validity FROM ecommerce_packagemodel WHERE id = $1` ,packagenum)
    row3.Scan(&validity)
    

    current_date := time.Now()
    difference := current_date.Sub(subscribed_at)
    diff := difference.Hours()/24
    fmt.Println(diff)
    if diff > validity {
      fmt.Println("Oho")
      sqlStatement := `
      UPDATE authentication_newusermodel
      SET is_sub = false
      WHERE username = $1;`
      _, err := db.Exec(sqlStatement, username)
      if err != nil {
        panic(err)
      }
    }
  }
}


func rating(db *sql.DB){

	var rating float64
	// var rating
	var worker_name string 
	// var username string

	// fetchsub(db)
	
	row,_ := db.Query(
		`SELECT  avg(rating),worker_name FROM ecommerce_hiremodel group by worker_name;`  )
		defer row.Close()


for row.Next() {
    // row.Scan(&rating)
    row.Scan(&rating,&worker_name)
	

	rate := int(math.Round(rating))

	_,err := db.Exec(`UPDATE authentication_newusermodel SET rating = $1 WHERE username = $2;`,rate,worker_name )
	if err != nil {
		fmt.Println("err")

		fmt.Println(err)
	}


}

}