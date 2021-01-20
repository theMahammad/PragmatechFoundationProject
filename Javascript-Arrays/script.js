function findCharAtWords(word,char){
    let count = 0;
    let arrWord = Array.from(word)
    for(let i = 0;i< arrWord.length;i++){
        if(arrWord[i]== char){
            count++;

        }

    }
    return count;
}
console.log(findCharAtWords("Mehemmed",))
function findNotCaseSenseChar(word,char){
    let count = 0;
    let arrWord = Array.from(word)
    for(let i = 0;i< arrWord.length;i++){
        if(arrWord[i]== char){
            count++;

        }

    }
    return count;
}