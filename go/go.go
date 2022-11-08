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
  host     = "db"
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

//   err = db.Ping()
//   if err != nil {
//     panic(err)
//   }

  fmt.Println("Successfully connected!")
  gocron.Every(2).Second().Do(workStatus, db)
  gocron.Every(100).Second().Do(fetchsub, db)
  gocron.Every(60).Second().Do(rating, db)
  gocron.Every(5).Second().Do(expiry2, db)

  gocron.Every(5).Second().Do(copytohire, db)
	<-gocron.Start()
}

func workStatus(db *sql.DB){
  var id int
  // fetchsub(db)
  fetch_id := db.QueryRow(`SELECT id FROM ecommerce_hiremodel WHERE user_status=true AND worker_status=true `)
  fetch_id.Scan(&id)
  sqlStatement := `
  UPDATE ecommerce_hiremodel
  SET status=4, worker_status=false, user_status=false 
  WHERE id = $1;`
  _, err := db.Exec(sqlStatement, id)
  if err != nil {
    panic(err)
  }
  
}

func fetchsub(db *sql.DB) {
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
    // fmt.Println(diff)
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

func copytohire(db *sql.DB){
  var hirer string
  var name string
  var place string
  var work_type bool
  var phone int64
  var status int
  var job_title string
  var rate float64
  var worker_name string
  var worker_phone string
  var id int

  // fetchsub(db)
  fetch,err3 := db.Query(`SELECT id,hirer,name,place,work_type,phone,status,job_title,rate,worker_name,worker_phone FROM home_appliedjobs WHERE status= 1 `)
  if(err3 != nil){
    panic(err3)
  }
  defer fetch.Close()
  for fetch.Next() {
    fetch.Scan(&id,&hirer,&name,&place,&work_type,&phone,&status,&job_title,&rate,&worker_name,&worker_phone)
  }
  fmt.Println(hirer,name,place,work_type,phone,status,job_title,rate,worker_name,worker_phone)
  if(id != 0){
  sqlStatement := `
  INSERT INTO ecommerce_hiremodel("worker_name","Hire_name","Name","Place","Work_mode","Phone","status","job_title","user_status","worker_status","rating")  VALUES($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11) ;`
  _, err := db.Exec(sqlStatement,worker_name,hirer,name,place,work_type,phone,3,job_title,"false","false","0")
  if err != nil {
    panic(err)
  }
  sqlStatement1 :=`
  UPDATE home_appliedjobs
  SET status = 2
  WHERE id = $1;`
  _, err1 := db.Exec(sqlStatement1,id)
  if err1 != nil {
    panic(err)
  }
  fmt.Println(rate)
  fmt.Println(worker_phone)
}
}


func expiry2(db *sql.DB){

  fmt.Println("Expiry")
  
  var id int
  
  
  var created_at time.Time
  
  validity := 2.0
  
  current_date := time.Now()
  
  fetch_id,_ := db.Query(`SELECT id,created_at FROM ecommerce_hiremodel WHERE status=2 `)
  
  defer fetch_id.Close()
  
  for fetch_id.Next(){
  
  fetch_id.Scan(&id,&created_at)
  
  // current_date := time.Now()
  fmt.Println("done",created_at)
  diff := current_date.Sub(created_at)
  
  fmt.Print(diff.Hours(),"--sdf---")
  
  difference := diff.Hours()/24
  
  if difference > validity {
  
  sqlStatement := `
  
  UPDATE ecommerce_hiremodel set rating=1 WHERE id = $1;`
  
  _, err1 := db.Exec(sqlStatement,id)
  
  fmt.Println("Deleted......")
  
  if err1 != nil {
  
  panic(err1)
  
  }
  
  
  }
  
  
  }
  
  }
