// 1 : from (Obyektdən massiv yaratmaq üçün istifadə olunur)
var arr_1 = Array.from("Salam")

console.log(arr_1) // S A L A M
//2 :  pop (sonuncu elementi massivdən silir və həmin elementi return edir)  
let arr_2 = ["M","A",3];
var lastElement = arr_2.pop()
console.log(lastElement) // 3
console.log(arr_2)// M A 
//3 :  reverse (Massivi tərs sıralamaq üçün istifadə olunur)
let reversed = [1,3,7,4].reverse()
console.log(reversed) //  4 7 3 1
// 4 : lastIndexOf (Bir element massivdə  birdən çox yerdə olanda onun sonuncu indeksini göstərmək üçündür )
let lastIndex_4 = [4,5,7,8,4,1,15,90,4].lastIndexOf(4)
console.log(lastIndex_4) // 8
//5 : slice (Əgər bir massivin müəyyən bir hissəsini götürmək istəyiriksə,bu metoddan istifadə edirik)
let arr_5 = [5,6,1,"Azer","Meleyke",87,7,9];
let newArr =arr_5.slice(3,5) //3-cü indeksdən başlayaraq 5-ci indeksə qədər,5 özü daxil deyil(əsas massivdən silmir)
console.log(newArr)// Azer Meleyke
//6 :  shift (Massivin ilk elementini silir və onu return edir)
let arr_6 = ["Salam","Necesen","Ne var,ne yox"]
let firstElement = arr_6.shift()
console.log(firstElement)
console.log(arr_6) // ["Necesen", "Ne var,ne yox"]
//7 : fill (massivin bir hissəsinə və ya tamamına istədiyimiz elementi yazdırmaq üçündür)
let arr_7 = [15,69,3,13,22,25] 
let  arr_7_1 = arr_7.fill(18,2,4) 
console.log(arr_7_1) // [15, 69, 18, 18, 22, 25]
console.log(arr_7) // [15, 69, 18, 18, 22, 25]
let  arrSameElement = arr_7.fill(5) // başlanğıc və son daxil edilməyəndə əvvəldən axıra kimi eyni elementi yerləşdirir
console.log(arrSameElement) // [5, 5, 5, 5, 5, 5]
//8 : includes (daxil edilən dəyərin massivdə olub-olmadığını yoxlayır)
let arr_8 = ["Mehemmed","Sadigzade","Eli","Abbasli","Memmed"]
console.log(arr_8.includes("Mehemmed")) //true
//9 : join (massivi string halına gətirmək üçün istifadə olunur)
let arr_9 = ["Men","Sen","O"]
let str =  arr_9.join();
console.log(str) //Men,Sen,O
let str1 =  arr_9.join("+"); // əgər nəsə daxil etməsək,vergüllə ayırır.Etsək,daxil etdiyimiz dəyər ilə
console.log(str1) //Men+Sen+O
//10 : concat (Massivləri bir-biriylə birləşdirmək üçündür)
var hege = ["Cecilie", "Lone"];
var stale = ["Emil", "Tobias", "Linus"];
var children = hege.concat(stale);
console.log(children) // ["Cecilie", "Lone", "Emil", "Tobias", "Linus"]
var holly = ["Di Caprio","Brad Pitt"]
var children1 = hege.concat(stale).concat(holly);
console.log(children1) //["Cecilie", "Lone", "Emil", "Tobias", "Linus", "Di Caprio", "Brad Pitt"]