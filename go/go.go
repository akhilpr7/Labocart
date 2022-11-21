package main

import (
  "database/sql"
  "fmt"
  "github.com/jasonlvhit/gocron"
  _ "github.com/lib/pq"
  "time"
  "math"
  "io"
  "crypto/rand"
  
)

const (
  host     = "db"
  port     = 5432
  user     = "labouser"
  password = "123"
  dbname   = "labocart"
)

func EncodeToString(max int) string {
  b := make([]byte, max)
  n, err := io.ReadAtLeast(rand.Reader, b, max)
  if n != max {
      panic(err)
  }
  for i := 0; i < len(b); i++ {
      b[i] = table[int(b[i])%len(table)]
  }
  return string(b)
}

var table = [...]byte{'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}


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
  gocron.Every(2).Second().Do(fetchsub, db)
  gocron.Every(2).Second().Do(rating, db)
  // gocron.Every(5).Second().Do(expiry2, db)

  gocron.Every(5).Second().Do(copytohire, db)
  gocron.Every(5).Second().Do(refund, db)
  gocron.Every(5).Second().Do(hirexpiry, db)
  gocron.Every(10).Second().Do(requestToHire, db)
	<-gocron.Start()
  
}

func workStatus(db *sql.DB){
  var id int
  var worker_name string
  var job_title string
  var wallet_worker float64
  var rate float64
  // fetchsub(db)
  fetch_id := db.QueryRow(`SELECT id FROM ecommerce_hiremodel WHERE worker_status=true AND user_status=1`)
  fetch_id.Scan(&id)
  fetch_id1 := db.QueryRow(`SELECT worker_name FROM ecommerce_hiremodel WHERE id=$1 `,id)
  fetch_id1.Scan(&worker_name)
  fetch_id2 := db.QueryRow(`SELECT job_title FROM ecommerce_hiremodel WHERE id=$1 `,id)
  fetch_id2.Scan(&job_title)
  fetch_id3 := db.QueryRow(`SELECT wallet FROM authentication_newusermodel WHERE username=$1 `,worker_name)
  fetch_id3.Scan(&wallet_worker)
  fetch_id4 := db.QueryRow(`SELECT rate FROM ecommerce_hiremodel WHERE id=$1 `,id)
  fetch_id4.Scan(&rate)
  sqlStatement01 := `UPDATE authentication_labourmodels SET status=1 WHERE  username = $1 AND job_title = $2;`
  _,err01:= db.Exec(sqlStatement01,worker_name,job_title)
  if err01 != nil {
    fmt.Println("------2")
    panic(err01)
  }
  sqlStatement02 := `UPDATE authentication_newusermodel SET wallet=$1 WHERE  username = $2;`
  _,err02:= db.Exec(sqlStatement02,wallet_worker+rate,worker_name)
  if err02 != nil {
    fmt.Println("------2")
    panic(err02)
  }

  sqlStatement := `
  UPDATE ecommerce_hiremodel
  SET status=4, worker_status=false, user_status=0 
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
  var id int
  var status int
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
      row01,_:= db.Query(
        `SELECT  id,status FROM authentication_labourmodels WHERE username=$1;`,username)
      defer row01.Close()
      for row01.Next(){
        row01.Scan(&id,&status)
        _,err := db.Exec(`UPDATE authentication_labourmodels SET status = 0 WHERE id = $1 AND status = 1;`,id)
        if err != nil {
          fmt.Println("err")
        }

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
		`SELECT  avg(rating),worker_name FROM ecommerce_hiremodel WHERE status=4 group by worker_name;`  )
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
  fetch,err3 := db.Query(`SELECT id,hirer,name,place,work_type,phone,status,job_title,rate,worker_uname,worker_phone FROM home_appliedjobs WHERE status= 1 `)
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
  work_date := time.Now()
  fmt.Println(work_date)
  var otp string
  otp=EncodeToString(6)
  for {
  if len([]rune(otp)) != 6{
    otp=EncodeToString(6)
  }else{
    break
  }
  }
    // fmt.Println(len([]rune(otp)),"lengthhhhhhhhhhhhhhhhhhh")

  
  sqlStatement := `
  INSERT INTO ecommerce_hiremodel("worker_name","Hire_name","Name","Place","Work_mode","Phone","status","job_title","user_status","worker_status","rating","created_at","rate","worker_phone","work_date","comment","otp")  VALUES($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16,$17);`
  _, err := db.Exec(sqlStatement,worker_name,hirer,name,place,work_type,phone,3,job_title,"0","false","0",created_at,rate,worker_phone,work_date,"",otp)
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
  var otp string
  otp=EncodeToString(6)
  for {
  if len([]rune(otp)) != 6{
    otp=EncodeToString(6)
  }else{
    break
  }
  }
  sqlStatement := `
  INSERT INTO ecommerce_hiremodel("worker_name","Hire_name","Name","Place","Work_mode","Phone","status","job_title","user_status","worker_status","rating","comment","created_at","rate","work_date","worker_phone","otp")  VALUES($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16,$17) ;`
  _, err := db.Exec(sqlStatement,worker_name,hirer,name,place,work_type,phone,3,job_title,"0","false","0","",created_at,rate,work_date,worker_phone,otp)
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
  var status int
  fetch,err := db.Query(`SELECT created_at,id,status FROM ecommerce_requestsmodel WHERE status=3 or status=0`)
  if(err!= nil){
    panic(err)
  }
  defer fetch.Close()
  for fetch.Next(){
    fetch.Scan(&created_at,&id,&status)
    if status == 0 {
      current_date := time.Now()
      difference := current_date.Sub(created_at)
      diff := difference.Hours()
      fmt.Println(diff)
      fmt.Println("-----------")
      if diff > 1{
        // var rate float64
        // var hirer string
        // var wallet float64
        // row1 := db.QueryRow(`SELECT rate FROM ecommerce_requestsmodel WHERE id=$1`,id)
        // row1.Scan(&rate)
        // row2 := db.QueryRow(`SELECT hirer FROM ecommerce_requestsmodel WHERE id=$1`,id)
        // row2.Scan(&hirer)
        // row3 := db.QueryRow(`SELECT wallet FROM authentication_newusermodel WHERE username=$1`,hirer)
        // row3.Scan(&wallet)
        
        // sqlStatement1 :=`
        // UPDATE authentication_newusermodel
        // SET wallet = $1
        // WHERE username = $2;`
        // _, err3 := db.Exec(sqlStatement1,wallet+rate,hirer)
        // if err3 != nil {
        //   fmt.Println("------2")
        //   panic(err)
        // }
  
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
        fmt.Println("Deleting req model")
        if err4 != nil {
          fmt.Println("------3")
          panic(err4)
        }
      }
    }else if status == 3 {
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
        fmt.Println("Deleting req model")
        if err4 != nil {
          fmt.Println("------3")
          panic(err4)
        }


        // sqlStatement2 :=`
        // UPDATE ecommerce_requestsmodel
        // SET status = 5
        // WHERE id = $1;`
        // _, err4 := db.Exec(sqlStatement2,id)
        // fmt.Println("updating req model")
        // if err4 != nil {
        //   fmt.Println("------3")
        //   panic(err4)
        // }

    }
  }
}}

