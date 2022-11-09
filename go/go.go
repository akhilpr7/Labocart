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
  // gocron.Every(10).Second().Do(expiry, db)
  gocron.Every(2).Second().Do(workStatus, db)
  gocron.Every(2).Second().Do(requestdelete, db)
  gocron.Every(100).Second().Do(fetchsub, db)
  gocron.Every(60).Second().Do(rating, db)
  // gocron.Every(5).Second().Do(expiry2, db)

  gocron.Every(5).Second().Do(copytohire, db)
  gocron.Every(10).Second().Do(requestToHire, db)
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
    fmt.Println("------1")
    panic(err3)
  }
  defer fetch.Close()
  for fetch.Next() {
    fetch.Scan(&id,&hirer,&name,&place,&work_type,&phone,&status,&job_title,&rate,&worker_name,&worker_phone)
  }
  fmt.Println(hirer,name,place,work_type,phone,status,job_title,rate,worker_name,worker_phone)
  if(id != 0){
  created_at := time.Now()
  fmt.Println(created_at)
  sqlStatement := `
  INSERT INTO ecommerce_hiremodel("worker_name","Hire_name","Name","Place","Work_mode","Phone","status","job_title","user_status","worker_status","rating","comment","created_at")  VALUES($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13) ;`
  _, err := db.Exec(sqlStatement,worker_name,hirer,name,place,work_type,phone,3,job_title,"false","false","0","",created_at)
  if err != nil {
    fmt.Println("------2")
    panic(err)
  }
  sqlStatement1 :=`
  UPDATE home_appliedjobs
  SET status = 2
  WHERE id = $1;`
  _, err1 := db.Exec(sqlStatement1,id)
  if err1 != nil {
    fmt.Println("------3")
    panic(err)
  }
  fmt.Println(rate)
  fmt.Println(worker_phone)
}
}



// func requestToHire(db *sql.DB){
// 	var hirer string
// 	var name string
// 	var place string
// 	var work_type bool
// 	var phone int64
// 	var status int
// 	var job_title string
// 	var rate float64
// 	var worker_name string
// 	var worker_phone string
// 	var id int
// 	var created_at string
  
// 	// fmt.Println("Requesttttttttttttttttttttttttttttttttttttt")
// 	fetch,err := db.Query(`SELECT * FROM "ecommerce_requestsmodel" WHERE "status" = 1 `)
// 	if(err!= nil){
//     fmt.Println("errorrrrrrrrrrrrrrrrrrrrrrrrr aado")
// 		panic(err)
// 	}
//   defer fetch.Close()
// 	for fetch.Next() {
//     fmt.Printf(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
// 	  fetch.Scan(&id,&hirer,&name,&place,&work_type,&phone,&status,&job_title,&rate,&worker_name,&worker_phone,&created_at)
// 	}
//   fmt.Println(id,hirer,name,place,work_type,phone,status,job_title,rate,worker_name,worker_phone,created_at)
//   if(id != 0){
//     created_at := time.Now()
//     fmt.Println(created_at)
//     sqlStatement := `
//     INSERT INTO ecommerce_hiremodel("worker_name","Hire_name","Name","Place","Work_mode","Phone","status","job_title","user_status","worker_status","rating","comment","created_at")  VALUES($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13) ;`
//     _, err := db.Exec(sqlStatement,worker_name,hirer,name,place,work_type,phone,3,job_title,"false","false","0","",created_at)
//     if err != nil {
//       fmt.Println("------2")
//       panic(err)
//     }

// }
// }



func requestToHire(db *sql.DB){
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
	var created_at string
	var work_date string

  fetch,err3 := db.Query(`SELECT id,hirer,name,place,work_type,phone,status,job_title,rate,worker_name,worker_phone,created_at,work_date FROM ecommerce_requestsmodel WHERE status= 1 `)
  if(err3 != nil){
    fmt.Println("------1")
    panic(err3)
  }
  defer fetch.Close()
  for fetch.Next() {
    fetch.Scan(&id,&hirer,&name,&place,&work_type,&phone,&status,&job_title,&rate,&worker_name,&worker_phone,&created_at,&work_date)
  }
  fmt.Println(hirer,name,place,work_type,phone,status,job_title,rate,worker_name,worker_phone,work_date)
  if(id != 0){
  created_at := time.Now()
  fmt.Println(created_at)
  sqlStatement := `
  INSERT INTO ecommerce_hiremodel("worker_name","Hire_name","Name","Place","Work_mode","Phone","status","job_title","user_status","worker_status","rating","comment","created_at","rate","work_date","worker_phone")  VALUES($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16) ;`
  _, err := db.Exec(sqlStatement,worker_name,hirer,name,place,work_type,phone,3,job_title,"false","false","0","",created_at,rate,work_date,worker_phone)
  if err != nil {
    fmt.Println("------2")
    panic(err)
  }
  sqlStatement1 :=`
  UPDATE ecommerce_requestsmodel
  SET status = 2
  WHERE id = $1;`
  _, err3 := db.Exec(sqlStatement1,id)
  if err3 != nil {
    fmt.Println("------3")
    panic(err)
  }
}
}



func requestdelete(db *sql.DB){
  var created_at time.Time
  var id int
  fetch,err := db.Query(`SELECT created_at,id FROM ecommerce_requestsmodel WHERE status=2 or status=0`)
  if(err!= nil){
    panic(err)
  }
  defer fetch.Close()
  for fetch.Next(){
    fetch.Scan(&created_at,&id)
    current_date := time.Now()
    difference := current_date.Sub(created_at)
    diff := difference.Hours()
    fmt.Println(diff)
    fmt.Println("-----------")
    if diff > 1{
      var rate float64
      var hirer string
      var wallet float64
      row1 := db.QueryRow(`SELECT rate FROM ecommerce_requestsmodel WHERE id=$1`,id)
      row1.Scan(&rate)
      row2 := db.QueryRow(`SELECT hirer FROM ecommerce_requestsmodel WHERE id=$1`,id)
      row2.Scan(&hirer)
      row3 := db.QueryRow(`SELECT wallet FROM authentication_newusermodel WHERE username=$1`,hirer)
      row3.Scan(&wallet)
      
      sqlStatement1 :=`
      UPDATE authentication_newusermodel
      SET wallet = $1
      WHERE username = $2;`
      _, err3 := db.Exec(sqlStatement1,wallet+rate,hirer)
      if err3 != nil {
        fmt.Println("------2")
        panic(err)
      }

      sqlStatement3 :=`
      DELETE FROM ecommerce_labopaymentmodel WHERE work_id_id = $1;`
      _, err5 := db.Exec(sqlStatement3,id)
      if err5 != nil {
        fmt.Println("------5")
        panic(err5)
      }
    


      sqlStatement2 :=`
      DELETE FROM ecommerce_requestsmodel WHERE id = $1;`
      _, err4 := db.Exec(sqlStatement2,id)
      if err4 != nil {
        fmt.Println("------3")
        panic(err4)
      }
    }

  }
}