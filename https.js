const https = require("https");

async function get_articles(threshold){
    try{
        let articles = [];
        let {data,page,total_pages} =  await get_articles_api();
        articles = [...data];
        for(let i=Number(page)+1;i<=total_pages;i++){
            let {data,total_pages:t_pages} =await get_articles_api({page:i});
            if(t_pages > total_pages){
                total_pages = t_pages;
            }
            articles = [...articles,...data];
        }
       return articles.reduce((acc,article)=>{
           if(article.submission_count > threshold){
                acc.push(article.username);
           }
           return acc;
       },[]);
    }catch(e){
        console.log(e)
    }
}
function get_articles_api({page}={page:1}){
    return new Promise((resolve,reject)=>{
        https.get(`https://jsonmock.hackerrank.com/api/article_users/search?page=${page}`, (res)=>{
            let buffer_data = '';
            res.on('data', function(d) {
                buffer_data += d.toString();
            });
            res.on("end",()=>{
                resolve(JSON.parse(buffer_data));
            })   
        })
    })
    
}
get_articles(10).then(console.log);