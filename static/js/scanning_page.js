function Qrscanner() {
    try {
        function success_scanning(decodedtext,decodedresult) {
            const data =  JSON.stringify(decodedtext);
                setTimeout(() => {
                    scanner.clear();
                }, 4000);
                alert("Data Requested Successfully !");
                // fetch api
                fetch('/scanning',{
                    method:"PUT",
                    headers: {"Content-Type":"application/json"},
                    body: data
                })
                .then(resp => resp.json())
                .then(qdata => {
                    if (qdata.success) {
                        console.log("data Sent successfully !");
                        // redirect
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