func refund(db *sql.DB){
  // fmt.Println("refund process ....")
  
  fetch,err := db.Query(`SELECT created_at,id,rate FROM ecommerce_hiremodel WHERE user_status = 2 and status = 3`)
  if(err!= nil){
    panic(err)
  }
  defer fetch.Close()
  for fetch.Next() {
    var id int
    var rate float64
    var created_at time.Time
    var job_title string
    fetch.Scan(&created_at,&id,&rate)
    current_date := time.Now()
    difference := current_date.Sub(created_at)
    diff := difference.Hours()
    // fmt.Println("Difference :-------",diff)
    var worker_name string
    var hirer_name string
    var wallet_hirer float64
    var wallet_worker float64
    var work_mode string
    // fmt.Println(diff,"difference......")
    if diff >= 0.5{

      percenthirer := 0.6
      // fmt.Println("60/100 = ",percenthirer)
      percentworker := 0.4
      // fmt.Println("40/100 = ",percentworker)
      // fmt.Println(rate,"Rate is")
      // fmt.Println("refund to worker(40%)")
      refundworker := rate*percentworker
      refundhirer := rate*percenthirer
       
      // fmt.Println(refundhirer,"refundhirer")
      // fmt.Println(refundworker,"refundworker")
      fetch2 := db.QueryRow(`SELECT "worker_name","Hire_name","job_title","Work_mode" FROM ecommerce_hiremodel WHERE id =$1`,id)
      fetch2.Scan(&worker_name,&hirer_name,&job_title,&work_mode)
      // fmt.Println(hirer_name,"hirer is ")
      // fmt.Println(worker_name,"worker is ")
      row2 := db.QueryRow(`SELECT wallet FROM authentication_newusermodel WHERE username=$1`,worker_name)
      row2.Scan(&wallet_worker)
      sqlStatement1 :=`
      UPDATE authentication_newusermodel
      SET wallet = $1
      WHERE username = $2;`
      // fmt.Println(wallet_worker+refundworker,"refund to worker  ")
      _, err3 := db.Exec(sqlStatement1,wallet_worker+refundworker,worker_name)
      if err3 != nil {
        fmt.Println("------2")
        panic(err3)
      }
      row1 := db.QueryRow(`SELECT wallet FROM authentication_newusermodel WHERE username=$1`,hirer_name)
      row1.Scan(&wallet_hirer)
      
      sqlStatement2 :=`
      UPDATE authentication_newusermodel
      SET wallet = $1
      WHERE username = $2;`
      // fmt.Println(wallet_hirer+refundhirer,"refund to hirer   ")
      _, err4 := db.Exec(sqlStatement2,wallet_hirer+refundhirer,hirer_name)
      if err4 != nil {
        fmt.Println("------2")
        panic(err4)
      }

      sqlStatement6 :=`
      UPDATE ecommerce_hiremodel
      SET status = 5
      WHERE id = $1;`
      // fmt.Println(wallet_hirer+refundhirer)
      _, err6 := db.Exec(sqlStatement6,id)
      if err6 != nil {
        fmt.Println("------2")
        panic(err6)
      }
      
      sqlStatement8 :=`
      UPDATE ecommerce_hiremodel
      SET user_status = 0
      WHERE id = $1;`
      // fmt.Println(wallet_hirer+refundhirer)
      _, err8 := db.Exec(sqlStatement8,id)
      if err8 != nil {
        fmt.Println("------2")
        panic(err8)
      }

      sqlStatement01 := `UPDATE authentication_labourmodels SET status=1 WHERE  username = $1 AND job_title = $2;`
      _,err01:= db.Exec(sqlStatement01,worker_name,job_title)
      if err01 != nil {
        fmt.Println("------2")
        panic(err01)
      }
      sqlStatement02 := ` INSERT INTO ecommerce_refundhistory(hirer,worker,rate,worker_refund,hirer_refund,work_mode,job_title,work_date,status) VALUES($1,$2,$3,$4,$5,$6,$7,$8,$9)`
      _,err02:= db.Exec(sqlStatement02,hirer_name,worker_name,rate,refundworker,refundhirer,work_mode,job_title,created_at,1)
      if err02 != nil {
        fmt.Println("------2")
        panic(err02)
      }
    }else{
      // fmt.Println("refund to worker(0%)")
      fetch5 := db.QueryRow(`SELECT "Hire_name" FROM ecommerce_hiremodel WHERE "id" = $1`,id)
      fetch5.Scan(&hirer_name)
      fetch01 := db.QueryRow(`SELECT "worker_name" FROM ecommerce_hiremodel WHERE "id" = $1`,id)
      fetch01.Scan(&worker_name)
      fetch02 := db.QueryRow(`SELECT "job_title" FROM ecommerce_hiremodel WHERE "id" = $1`,id)
      fetch02.Scan(&job_title)
      fetch03 := db.QueryRow(`SELECT "Work_mode" FROM ecommerce_hiremodel WHERE "id" = $1`,id)
      fetch03.Scan(&work_mode)
      fmt.Println(work_mode,"---------")
      row5 := db.QueryRow(`SELECT wallet FROM authentication_newusermodel WHERE username=$1`,hirer_name)
      row5.Scan(&wallet_hirer)

      sqlStatement10 :=`
      UPDATE authentication_newusermodel
      SET wallet = $1
      WHERE username = $2;`
      // fmt.Println(wallet_hirer+rate,"refundhirer")
      _, err5 := db.Exec(sqlStatement10,wallet_hirer+rate,hirer_name)
      if err5 != nil {
        fmt.Println("------2")
        panic(err5)
      }
      sqlStatement7 :=`
      UPDATE ecommerce_hiremodel
      SET status = 5
      WHERE id = $1;`
      // fmt.Println(wallet_hirer+refundhirer)
      _, err7 := db.Exec(sqlStatement7,id)
      if err7 != nil {
        fmt.Println("------2")
        panic(err7)
      }

      sqlStatement9 :=`
      UPDATE ecommerce_hiremodel
      SET user_status = 0
      WHERE id = $1;`
      // fmt.Println(wallet_hirer+refundhirer)
      _, err9 := db.Exec(sqlStatement9,id)
      if err9 != nil {
        fmt.Println("------2")
        panic(err9)
      }
      
      sqlStatement01 := `UPDATE authentication_labourmodels SET status=1 WHERE  username = $1 AND job_title = $2;`
      _,err01:= db.Exec(sqlStatement01,worker_name,job_title)
      if err01 != nil {
        fmt.Println("------2")
        panic(err01)
      }


      sqlStatement02 := ` INSERT INTO ecommerce_refundhistory(hirer,worker,rate,worker_refund,hirer_refund,work_mode,job_title,work_date,status) VALUES($1,$2,$3,$4,$5,$6,$7,$8,$9)`
      _,err02:= db.Exec(sqlStatement02,hirer_name,worker_name,rate,0,rate,work_mode,job_title,created_at,2)
      if err02 != nil {
        fmt.Println("------2")
        panic(err02)
      }

    }

  }
}

