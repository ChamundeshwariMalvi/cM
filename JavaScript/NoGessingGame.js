let user1= prompt("Enter number btw 1 to 100");

if(user1>1 && user1<100){
    alert("User2 please guess the number btw 1 to 100")
    let user2;
    let guess=0;
    do{
        User2=prompt("guess a number");
        if(user2>user1){
            alert("Entered number is greater then original")
        }
        else if(user2<user1){

            alert("Entered number is smaller then original")
        }
        guess++;

    }while(user1!=user2)
        alert("You guess it!!! It took "+ guess + " guesses to guess the number")
     
}
else{
    alert("Enter valid number")
}



