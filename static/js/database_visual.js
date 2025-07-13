function openPopup() {
    document.getElementById('popupOverlay').classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closePopup() {
    document.getElementById('popupOverlay').classList.remove('active');
    document.body.style.overflow = 'auto';
}

function switchTab(tab) {
    // Remove active class from all tabs and content
    document.querySelectorAll('.tab-button').forEach(btn => btn.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
    
    // Add active class to clicked tab and corresponding content
    event.target.classList.add('active');
    document.getElementById(tab + '-tab').classList.add('active');
}

// Close popup when clicking outside
document.getElementById('popupOverlay').addEventListener('click', function(e) {
    if (e.target === this) {
        closePopup();
    }
});

// Close popup with Escape key
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closePopup();
    }
});

// Form submission handlers
document.getElementById('employeeForm').addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Employee form submitted! 🎉');
    closePopup();
});

document.getElementById('assetForm').addEventListener('submit', function(e) {
    e.preventDefault();
    alert('Asset form submitted! 🎉');
    closePopup();
});

// Add some interactive effects
document.querySelectorAll('.form-input, .form-select').forEach(input => {
    input.addEventListener('focus', function() {
        this.parentElement.style.transform = 'translateY(-2px)';
    });
    
    input.addEventListener('blur', function() {
        this.parentElement.style.transform = 'translateY(0)';
    });
});

//getting data from the employee_form

document.getElementById('employeeForm').addEventListener("submit", function(e) {
     e.preventDefault();

     try {
        const employee_data = {
            'employee_id': Number(document.getElementById("employee_id_emp_form").value),
            'employee_fullname': document.getElementById("employee_fullname").value.trim(),
            'employee_email' : document.getElementById("employee_email").value.trim(),
            'type' : "employee_form"
        };

        if (Number.isNaN(employee_data.employee_id)) {
            alert("Something Wrong : Invalid ID ");
            throw new Error("Something Wrong! : invalid ID!");
        };

        // verifying the email 
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(employee_data.employee_email)) {
            alert("Something Wrong! : Invalid Email !")
            throw new Error("You Email is not valid !")
        };

        // let globalVariable = employee_data.employee_id;

        fetch('/asset_table',{
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body: JSON.stringify(employee_data)
        })
        .then(resp => {
            if (!resp.ok) {
                throw new Error(`Htttp bad request! : ${resp.status}`);
            }
            return resp.json();
        })
        .then(data => { 
            if (data.success) {
                console.log("DATA SENT SUCCESSFULLY!");
                window.location.href = '/admin'
            } else {
                throw new Error("SOMETHING WRONG! : DATA NOT SENT.");
            }
        })
        .catch(err => {
            console.error(err);
        });
    } catch(err) {
        console.error(err);
    };
});


// handling now the asset form 
document.getElementById("assetForm").addEventListener("submit", function(e) {
    e.preventDefault();
    try{
        const asset_data = { 
            'asset_serial' : document.getElementById("asset_serial").value.trim(),
            'employee_id' : Number(document.getElementById("employee_id_asset_form").value),
            'asset_type' : document.getElementById("asset_type").value.trim(),
            'first_using_date': document.getElementById("first_using_date").value,
            'last_using_date' : document.getElementById("last_using_date").value,
            'type' : "asset_form"
        };
        console.log(asset_data);
        
        if (Number.isNaN(asset_data.employee_id)) {
            throw new Error("SOMETHING WRONG! : Invalid ID");
        };

        // send data using fetch API (again!) to the backend
        fetch('/asset_table',{
            method: "POST",
            headers: {"Content-Type":"application/json"},
            body: JSON.stringify(asset_data)
        })
        .then(resp => {
            if(!resp.ok) {
                alert("SOMETHING WENT WRONG : HTTP BAD REQUEST!")
                throw new Error(`Http bad request : ${resp.status}`);
            };
            return resp.json();
        })
        .then(data => {
            if (data.success) {
                console.log("DATA SENT SUCCESSFULLY!");
                console.log(data.success)
                window.location.href = '/admin'
            } else {
                throw new Error("SOMETHING WRONG! : ",(data.error ||"Oops!"));
            };
        })
        .catch(err => {
            console.error(err);
        })
    } catch(err) {
        console.error(err);
    };
});