const questions=[
    {
        question:"which one from these is language for front-end?",
        answers:[
            {text:"html" , correct:true},
            {text:"node" , correct:false},
            {text:"express" , correct:false},
            {text:"c++" , correct:false},

        ]
    },
    {
        question: "which is smallest continent in world?",
        answers: [
            {text:"Asia" , correct:false},
            {text:"Australia" , correct:true},
            {text:"Arctic" , correct:false},
            {text:"Africa" , correct:false},
        ]
    },
    {
        question: "which is language is server side?",
        answers: [
            {text:"Node" , correct:true},
            {text:"html" , correct:false},
            {text:"css" , correct:false},
            {text:"Js" , correct:false},
        ]
    },
    {
        question: "which is largest desert in the world?",
        answers: [
            {text:"kalahari" , correct:false},
            {text:"Gobi" , correct:false},
            {text:"sahara" , correct:false},
            {text:"Antarctica" , correct:true},
        ]
    }
];

let questionElement=document.getElementById("question")
let answerButton=document.getElementById("answer-buttons")
let nextButton= document.getElementById("next-btn")

let currentQuestionIndex;
let score;

function startQuiz(){
    currentQuestionIndex=0
    score=0
    showQuestion();
}

function showQuestion(){
    resetState();
    let currentQuestion=questions[currentQuestionIndex];
    let questionNo= currentQuestionIndex + 1;

    questionElement.innerHTML = questionNo + " . " +  currentQuestion.question;

    
    currentQuestion.answers.forEach((answer) => {
        const button=document.createElement("button"); 
        button.innerHTML=answer.text;
        button.classList.add("btn")
        answerButton.appendChild(button);

        if(answer.correct) {
            button.dataset.correct=answer.correct;
        }       

        button.addEventListener("click",selectAnswer)

    })

  

}


function resetState(){
    nextButton.style.display="none"
    while(answerButton.firstChild){
        answerButton.removeChild(answerButton.firstChild)
    }

}

function selectAnswer (event){
    console.log(event)//object of clicked button
    const selectedBtn= event.target;
    const isCorrect=selectedBtn.dataset.correct==="true"

    if(isCorrect){
        selectedBtn.classList.add("correct");
        score++;
    }
    else{
        selectedBtn.classList.add("incorrect");
    }
    
 

    Array.from(answerButton.children).forEach((button)=>{
        if(button.dataset.correct==="true"){
            button.classList.add("correct")
        }

        button.disabled=true

    })    
    
    nextButton.style.display="block"
    

}

function showScore(){
    resetState();
    questionElement.innerHTML=`Your Score is ${score}`
    nextButton.innerHTML="Play Again"
    nextButton.style.display="block"
}

function handleNextButton(){
    currentQuestionIndex++;
    if(currentQuestionIndex<questions.length){
        showQuestion();
    }
    else{
        showScore();
    }
}



nextButton.addEventListener("click",()=>{
    if(currentQuestionIndex < questions.length){
        handleNextButton();
    }
    else{
        startQuiz();
    }
})


startQuiz();