function display(){

    let birthmahina = document.getElementById("birthmonth").value;
    let birthsaal = document.getElementById("birthyear").value;

    let currentmahina = document.getElementById("current-month").value;
    let currentsaal = document.getElementById("current-year").value;

    let mm;
    let yyyy;

    if (birthmahina > currentmahina) {
        // 20
        mm = 12-(birthmahina-currentmahina);
        yyyy = (currentsaal-birthsaal)-1;
        document.getElementById("output").innerHTML = "Your Current Age is " + yyyy + "Years and " + mm + "Months";
    }

    else if(birthmahina < currentmahina){
        // 20
        mm = (currentmahina-birthmahina);
        yyyy = currentsaal-birthsaal;
        document.getElementById("output").innerHTML = "Your Current Age is " + yyyy + "Years and " + mm + "Months";
    }

    else if(birthmahina < 0 || birthsaal < 0 || currentmahina < 0 || currentsaal < 0){
        // if input is in minus
        document.getElementById("output").innerHTML = "Something wrong with Input";
    }

    else {
        // 21

        yyyy = currentsaal-birthsaal;
        document.getElementById("output").innerHTML = yyyy;
    }




}