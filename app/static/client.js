const DISTANCE_API = "/distance";
// https://developer.mozilla.org/en-US/docs/Learn/Forms/Sending_forms_through_JavaScript
window.addEventListener( "load", () => {  
    const form = document.getElementById( "distanceForm" );
    const result = document.getElementById("result");
    show_error_msg = e => {result.textContent = 'Could not calculate distance.'}

    form.addEventListener( "submit", function ( event ) {
      console.log("!");
      event.preventDefault();
      const FD = new FormData( form );
      const query = Array.from(FD.entries())
        .reduce(
            (p, n) => p+n[0]+'='+n[1]+'&',
            DISTANCE_API+'?'
        ).slice(0, -1)
    
      result.textContent = "Calculating distance...";
      
      const XHR = new XMLHttpRequest();
  
      XHR.addEventListener( "load", e =>  {
        try {
          result.textContent =
            'The distance is '+(JSON.parse(e.target.responseText).distance).toFixed(2)+' km.'
        } catch (e) {
            show_error_msg(e);
        }
      });
      XHR.addEventListener( "error", show_error_msg);

      XHR.open( "get", query );
      XHR.send();
    } );
  } );
  