func hirexpiry(db *sql.DB){

  fetch,err := db.Query(`SELECT created_at,id,rate FROM ecommerce_hiremodel WHERE status = 3`)
  if(err!= nil){
    panic(err)
  }
  defer fetch.Close()
  for fetch.Next() {
    var id int
    var rate float64
    var created_at time.Time
    var job_title string
    var user_status int
    var worker_status bool
    fetch.Scan(&created_at,&id,&rate)
    current_date := time.Now()
    difference := created_at.Sub(current_date)
    diff := difference.Hours()/24
    // fmt.Println("Difference :-------",diff)
    var worker_name string
    var hirer_name string
    var wallet_hirer float64
    // var wallet_worker float64
    var work_mode string
    // fmt.Println(diff,"DAYSSSSSSSSSSSS")
    if diff >= 1{
      // fmt.Println("wooooooooooo")
      fetch1 := db.QueryRow(`SELECT user_status,worker_status FROM ecommerce_hiremodel WHERE id=$1`,id)
      fetch1.Scan(&user_status,&worker_status)
      // fmt.Println(user_status,"sssssssssssssssssssssssss",worker_status)
      if (user_status==0) && (worker_status==false){
        fmt.Println("entered both false!!")
        fetch5 := db.QueryRow(`SELECT "Hire_name" FROM ecommerce_hiremodel WHERE "id" = $1`,id)
        fetch5.Scan(&hirer_name)
        fmt.Println(hirer_name,"hireeeer")
        fetch01 := db.QueryRow(`SELECT "worker_name" FROM ecommerce_hiremodel WHERE "id" = $1`,id)
        fetch01.Scan(&worker_name)
        fmt.Println(worker_name,"worker")

        fetch02 := db.QueryRow(`SELECT "job_title" FROM ecommerce_hiremodel WHERE "id" = $1`,id)
        fetch02.Scan(&job_title)
        fmt.Println(job_title,"job")
        fetch03 := db.QueryRow(`SELECT "Work_mode" FROM ecommerce_hiremodel WHERE "id" = $1`,id)
        fetch03.Scan(&work_mode)
        fmt.Println(work_mode,"work mode")
        fmt.Println(work_mode,"---------")
        row5 := db.QueryRow(`SELECT "wallet" FROM authentication_newusermodel WHERE username=$1`,hirer_name)
        row5.Scan(&wallet_hirer)
        fmt.Println(wallet_hirer,"wallet hirer")
        fmt.Println(wallet_hirer+rate,"refund issued /pay")
        sqlStatement10 :=`
        UPDATE authentication_newusermodel
        SET wallet = $1
        WHERE username = $2;`
        // fmt.Println(wallet_hirer+rate,"refundhirer")
        _, err5 := db.Exec(sqlStatement10,wallet_hirer+rate,hirer_name)
        if err5 != nil {
          fmt.Println("------2")
          panic(err5)
        }
        sqlStatement7 :=`
        UPDATE ecommerce_hiremodel
        SET status = 5
        WHERE id = $1;`
        // fmt.Println(wallet_hirer+refundhirer)
        _, err7 := db.Exec(sqlStatement7,id)
        if err7 != nil {
          fmt.Println("------2")
          panic(err7)
        }
        // sqlStatement9 :=`
        // UPDATE ecommerce_hiremodel
        // SET user_sta
        // WHERE id = $1;`
        // // fmt.Println(wallet_hirer+refundhirer)
        // _, err9 := db.Exec(sqlStatement9,id)
        // if err9 != nil {
        //   fmt.Println("------2")
        //   panic(err9)
        // }
        
        sqlStatement01 := `UPDATE authentication_labourmodels SET status=1 WHERE  username = $1 AND job_title = $2;`
        _,err01:= db.Exec(sqlStatement01,worker_name,job_title)
        if err01 != nil {
          fmt.Println("------2")
          panic(err01)
        }
  
  
        sqlStatement02 := ` INSERT INTO ecommerce_refundhistory(hirer,worker,rate,worker_refund,hirer_refund,work_mode,job_title,work_date,status) VALUES($1,$2,$3,$4,$5,$6,$7,$8,$9)`
        _,err02:= db.Exec(sqlStatement02,hirer_name,worker_name,rate,0,rate,work_mode,job_title,created_at,2)
        if err02 != nil {
          fmt.Println("------2")
          panic(err02)
        }
  

      }else if (user_status==0) && (worker_status==true){
        fmt.Println("worker status  true")
    
        var wallet_worker float64
       
        // fetchsub(db)
     
        fetch_id1 := db.QueryRow(`SELECT worker_name FROM ecommerce_hiremodel WHERE id=$1 `,id)
        fetch_id1.Scan(&worker_name)
        fmt.Println(worker_name,"worker")
        fetch_id2 := db.QueryRow(`SELECT job_title FROM ecommerce_hiremodel WHERE id=$1 `,id)
        fetch_id2.Scan(&job_title)
        fmt.Println(job_title,"job")
        fetch_id3 := db.QueryRow(`SELECT wallet FROM authentication_newusermodel WHERE username=$1 `,worker_name)
        fetch_id3.Scan(&wallet_worker)
        fmt.Println(wallet_worker,"worker wallet")
        // fetch_id4 := db.QueryRow(`SELECT rate FROM ecommerce_hiremodel WHERE id=$1 `,id)
        // fetch_id4.Scan(&rate)
        // fmt.Println()
        sqlStatement01 := `UPDATE authentication_labourmodels SET status=1 WHERE  username = $1 AND job_title = $2;`
        _,err01:= db.Exec(sqlStatement01,worker_name,job_title)
        if err01 != nil {
          fmt.Println("------2")
          panic(err01)
        }
        fmt.Println(wallet_worker+rate,"refund issued /pay")
        sqlStatement02 := `UPDATE authentication_newusermodel SET wallet=$1 WHERE  username = $2;`
        _,err02:= db.Exec(sqlStatement02,wallet_worker+rate,worker_name)
        if err02 != nil {
          fmt.Println("------2")
          panic(err02)
        }
      
        sqlStatement := `
        UPDATE ecommerce_hiremodel
        SET status=4, worker_status=false, user_status=0 
        WHERE id = $1;`
        _, err := db.Exec(sqlStatement, id)
        if err != nil {
          panic(err)
        }
        
  

      }
      }
    }

    }
  