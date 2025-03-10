$(function(){
    const BASE_URL = "https://1608-2600-4041-2dc-9400-fcfe-cef0-f39a-6a08.ngrok-free.app";
    var container=$("container")
    
    // declare all characters
    const characters ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

    let resetCount = 0; // Reset only once at initialization
    
    // This function logs user action and sends to backend
    function logUserAction(action, additionalData = {}){
        const timestamp = new Date().toISOString();
        
        //only generate new user ID if there is a new session
        const userID = generateUserID(5); 
        console.log(userID); //print ID
        
        const logData = {
            userID: userID,
            action: action,
            timestamp: timestamp,
            additionalData: additionalData,
        }
        
        // forward to NGROk
        fetch(`/logSliderData`, {  // Use the ngrok URL here
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(logData)  // Send your drawing data
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log("Data sent successfully:", data);
        })
        .catch(error => {
            console.error("Error sending data:", error);
        });

    };

    //Helper function: Generate random string for user ID
    function generateUserID(length){
        let result = ' ';
        const charactersLength = characters.length;
        for ( let i = 0; i < length; i++ ) {
            result += characters.charAt(Math.floor(Math.random() * charactersLength));
        }
    
        return result;
    };

    // Initialize sliders for jQuery Mobile
    $("#AS-arousal, #AS-pleasure").slider();

    //Arousal slider
    $("#AS-arousal").on("input change", function () {
        let value = $(this).val();
        console.log("Arousal value:", value);
        logUserAction(`Arousal Slider Moved`, { arousalValue: value });
    });

    $("#AS-pleasure").on("input change", function () {
        let value = $(this).val();
        // console.log("Pleasure value:", value);
        logUserAction(`Pleasure Slider Moved`, { pleasureValue: value });
    });

    //refresh sliders for jquery mobile
    $("#AS-arousal, #AS-pleasure").slider("refresh");


    $('#new-image-button').on("click", function() {
        console.log("New image button clicked");

        const timestamp = new Date().toISOString();
        
        //only generate new user ID if there is a new session
        const userID = generateUserID(5); 
        console.log(userID); //print ID

        $.ajax({
            url:'/getNewImage', 
            type: 'POST', 
            contentType: 'application/json',
            data: JSON.stringify({
                // This is the data to send
                arousal: $("#AS-arousal").val(),
                pleasure: $("#AS-pleasure").val(),
                timestamp: timestamp,
                userID: userID,
            }), 
            success: function(data) {
                // Success function
                // $("#result").text(data.result);
                console.log(data);

                // Set the image as the returned image
                let returned_img_url = data["img_url"]
                $('#emotion-img').attr('src', returned_img_url);
            }
        });
    })
});