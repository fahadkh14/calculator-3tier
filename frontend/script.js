const API_URL = "http://localhost:5000";


// Calculate Function

async function calculate(operation){


    const num1 = document.getElementById("num1").value;

    const num2 = document.getElementById("num2").value;



    if(num1 === "" || num2 === ""){

        showResult("Enter Numbers");

        return;

    }



    try{


        const response = await fetch(
            `${API_URL}/calculate`,
            {

            method:"POST",

            headers:{

                "Content-Type":"application/json"

            },


            body:JSON.stringify({

                num1:Number(num1),

                num2:Number(num2),

                operation:operation

            })


        });



        const data = await response.json();



        showResult(data.result);



        loadHistory();



    }

    catch(error){

        console.log(error);

        showResult("Server Error");

    }



}





// Display Result

function showResult(value){


    document.getElementById("result").innerHTML=value;


}





// Load History

async function loadHistory(){


    try{


        const response = await fetch(
            `${API_URL}/history`
        );


        const data = await response.json();



        const history =
        document.getElementById("history");



        history.innerHTML="";



        if(data.length === 0){


            history.innerHTML=
            "<li>No calculations yet</li>";


            return;

        }





        data.forEach(item=>{


            const li=document.createElement("li");



            li.innerHTML=`

            ${item.num1}

            <b>${getSymbol(item.operation)}</b>

            ${item.num2}

            =

            <strong>${item.result}</strong>

            `;



            history.appendChild(li);



        });



    }

    catch(error){


        console.log(error);


    }


}





// Operation Symbol

function getSymbol(operation){


    const symbols={

        add:"+",

        sub:"−",

        mul:"×",

        div:"÷"

    };


    return symbols[operation] || operation;


}





// Load history when page opens

loadHistory();
