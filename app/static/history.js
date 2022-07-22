const HISTORY_API = "/history";

window.addEventListener( "load", () => {  4
    const result = document.getElementById("result");
    const tableBody = document.getElementById("tableBody");
    show_error_msg = e => {result.textContent = 'Could not fetch history.'}

    const XHR = new XMLHttpRequest();
    XHR.addEventListener( "load", e =>  {
        try {
        
          (JSON.parse(e.target.responseText)).forEach(query => {
            const row = document.createElement("tr");
            ['origin', 'destination', 'distance'].forEach(
              key => {
                const td = document.createElement('td');
                td.innerText = query[key];
                row.appendChild(td);
              }
            )
            tableBody.appendChild(row);
          });
          result.innerText = ''
        } catch (e) {
          console.log(e)
            show_error_msg(e);
        }
    });
    XHR.addEventListener( "error", show_error_msg);
    XHR.open( "get", HISTORY_API );
    XHR.send();
});
