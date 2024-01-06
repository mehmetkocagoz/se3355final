function submitForm() {
    document.getElementById("cityForm").submit();
}
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

    // jQuery DatePicker initialization
    $(document).ready(function(){
        $("#DatePicker").datepicker();
    });

    $(document).ready(function(){
        $("#DatePicker2").datepicker();
    });
});
