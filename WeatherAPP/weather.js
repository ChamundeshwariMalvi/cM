apiKey ="7d0ae8e07a451b02c1038473ad8443af"
apiUrl="https://api.openweathermap.org/data/2.5/weather?&units=metric&q=";

const searchBox=document.querySelector(".search input");
const searchBtn=document.querySelector(".search button");

let weatherIcon=document.querySelector(".weather-icon");

async function checkWeather(city){
    const response= await fetch(apiUrl + city + `&appid=${apiKey}`)

    if(response.status == 404){
        document.querySelector(".error").style.display="block"
        document.querySelector(".weather").style.display="none"
    }
    else{
        let data=await response.json();
        console.log(data)
        document.querySelector(".city").innerHTML=data.name;
        document.querySelector(".temp").innerHTML=Math.round (data.main.temp) + "°C"
        document.querySelector(".wind").innerHTML=data.wind.speed + "Km.h"
        document.querySelector(".humidity").innerHTML=data.main.humidity + "%"


        if(data.weather[0].main == "clear"){
            weatherIcon.src = "images/clear.png";
        }
        else if (data.weather[0].main == "clouds"){
            weatherIcon.src = "images/clouds.png";
        }
        else if (data.weather[0].main == "rain"){
            weatherIcon.src ="images/rain.png";
        }
        else if (data.weather[0].main == "mist"){
            weatherIcon.src = "images/mist.png";
        }
        else if (data.weather[0].main == "drizzle"){
            weatherIcon.src = "images/drizzle.png";
        }
        document.querySelector(".error").style.display="none"
        document.querySelector(".weather").style.display="block"



    }

}
searchBtn.addEventListener("click",()=>{
    checkWeather(searchBox.value)
}) 