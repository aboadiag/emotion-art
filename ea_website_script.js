$(function(){
    const BASE_URL ="";
    var container=$("container")
    
    // declare all characters
    const characters ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

    let resetCount = 0; // Reset only once at initialization
    
    // This function logs user action and sends to backend
    function logUserAction(action, additionalData = {}){
        const timestamp = new Date().toISOString();
        
        //only generate new user ID if there is a new session
        const userID = generateString(5); 
        console.log(userID); //print ID
        
        const logData = {
            action: action,
            timestamp: timestamp,
        }
        
        // forward to NGROk
        fetch(`${BASE_URL}/logSliderData`, {  // Use the ngrok URL here
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
    
}
);