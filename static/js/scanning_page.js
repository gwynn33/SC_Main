function Qrscanner() {
    try {
        function parsingQrdata(qrtext) {
            const parts = qrtext.split(',');
            const obj = {};
            parts.forEach(part => {
                const [key, ...rest] = part.split(':');
                if (key && rest.length > 0) {
                    obj[key.trim()] = rest.join(':').trim();
                }
            });
            return obj;
        }

        function success_scanning(decodedtext,decodedresult) {
            console.log(decodedtext,"this is the qr data");
            const objdata =  parsingQrdata(decodedtext);
            console.log(objdata,"this is the parsed data");
                setTimeout(() => {
                    scanner.clear();
                }, 4000);
                console.log("Data Requested Successfully !");
                // fetch api
                fetch('/scanning',{
                    method:"PUT",
                    headers: {"Content-Type":"application/json"},
                    body: JSON.stringify(objdata)
                })
                .then(resp => resp.json())
                .then(qdata => {
                    if (qdata.success) {
                        console.log("data Sent successfully !");
                        showSuccessPopup()
                    }else {
                        alert("something wrong: ",qdata.message || qdata.error || "Unknown Error");
                    }
                })
                .catch(err => {
                    console.error(err);
                });
            }
        function failed_scanning(error) {    
            console.log("something Wrong : ",error);
            }
            const scanner =  new Html5QrcodeScanner(
                "camera_container",
                {fps:10,qrbox:250},
                false
            )
            scanner.render(success_scanning,failed_scanning);
    }catch (error) {
        console.error(error);
    }
}
Qrscanner();

// Function to show popup
function showSuccessPopup() {
  document.getElementById('popup-overlay').classList.add('active');
  document.body.style.overflow = 'hidden';
}

// Close popup function
document.getElementById('close-popup').addEventListener('click', function() {
  document.getElementById('popup-overlay').classList.remove('active');
  document.body.style.overflow = 'auto';    
});
