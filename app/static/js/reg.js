document.addEventListener('DOMContentLoaded', function () {
    // Your code here
    const APIURL = 'https://run.mocky.io/v3/898ebcec-4778-44e8-a6ec-4852243b7bf9';
    const countriesSelect = document.getElementById('countries');
  
    fetch(APIURL)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        data.forEach(country => {
          const option = document.createElement('option');
          option.value = country.value;
          option.text = country.label;
          countriesSelect.appendChild(option);
        });
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });


      const APIURL2 = 'https://run.mocky.io/v3/ec9790e6-3e47-44f4-a5da-fb1bf0fe46e9';
      const citiesSelect = document.getElementById('cities');

      fetch(APIURL2)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then(data2 => {
        data2.forEach(city => {
          const option = document.createElement('option');
          option.value = city.city;
          option.text = city.city;
          citiesSelect.appendChild(option);
        });
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  });