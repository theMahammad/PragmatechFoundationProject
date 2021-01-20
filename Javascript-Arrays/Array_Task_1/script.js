let ededler=[1,3,4,90,23,890,12,30,4,3,67,21];


/*TASK 1 */
    let sum = 0;
    function sumArray(array){
        
        for( let i = 0; i < array.length ;i++){
            sum+=array[i];
        }
        return sum;

    }
    console.log("Sum : "+sumArray(ededler))
/*TASK 2*/  
    let sumEven = 0;
    function sumEvens(array){
        
        for( let i = 0; i < array.length ;i++){
            if( array[i]%2 == 0 )
            sumEven+=array[i];
        }
        return sumEven;

    }
    console.log("Sum of Even Numbers : " + sumEvens(ededler))
/*TASK 3*/
    let sumOdd = 0;
    function sumOdds(array){
        
        for( let i = 0; i < array.length ;i++){
            if( array[i]%2 )
            sumOdd+=array[i];
        }
        return sumOdd;

    }    
    console.log("Sum of Odd Numbers : " +sumOdds(ededler))
/*TASK 4*/

    let countForEquals = 0;

    function findEquals(array){
        
        for( let i = 0; i < array.length ;i++){
            if( array[i] == array[i++] ){
            countForEquals++;

                }
        }
        
        return (countForEquals/2);
        }
    

    
    console.log("Number  of Equals number : " + findEquals(ededler)) 
/*TASK 5*/  
        
    let countTwoDigits = 0;
    function findTwoDigit(array){
        for( let i = 0; i < array.length ;i++){
            if( array[i] > 9 ){

                countTwoDigits++;

            }
        }
        return countTwoDigits;
    }
    console.log(findTwoDigit(ededler))
/*TASK 6*/  
        
    
    function sortReverse(inputArr) { 
        let n = inputArr.length;
            
        for(let i = 0; i < n; i++) {
           
            let max = i;
            for(let j = i+1; j < n; j++){
                if(inputArr[j] > inputArr[max]) {
                    max=j; 
                }
            }
            if (max != i) {
                
                let tmp = inputArr[i]; 
                inputArr[i] = inputArr[max];
                inputArr[max] = tmp;      
            }
        }
        return inputArr;
    }
    console.log(sortReverse(ededler))
