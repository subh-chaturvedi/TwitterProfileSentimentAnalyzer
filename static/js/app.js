console.log("Activated");

const onClickGenerateSentiment=async ()=>{
    console.log("sentiment button clicked");
    var handle = document.getElementById("handlevalue");
    console.log(handle);
    console.log(handle.value);
    var url = "http://127.0.0.1:4996/get_sentimentanalysis_overall"; //Use this if NOT using nginx
    // var url = "/api/get_sentimentanalysis_overall"; // Use this if using nginx

    var resulted = document.getElementById("resultshowcase1");

    
    resulted.innerHTML ="<h2 class=\"result1\">Loading.....</h2>"
    const data = new FormData
    data.append("username",handle.value)

    const res = await fetch(url,{
        method: 'POST',
        body:data
    })
    const res_data = await res.json()
    console.log(res_data );
    resulted.innerHTML = "<h2 class=\"result1\"> The Average Sentiment is: "+res_data.avg_sentiment_text.toString()+" with a specific value of "+res_data.avg_sentiment_float.toString()+"</h2>";


    console.log("kslfksjbb")

}

// window.onload = onPageLoad
