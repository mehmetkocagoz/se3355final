document.addEventListener("DOMContentLoaded", function(){
     // Date-related functionality
     const daysOfWeek = ["PZ", "PT", "SA", "ÇA", "PE", "CU", "CT"];
     const months = ["OCA","ŞUB","MAR","NİS","MAY","HAZ","TEM","AĞU","EYL","EKİ","KAS","ARA"];
 
     const currentDate = new Date();
     const dayOfWeek = currentDate.getDay();
     const currentDay = daysOfWeek[dayOfWeek];
     const dayOfMonth = currentDate.getDate();
     const month = currentDate.getMonth();
     const monthToText = months[month];
 
     function updateDateElements() {
         document.getElementById("day-of-week").innerHTML = currentDay;
         document.getElementById("day-of-week2").innerHTML = currentDay;
         document.getElementById("day-of-month").innerHTML = dayOfMonth;
         document.getElementById("day-of-month2").innerHTML = dayOfMonth;
         document.getElementById("month").innerHTML = monthToText;
         document.getElementById("month2").innerHTML = monthToText;
     }

    updateDateElements();
    // Geolocation functionality
    const x = document.getElementById("demo");

    function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition, handleGeolocationError);
        } else { 
            x.innerHTML = "Geolocation is not supported by this browser.";
        }
    }

    function showPosition(position) {
        x.innerHTML = "Latitude: " + position.coords.latitude + 
        "<br>Longitude: " + position.coords.longitude;
    }

    function handleGeolocationError(error) {
        x.innerHTML = "Error getting geolocation: " + error.message;
    }

    // Call the getLocation function when the window is loaded
    window.addEventListener("load", getLocation);

    // jQuery DatePicker initialization
    $(document).ready(function(){
        $("#DatePicker").datepicker();
    });

    $(document).ready(function(){
        $("#DatePicker2").datepicker();
    });
});
