let qrdata = null;

function Qrscanner() {      
    try {
        function parsingQrdata(qrtext){
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
            qrdata = parsingQrdata(decodedtext);
            if (!qrdata) {
                throw new Error("DATA NOT EXIST !");
            }

            setTimeout(() => {
                scanner.clear();
            },4000);
            // fetch API to send data of the QRcode !
            fetch('/User/page/scanner',{
                method:"PUT",
                headers:{"Content-Type":"application/json"},
                body: JSON.stringify({...qrdata,
                    type:'qr_scanner'
                })
            })
            
            .then(resp => {
                if (!resp.ok) {
                    throw new Error(`Http bad request : ${resp.status}`);
                }
                return resp.json();
            })

            .then(data => {
                if (data.success) {
                    console.log("DATA SENT SUCCESSFULLY!");
                    showFeedbackPopup();
                } else {
                    alert(data.error || data.message || "UNKNOWN ERROR!")
                    throw new Error("SOMETHING WRONG WE CAN'T SEND THE DATA!");
                }
            })
            
            .catch(err => {
                console.error("Error! : ",err);
            })
        }

        function failed_scanning(error) {
            console.error(error);
        }

        const scanner = new Html5QrcodeScanner(
            "camera_container",
            {fps:10,qrbox:250},
            false
        )
        scanner.render(success_scanning,failed_scanning);

    } catch (error) {
        console.error(error);
    } 
}

Qrscanner();

//just to handle the feedback popup 
document.addEventListener("DOMContentLoaded", () => {
  const overlay = document.getElementById("feedbackOverlay");
  const closeBtn = document.getElementById("closePopupBtn");

  window.showFeedbackPopup = function () {
    overlay.classList.add("active");
    document.body.classList.add("popup-open");
  };

  function hidePopup() {
    overlay.classList.remove("active");
    document.body.classList.remove("popup-open");
  }

  closeBtn.addEventListener("click", hidePopup);

  overlay.addEventListener("click", (e) => {
    if (e.target === overlay) {
      hidePopup();
    }
  });
});



//We are going to handle the data from the form uheheheh !
document.getElementById('feedbackForm').addEventListener("submit", function(e) {
    e.preventDefault() // to intorrupt stupid HTML philosophy!
    // console.log(qrdata);
    
    try {
        // taking inputs from the form !
        const formData = { 
            'temperature': document.querySelector('input[name="temperature"]:checked').value,
            'noise': document.querySelector('input[name="noise"]:checked').value,
            'assetstate':document.getElementById("assetState").value,
            'type' : 'form_submit'
        };

        if (qrdata) {
            Object.assign(formData,qrdata);
        } else {

        }
        console.log(formData);
        //verifying if there is something wrong!
        if (!formData.noise || !formData.assetstate || !formData.temperature) {
            throw new Error("SOMETHING WRONG WITH THE INPUTS!");
        }
        //fetch api again uhehehe!
        fetch('/User/page/scanner', {
            method:"PUT",
            headers: {"Content-Type":"application/json"},
            body: JSON.stringify(formData)
        })
        .then (resp => {
            if (!resp.ok) {
                throw new Error(`http bad request ${resp.status}`);
            }
            return resp.json();
        })
        .then(fdata => {
            if (fdata.success) {
                console.log("DATA IS SENT SUCCESSFULLY!");
                window.location.href = "/User/page/scanner";
            } else {
                throw new Error(fdata.message || fdata.error || "UNKNOWN ERROR!");
            }
        })
        .catch(err => {
            console.error(err);
        })
    } catch(error){
        console.error(error);   
    }
});

