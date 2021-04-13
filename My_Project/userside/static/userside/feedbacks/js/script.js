
if( $bool==false ){
    $('.like-or-dislike a').click(function(e){
        e.preventDefault()
        alert("Reaksiya vermək üçün daxil olun")
    })
}else{
    
}
 
        

  
 
  

      $('.card').hover(function(){
         let rest =  jQuery(this).find(".restaurant-logo")
         rest.attr('class','animate__animated animate__flash')
         let read_more =  jQuery(this).find(".read-more")
         read_more.attr('class','d-inline-block animate__animated animate__tada')
         let stars =  jQuery(this).find(".taste-rating-score")
         stars.addClass('animate__animated animate__flip')
         let srv_stars =  jQuery(this).find(".service-rating-score")
         srv_stars.addClass('animate__animated animate__flip')
         let atmp_stars =  jQuery(this).find(".atmp-rating-score")
         atmp_stars.addClass('animate__animated animate__flip')
      })
     
    
 