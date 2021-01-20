userList=[
    {
        name:'Sabir',
        email:'sabir@mail.com',
        userTasks:[
            {
                taskName:'Task01',
                taskDeadline:2
            },
            {
                taskName:'Task02',
                taskDeadline:8
            },
            {
                taskName:'Task03',
                taskDeadline:10
            }

        ]
    },
    {
        name:'Hesen',
        email:'hesen.mail.com',
        userTasks:[
            {
                taskName:'XTask01',
                taskDeadline:2
            },
            {
                taskName:'XTask02',
                taskDeadline:15
            },
            {
                taskName:'XTask03',
                taskDeadline:4
            }

        ]
    }
]
//1
    function findUserTasksByName(userName){
        for (let check in userList){
            if(userList[check].name == userName){
                return userList[check].userTasks;
            }
        }
    } 
    console.log(findUserTasksByName("Hesen"))
//2
    function userEmailCheck(){
        // butun istifadecilerin mail adreslerinin duzgun olub olmadigini yoxlayin (mail daxilinde @ isaretinin olub olmamasi)
        for (let i = 0; i < userList.length;i++){
            if(  userList[i].email.includes("@") == false ){
                console.log(userList[i].name) 
            }
        }
        // duzgun olmayan mail adresi varsa o mailin hansi istifadeciye aid oldugunu ekrana cap edin
    } 
    userEmailCheck()
//3     
    function findLongestDeadline(){
        let max = 0;
        //maksimum deadline-ı tapmaq
            userList.forEach(user => {
            user.userTasks.forEach(tasks  => {
                if(tasks.taskDeadline > max){

                    max = tasks.taskDeadline;
                    
                }
            })
            });
        //maksimum deadline-ın bilgilərini çapa vermək
            for (let i = 0; i < userList.length; i++ ){
            
                for(let j = 0; j <userList[i].userTasks.length;j++){
                    if(userList[i].userTasks[j].taskDeadline == max){
                        console.log(`Adı : ${userList[i].name}\nTapşırığı :${userList[i].userTasks[j].taskName}\nSon müddəti :${userList[i].userTasks[j].taskDeadline}`)
                    }
                }
            }
        

        
    }



findLongestDeadline()