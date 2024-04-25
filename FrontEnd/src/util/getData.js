const URL = ''; //waiting for URL from BackEnd

export const fetchAPI = async (URL) =>{
    try {
        const response = await fetch(URL,{
            method:'GET',
            headers:{
                'Content-type':'application/json'
            }
        })
        response ? console.log(response) : console.log('Fetch API FAIL');
    } catch (error) {
        console.log(error);
    }   
}