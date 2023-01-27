function onClickGenerateSentiment() {
    console.log("sentiment button clicked");
    var handle = document.getElementById("handlevalue");
    console.log(handle);
    var url = "http://127.0.0.1:5000/get_sentimentanalysis_overall"; //Use this if NOT using nginx
    // var url = "/api/get_sentimentanalysis_overall"; // Use this if using nginx

    var estPrice = document.getElementById("resultshowcase1");

    $.post(url, {
        username: handle.value
    },function(data, status) {
        console.log(data);
        estPrice.innerHTML = "<h2 class=\"result1\"> The Average Sentiment is: "+data.avg_sentiment_text.toString()+" with a specific value of "+data.avg_sentiment_float.toString()+"</h2>";
        console.log(status);    
    });
    console.log("Reached End -1");

}

// window.onload = onPageLoad;