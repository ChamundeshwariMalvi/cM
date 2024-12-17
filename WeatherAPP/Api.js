// console.log("Navbar")

// console.log("world")

// console.log("haii")

// setTimeout(()=>{
//     console.log("Navbar")

// },3000)

// console.log("body")

// setTimeout(()=>{
//     console.log("body data")
// },5000)

// console.log("Footer")
// console.log("one")


// setTimeout(() => {
//      console.log("five")
// })



// setTimeout(() => {
//     console.log("Jai shree ram")
// },3000)

// console.log("three")


// API---------------------------Application Programming Interface----------------------------

const 


let para=document.getElementById("parafacts")
let button=document.getElementById("btn")

async function getfacts() {
    console.log("getting data.....")
    let data=await fetch(URL)
    console.log("hehehe",data)
    let actualdata = await data.json();
    console.log("hahaha",actualdata);

}