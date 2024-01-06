function submitForm() {
    document.getElementById("cityForm").submit();
}
document.addEventListener("DOMContentLoaded", function () {
    const daysOfWeek = ["PZ", "PT", "SA", "ÇA", "PE", "CU", "CT"];
    const months = ["OCA", "ŞUB", "MAR", "NİS", "MAY", "HAZ", "TEM", "AĞU", "EYL", "EKİ", "KAS", "ARA"];

    function updateDateElements(selectedDate, targetDayOfWeekId, targetDayOfMonthId, targetMonthId) {
        const selectedDateObject = new Date(selectedDate);
        const dayOfWeek = selectedDateObject.getDay();
        const currentDay = daysOfWeek[dayOfWeek];
        const dayOfMonth = selectedDateObject.getDate();
        const month = selectedDateObject.getMonth();
        const monthToText = months[month];

        document.getElementById(targetDayOfWeekId).innerHTML = currentDay;
        document.getElementById(targetDayOfMonthId).innerHTML = dayOfMonth;
        document.getElementById(targetMonthId).innerHTML = monthToText;
    }

    // Initialize date elements with the current date
    updateDateElements(new Date(), "day-of-week", "day-of-month", "month");
    updateDateElements(new Date(), "day-of-week2", "day-of-month2", "month2");

    // jQuery DatePicker initialization
    $(document).ready(function () {
        $("#DatePicker").datepicker({
            onSelect: function (dateText) {
                updateDateElements(dateText, "day-of-week", "day-of-month", "month");
            }
        });

        $("#DatePicker2").datepicker({
            onSelect: function (dateText) {
                updateDateElements(dateText, "day-of-week2", "day-of-month2", "month2");
            }
        });
    });
});

