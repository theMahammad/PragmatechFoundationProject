function addClass() {
    document.body.classList.add("sent");
  }
  
  sendLetter.addEventListener("click", addClass);
  (function(){
    // set flag to indicate whether we should wait or actually submit
    var delaySubmit = true;
    // get form el
    var form = document.getElementById('oley');
    form.addEventListener("submit", function(e) {
  
      // if we've already waited the 2 seconds, submit
      if( ! delaySubmit )
        return;
  
      // otherwise, stop the submission
      e.preventDefault();
      // set the flag for next time
      delaySubmit = false;
  
      // and resubmit in 2 seconds. 
      window.setTimeout(function() {
          form.submit();
      }, 4000);
    });
  })();