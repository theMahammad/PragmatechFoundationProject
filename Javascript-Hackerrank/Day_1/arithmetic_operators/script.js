

/**
*   Calculate the area of a rectangle.
*
*   length: The length of the rectangle.
*   width: The width of the rectangle.
*   
*	Return a number denoting the rectangle's area.
**/
function getArea(length, width) {
    let area;
    // Write your code here
    if(length > 1000 && width > 1000){
        return;
    }else{
        area = length*width
        return area;
    }

    
    
}

/**
*   Calculate the perimeter of a rectangle.
*	
*	length: The length of the rectangle.
*   width: The width of the rectangle.
*   
*	Return a number denoting the perimeter of a rectangle.
**/
function getPerimeter(length, width) {
    let perimeter;
    // Write your code here
     if(length > 1000 && width > 1000){
        return;
    }else{
        perimeter = length*2 + width*2
         return perimeter;
    }
    
   
}

console.log(getArea(5,6))

