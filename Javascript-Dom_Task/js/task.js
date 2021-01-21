function createGallery(){
    let body = document.querySelector('body')
    let sectionGallery = document.createElement('section')
    let divContainer = document.createElement('div')
    sectionGallery.setAttribute('id','gallery')
    divContainer.setAttribute('class','container')
    
    
    
    
    
    //dinamik şəkildə şəkilləri yerləşdirmək üçün
    let count = 0;
    for( let forRow = 0; forRow < 2 ;forRow++){
        
        divRow = document.createElement('div')
        divContainer.appendChild(divRow);
        divRow.setAttribute('class','row')
        for( let forCol = 0 ;forCol < 3 ; forCol++){
            count++;
             divCol4 = document.createElement('div')
             divCol4.setAttribute('class','col-4')
               divRow.appendChild(divCol4)
            
                let divBox = document.createElement('div')
                divBox.setAttribute('class','box')
                let img = document.createElement('img')
    
                img.setAttribute('src',`img/${count}.jpg`)
                divBox.appendChild(img)
                divCol4.appendChild(divBox)
          }
    
    }
    sectionGallery.appendChild(divContainer)
    body.appendChild(sectionGallery)
    
}
createGallery();


